from setuptools import setup, find_packages

setup(
    name="hash-utils",
    version="0.1.0",
    description="A utility package for generating unique hashes with Redis integration",
    author="Abhishek Prakash",
    author_email="abhishekprakash47@gmail.com",
    url="https://github.com/abhishekprakash256/hash-utils",
    packages=find_packages(),
    install_requires=[
        "redis",
        "redis-helper-kit @ git+https://github.com/abhishekprakash256/redis-helper-kit.git"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
