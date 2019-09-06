from setuptools import setup, find_packages
from pathlib import Path
import os

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="alacritty-color-switcher",
    version="0.1.0",
    description="Apply color schemes to your alacritty config.",
    long_description=readme,
    author="Timm Behner",
    author_email="behner@cs.uni-bonn.de",
    url="https://github.com/tbehner/alacritty-color-switcher",
    license=license,
    install_requires=["click", "toml"],
    packages=find_packages(exclude=("tests", "docs")),
    entry_points={"console_scripts": ["acs=alacritty_color_switcher.cli:main"]},
)
