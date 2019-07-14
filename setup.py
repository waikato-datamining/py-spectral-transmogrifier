from setuptools import setup, find_namespace_packages

setup(
    name="wai.spectra",
    description="Python library for transmogrifying spectral data.",
    long_description="Python library for weird transformations of spectra that have nowhere else to live.",
    url="https://github.com/waikato-datamining/py-spectral-transmogrifier",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 3',
    ],
    license='GNU General Public License version 3.0 (GPLv3)',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where="src"),
    namespace_packages=[
        "wai"
    ],
    version="0.0.1",
    author='Corey Sterling',
    author_email='coreytsterling@gmail.com',
    install_requires=[
        "numpy",
        "pyAudioAnalysis",
        "pypng",
        "wai.keras"
    ]
)
