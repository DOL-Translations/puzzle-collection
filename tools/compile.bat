@echo off

set ISOFile=..\input\Nintendo Puzzle Collection [J].iso
set ISOTargetSize=1459978240

if not exist "%ISOFile%" (
	echo [INFO] "%ISOFile%" was not found
	echo Did you name the ROM correctly and place it in the correct folder?
	echo Exiting in 10 seconds..
	C:\Windows\System32\timeout.exe /t 10 /nobreak >nul
	exit /b 0
)

for %%F in ("%ISOFile%") do (
    set "ISOSize=%%~zF"
)

if %ISOSize% neq %ISOTargetSize% (
    echo [INFO] "%ISOFile%" has an incorrect size
    echo Are you using the uncompressed ROM?
    echo Exiting in 10 seconds..
    C:\Windows\System32\timeout.exe /t 10 /nobreak >nul
    exit /b 0
)

echo [INFO] Compiling patches - Please wait..

//todo: extract .rel
//decompress .rel

bass\\win\\bass.exe ..\\src\\Menu\\Main.asm
bass\\win\\bass.exe ..\\src\\DrMario\\Main.asm
bass\\win\\bass.exe ..\\src\\YCookie\\Main.asm

//todo: compress .rel
//repack .rel

bass\\win\\bass.exe ..\\src\\Main\\Main.asm

echo [INFO] Patches compiled
echo ---------- 
echo Finished!
echo ----------
C:\Windows\System32\timeout.exe /t 5 /nobreak >nul
exit /b 0