#!/usr/bin/env python3
"""Script untuk testing API dan menambahkan data awal."""

import requests
import json

# URL server
base_url = 'http://127.0.0.1:6543/api/matakuliah'

def test_get():
    """Test GET endpoint."""
    try:
        response = requests.get(base_url)
        print(f"GET /api/matakuliah: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def add_matakuliah(data):
    """Tambah matakuliah baru."""
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(base_url, json=data, headers=headers)
        print(f"\nPOST /api/matakuliah ({data['nama_mk']}): {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print("=" * 60)
    print("TESTING API MANAJEMEN MATAKULIAH")
    print("=" * 60)
    
    print("\n1. Testing GET (List kosong):")
    print("-" * 60)
    test_get()

    # Data matakuliah untuk ditambahkan
    matakuliahs = [
        {
            "kode_mk": "IF101",
            "nama_mk": "Algoritma dan Pemrograman",
            "sks": 3,
            "semester": 1
        },
        {
            "kode_mk": "IF102",
            "nama_mk": "Struktur Data",
            "sks": 3,
            "semester": 2
        },
        {
            "kode_mk": "IF103",
            "nama_mk": "Basis Data",
            "sks": 3,
            "semester": 3
        }
    ]

    print("\n\n2. Testing POST (Tambah 3 matakuliah):")
    print("-" * 60)
    for mk in matakuliahs:
        add_matakuliah(mk)

    print("\n\n3. Testing GET (Final list):")
    print("-" * 60)
    test_get()
    
    print("\n" + "=" * 60)
    print("TESTING SELESAI")
    print("=" * 60)
