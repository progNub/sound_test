from cx_Freeze import setup, Executable

executables = [Executable('sound.py'
)]



includes = ['pygame', 'pygame.mixer', 'random']

zip_include_packages = ['pygame', 'pygame.mixer', 'random']

include_files = [
'DOM_C.mp3',
'TON_C.mp3',
'subDOM_C.mp3'
]

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name="sound.py",
version="1.0",
description='My app',
executables=executables,
options=options)