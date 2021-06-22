""" (ref) https://stackoverflow.com/questions/4870121/python-help-with-from-distutils-core-import-setup
    (ref) https://github.com/jesolem/PCV/blob/master/setup.py
"""

from distutils.core import setup

setup(name='Programming-ComputerVision-Python',
        version='1.0',
        author='DoranLYong',
        url='https://github.com/DoranLyong/Programming-ComputerVision-Python',
        packages=['CVLibs'],
        requires=['NumPy', 'Matplotlib', 'SciPy'],
        )