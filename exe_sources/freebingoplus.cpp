/*
FreeBingo+ Launcher.
Copyright (C) 2021 by Fedor Egorov <fedoregorov1@yandex.ru>
This file is part of FreeBingo+.

FreeBingo+ is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

FreeBingo+ is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with FreeBingo+. If not, see <https://www.gnu.org/licenses/>.
*/

#include <iostream>
#include <cstdlib>
#include <Windows.h>
using namespace std;

int main() {
    ShellExecute(0, "open", "pythonw.exe", "freebingoplus.pyw", nullptr, SW_HIDE);
    /* system("pythonw.exe freebingoplus.pyw"); */
}
