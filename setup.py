#
#  FFTerm
#  Play videos in the terminal.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
import setuptools

VERSION = os.environ.get("PYPI_VERSION", "0.1.5")
VERSION = VERSION.split("/")[-1]  # GitHub input


with open("README.md", "r") as fp:
    long_description = fp.read()

with open("requirements.txt", "r") as fp:
    requirements = fp.read().strip().split("\n")

setuptools.setup(
    name="ffterm",
    version=VERSION,
    author="Patrick Huang",
    author_email="phuang1024@gmail.com",
    description="Play media in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phuang1024/ffterm",
    py_modules=["ffterm"],
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ffterm = ffterm.main:main",
        ]
    },
)
