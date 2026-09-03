@echo off
REM Start MongoDB with mmapv1 storage engine
cd "C:\Program Files\MongoDB\Server\3.2\bin"
mongod --dbpath "C:\data\db" --storageEngine=mmapv1
pause
