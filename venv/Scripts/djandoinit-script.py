#!c:\users\joh98\documents\github\portfolio\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'djando==0.2','console_scripts','djandoinit'
__requires__ = 'djando==0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('djando==0.2', 'console_scripts', 'djandoinit')()
    )
