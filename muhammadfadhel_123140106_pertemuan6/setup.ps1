# Setup Script untuk Aplikasi Matakuliah Pyramid
# Jalankan script ini untuk setup otomatis proyek

Write-Host "=== SETUP APLIKASI MATAKULIAH PYRAMID ===" -ForegroundColor Green
Write-Host ""

# 1. Install dependensi Python
Write-Host "1. Installing Python dependencies..." -ForegroundColor Yellow
pip install -e .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error installing dependencies. Please check Python and pip installation." -ForegroundColor Red
    exit 1
}

# 2. Setup Database
Write-Host "2. Setting up database..." -ForegroundColor Yellow
Write-Host "Mencoba PostgreSQL terlebih dahulu..." -ForegroundColor Cyan

# Coba setup PostgreSQL
$usePostgres = $true
psql -U postgres -c "SELECT 1;" 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "PostgreSQL tidak tersedia. Menggunakan SQLite sebagai alternatif." -ForegroundColor Yellow
    $usePostgres = $false
    
    # Update development.ini untuk SQLite
    $configPath = "development.ini"
    $sqliteUrl = "sqlalchemy.url = sqlite:///matakuliah.db"
    $postgresUrl = "sqlalchemy.url = postgresql://postgres:password@localhost:5432/matakuliah_db"
    
    (Get-Content $configPath) -replace $postgresUrl, $sqliteUrl | Set-Content $configPath
    Write-Host "Konfigurasi database diubah ke SQLite." -ForegroundColor Green
} else {
    Write-Host "PostgreSQL tersedia. Menggunakan PostgreSQL." -ForegroundColor Green
    # Coba buat database PostgreSQL
    psql -U postgres -c "CREATE DATABASE matakuliah_db;" 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Database matakuliah_db sudah ada atau gagal dibuat." -ForegroundColor Yellow
    } else {
        Write-Host "Database matakuliah_db berhasil dibuat." -ForegroundColor Green
    }
}

# 3. Jalankan migrasi database
Write-Host "3. Running database migrations..." -ForegroundColor Yellow
alembic upgrade head
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error running migrations. Check database connection." -ForegroundColor Red
    exit 1
}

# 4. Jalankan server
Write-Host "4. Starting Pyramid server..." -ForegroundColor Yellow
Write-Host "Server akan berjalan di background. Tekan Ctrl+C untuk stop." -ForegroundColor Cyan

# Jalankan server di background
Start-Job -ScriptBlock {
    pserve development.ini
} | Out-Null

Start-Sleep -Seconds 3  # Tunggu server start

# 5. Jalankan testing
Write-Host "5. Running API tests..." -ForegroundColor Yellow
python test_api.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed. Check server and database." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== SETUP SELESAI ===" -ForegroundColor Green
if ($usePostgres) {
    Write-Host "Database: PostgreSQL (matakuliah_db)" -ForegroundColor Green
} else {
    Write-Host "Database: SQLite (matakuliah.db)" -ForegroundColor Green
}
Write-Host "Aplikasi berjalan di: http://127.0.0.1:6543" -ForegroundColor Green
Write-Host "API endpoints: /api/matakuliah" -ForegroundColor Green
Write-Host ""
Write-Host "Untuk stop server, tekan Ctrl+C atau tutup terminal." -ForegroundColor Yellow