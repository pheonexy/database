@echo off
REM Start MongoDB through config file
cd "C:\Program Files\MongoDB\Server\3.2\bin"
mongod -f "C:\Mongodb\mongod.cfg"
pause
