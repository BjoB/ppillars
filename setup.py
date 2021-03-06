
#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ppillars',
    version='0.1.0',
    description='Point Pillars Object Detection',
    url='https://github.com/BjoB/ppillars',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Björn Barschtipan',
    author_email='',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=False,
    setup_requires=['wheel'],
    python_requires='>=3.5',
    install_requires=[
        'tensorflow',
        'numpy',
        'pandas',
    ],
    extras_require={
        'dev': [
            'black',
            'pycodestyle',
            'pyflakes',
            'pytest',
        ],
    },
)
