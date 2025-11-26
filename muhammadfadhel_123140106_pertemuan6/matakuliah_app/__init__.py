"""Konfigurasi utama aplikasi Pyramid.

File ini mengatur routing, database connection, dan konfigurasi aplikasi.
"""
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from .models import Base

def main(global_config, **settings):
    """Fungsi utama untuk membuat dan mengkonfigurasi aplikasi WSGI.
    
    Args:
        global_config: Konfigurasi global dari file .ini
        **settings: Settings tambahan dari file .ini
        
    Returns:
        WSGI application
    """
    # Setup database engine dan session
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    settings['db_session'] = DBSession

    # Konfigurasi Pyramid
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    
    # Routing - semua endpoint dengan request_method yang spesifik
    config.add_route('home', '/')
    config.add_route('matakuliah_list', '/api/matakuliah', request_method='GET')
    config.add_route('matakuliah_detail', '/api/matakuliah/{id}', request_method='GET')
    config.add_route('matakuliah_create', '/api/matakuliah', request_method='POST')
    config.add_route('matakuliah_update', '/api/matakuliah/{id}', request_method='PUT')
    config.add_route('matakuliah_delete', '/api/matakuliah/{id}', request_method='DELETE')
    
    # Scan views untuk menemukan semua view config
    config.scan('.views')
    return config.make_wsgi_app()
