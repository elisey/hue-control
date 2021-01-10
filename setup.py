from setuptools import setup, find_packages

setup(
    name="hue",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "phue"
    ],
    entry_points={
        "console_scripts": [
            "hue=hue.hue:main"
        ]
    }
)