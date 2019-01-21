#!/usr/bin/env python
import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = "0.1"


if __name__ == "__main__":
    setup(
        name="LittlePhotoStudio",
        author="Csaba Palankai",
        author_email="csaba.palankai@gmail.com",
        packages=find_packages("src", exclude=["*.tests", "tests", "*.tests.*"]),
        package_dir={"": "src"},
        include_package_data=True,
        version=VERSION,
        license="GPLv3",
        description="Photo organising, editing toolset",
        long_description=read("README.rst"),
        url="https://gitlab.com/palankai/LittlePhotoStudio",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
        ],
        keywords=("photo", "timelapse"),
        zip_safe=False,
        python_requires=">=3.7",
        install_requires=["Click>=7.0'", "opencv-python-headless==4.0.0.21"],
        setup_requires=["pytest-runner", "black"],
        tests_require=["pytest-cov", "colorama", "pytest"],
        entry_points={"console_scripts": ["lps=lps.main:entry_point"]},
    )
