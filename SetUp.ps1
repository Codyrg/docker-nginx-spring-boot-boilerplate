docker-compose up -d
# give db container some time to initialize
Start-Sleep -Seconds 15

$dir = Get-Location
Set-Location ./sample-database
python create_tables.py
Set-Location $dir