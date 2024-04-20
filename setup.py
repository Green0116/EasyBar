from setuptools import setup, find_packages


setup(
    name='EasyBar',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[],
    python_requires='>=3.6',
    author='University of Liverpool',
)
