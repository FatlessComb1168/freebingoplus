@echo off
windres icon.rc -O coff -o icon.res
g++ -static-libgcc -static-libstdc++ freebingoplus.cpp icon.res -o freebingoplus.exe
pause