from distutils.core import setup
import py2exe
setup(
    console=['RDL.py'],
    options={
        'py2exe':{
            'packages':['shutil','youtube_dl','urllib'],
            }
        }
    )
