from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'Predticts Basmati Paddy Seeds '

# Setting up
setup(
    name="Rice_img_cls",
    version=VERSION,
    author="Nimisha_Tiwari",
    author_email="nimi.tiwari08@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'tensorflow', 'keras', 'numpy','matplotlib',],
    keywords=['python', 'Rice', 'Basmati', 'deep learning', 'image classification', 'icgeb'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: '3.7','3.8','3.9','3.10' ",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
