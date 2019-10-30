import distutils
from distutils import dir_util
from distutils import file_util

import sys

p = None

if len(sys.argv) > 1:
    print(sys.argv[1:])
    p = sys.argv[1]

name = "WoxGiphy"

if p is None:
    distutils.dir_util.copy_tree(f"C:\\Projects\\{name}", f"C:\\Users\\g\\AppData\\Local\\Wox\\app-1.3.524\\Plugins\\{name}", preserve_mode=0)
else:
    distutils.file_util.copy_file(f"C:\\Projects\\{name}\\main.py", f"C:\\Users\\g\\AppData\\Local\\Wox\\app-1.3.524\\Plugins\\{name}\\main.py", preserve_mode=0)
