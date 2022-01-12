$dir = Get-Location
Set-Location ./sample-database
docker-compose down -v
Set-Location $dir