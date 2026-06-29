#!/usr/bin/env python
"""cumm-rocm: ROCm port of cumm GEMM library using FlyDSL."""

from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")
version = "0.9.0+dtk2604"

setup(
    name="cumm-rocm",
    version=version,
    description="ROCm port of CUda Matrix Multiply library (FlyDSL backend)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZJLi2013/cumm-rocm",
    author="ZJLi2013",
    license="Apache-2.0",
    python_requires=">=3.10",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "cumm": ["csrc_hip/*.cpp", "csrc_hip/*.hip", "csrc_hip/*.h"],
    },
    install_requires=[
        "torch",
        "numpy",
    ],
    extras_require={
        "flydsl": [
            "flydsl",
        ],
    },
)
