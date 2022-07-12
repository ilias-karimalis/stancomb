#!/usr/bin/env python3

import os
from tkinter import W
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='stancomb',
      version='0.0.1',
      description='We mix Stan models for you!',
      author='Ilias Karimalis',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['stancomb'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['parsec'],
      python_requires='>=3.8',
    #   extras_require={
    #     'gpu': ["pyopencl", "six"],
    #     'testing': [
    #         "pytest",
    #         "torch~=1.11.0",
    #         "tqdm",
    #         "protobuf~=3.19.0",
    #         "onnx",
    #         "onnx2torch",
    #         "mypy",
    #     ],
    #   },
      include_package_data=True)