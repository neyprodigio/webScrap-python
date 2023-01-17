import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("script.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Bet Moni",
    version = "1.0",
    description = "Monitoramento bet365",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
