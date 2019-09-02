# spcxbutcher's setup.py
from distutils.core import setup
setup(
    name = "spcxbutcher",
    packages = ["spcxbutcher"],
    version = "0.4",
    description = "SPCX photon data parser",
    author = "Moran Netser",
    author_email = "moran.netser@gmail.com",
    url = "https://github.com/moran-netser/SPCXparser",
    keywords = ["SPCX", "SPC", "photon", "photons"],
    scripts = ['bin/spcx_to_json', 'bin/spcx_to_matlab', 'bin/spcx_view'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics"
        ]
)
