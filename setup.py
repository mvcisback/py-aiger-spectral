from setuptools import find_packages
from distutils.core import setup

DESC = 'TODO'

setup(
    name='py-aiger-spectral',
    version='0.0.0',
    description=DESC,
    url='http://github.com/mvcisback/py-aiger-spectral',
    author='Marcell Vazquez-Chanlatte',
    author_email='marcell.vc@eecs.berkeley.edu',
    license='MIT',
    install_requires=[
        'py-aiger',
    ],
    packages=find_packages(),
)
