@echo off
echo === SETUP APLIKASI MATAKULIAH PYRAMID ===
echo.

REM 1. Install dependensi Python
echo 1. Installing Python dependencies...
pip install -e .
if %errorlevel% neq 0 (
    echo Error installing dependencies. Please check Python and pip installation.
    pause
    exit /b 1
)

REM 2. Setup Database
echo 2. Setting up database...
echo Mencoba PostgreSQL terlebih dahulu...

REM Cek apakah PostgreSQL tersedia
psql -U postgres -c "SELECT 1;" >nul 2>&1
if %errorlevel% neq 0 (
    echo PostgreSQL tidak tersedia. Menggunakan SQLite sebagai alternatif.
    REM Update development.ini untuk SQLite
    powershell -Command "(Get-Content development.ini) -replace 'sqlalchemy.url = postgresql://postgres:password@localhost:5432/matakuliah_db', 'sqlalchemy.url = sqlite:///matakuliah.db' | Set-Content development.ini"
    echo Konfigurasi database diubah ke SQLite.
    set USE_POSTGRES=0
) else (
    echo PostgreSQL tersedia. Menggunakan PostgreSQL.
    REM Coba buat database PostgreSQL
    psql -U postgres -c "CREATE DATABASE matakuliah_db;" 2>nul
    if %errorlevel% neq 0 (
        echo Database matakuliah_db sudah ada atau gagal dibuat.
    ) else (
        echo Database matakuliah_db berhasil dibuat.
    )
    set USE_POSTGRES=1
)

REM 3. Jalankan migrasi database
echo 3. Running database migrations...
alembic upgrade head
if %errorlevel% neq 0 (
    echo Error running migrations. Check database connection.
    pause
    exit /b 1
)

REM 4. Jalankan server
echo 4. Starting Pyramid server...
echo Server akan berjalan di background. Tekan Ctrl+C untuk stop.
start "Pyramid Server" cmd /c "pserve development.ini"

REM Tunggu server start
timeout /t 3 /nobreak >nul

REM 5. Jalankan testing
echo 5. Running API tests...
python test_api.py
if %errorlevel% neq 0 (
    echo Tests failed. Check server and database.
    pause
    exit /b 1
)

echo.
echo === SETUP SELESAI ===
if "%USE_POSTGRES%"=="1" (
    echo Database: PostgreSQL (matakuliah_db)
) else (
    echo Database: SQLite (matakuliah.db)
)
echo Aplikasi berjalan di: http://127.0.0.1:6543
echo API endpoints: /api/matakuliah
echo.
echo Untuk stop server, tutup jendela command prompt server.
pause