"""Views untuk API Manajemen Matakuliah.

File ini berisi semua endpoint untuk operasi CRUD pada data matakuliah.
"""
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import IntegrityError
import json
from .models import Matakuliah

@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    """Endpoint untuk mendapatkan semua data matakuliah.
    
    Returns:
        dict: Dictionary berisi list semua matakuliah
    """
    dbsession = request.registry.settings['db_session']()
    matakuliahs = dbsession.query(Matakuliah).all()
    return {'matakuliahs': [mk.to_dict() for mk in matakuliahs]}

@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    """Endpoint untuk mendapatkan detail satu matakuliah berdasarkan ID.
    
    Args:
        request: Request object yang berisi parameter ID
        
    Returns:
        dict: Dictionary berisi data matakuliah atau error message
    """
    dbsession = request.registry.settings['db_session']()
    id = int(request.matchdict['id'])
    mk = dbsession.query(Matakuliah).filter_by(id=id).first()
    if mk is None:
        request.response.status = 404
        return {'error': 'Matakuliah not found'}
    return mk.to_dict()

@view_config(route_name='matakuliah_create', renderer='json')
def matakuliah_create(request):
    """Endpoint untuk menambahkan matakuliah baru.
    
    Request body harus berisi: kode_mk, nama_mk, sks, semester
    
    Returns:
        dict: Data matakuliah yang baru dibuat atau error message
    """
    dbsession = request.registry.settings['db_session']()
    try:
        data = request.json_body
        # Membuat instance Matakuliah baru
        mk = Matakuliah(
            kode_mk=data['kode_mk'],
            nama_mk=data['nama_mk'],
            sks=data['sks'],
            semester=data['semester']
        )
        dbsession.add(mk)
        dbsession.commit()
        return mk.to_dict()
    except IntegrityError:
        # Handle jika kode_mk sudah ada (constraint unique)
        dbsession.rollback()
        request.response.status = 400
        return {'error': 'Kode MK must be unique'}
    except KeyError:
        # Handle jika ada field yang hilang
        request.response.status = 400
        return {'error': 'Missing required fields'}

@view_config(route_name='matakuliah_update', renderer='json')
def matakuliah_update(request):
    """Endpoint untuk mengupdate data matakuliah.
    
    Field yang dikirim akan diupdate, field lain tetap.
    
    Returns:
        dict: Data matakuliah yang sudah diupdate atau error message
    """
    dbsession = request.registry.settings['db_session']()
    id = int(request.matchdict['id'])
    mk = dbsession.query(Matakuliah).filter_by(id=id).first()
    
    # Validasi apakah matakuliah dengan ID tersebut ada
    if mk is None:
        request.response.status = 404
        return {'error': 'Matakuliah not found'}
    
    try:
        data = request.json_body
        # Update hanya field yang dikirimkan
        mk.kode_mk = data.get('kode_mk', mk.kode_mk)
        mk.nama_mk = data.get('nama_mk', mk.nama_mk)
        mk.sks = data.get('sks', mk.sks)
        mk.semester = data.get('semester', mk.semester)
        dbsession.commit()
        return mk.to_dict()
    except IntegrityError:
        # Handle jika kode_mk baru sudah digunakan
        dbsession.rollback()
        request.response.status = 400
        return {'error': 'Kode MK must be unique'}

@view_config(route_name='matakuliah_delete', renderer='json')
def matakuliah_delete(request):
    """Endpoint untuk menghapus matakuliah berdasarkan ID.
    
    Returns:
        dict: Confirmation message atau error message
    """
    dbsession = request.registry.settings['db_session']()
    id = int(request.matchdict['id'])
    mk = dbsession.query(Matakuliah).filter_by(id=id).first()
    
    # Validasi apakah matakuliah dengan ID tersebut ada
    if mk is None:
        request.response.status = 404
        return {'error': 'Matakuliah not found'}
    
    # Hapus dari database
    dbsession.delete(mk)
    dbsession.commit()
    return {'message': 'Matakuliah deleted'}