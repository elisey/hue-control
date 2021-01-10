from setuptools import setup, find_packages
from hue.hue import __version__

setup(
    name="hue",
    version=__version__,
    description="Utility for controling Hue smart lams",
    author="Elisey Ravnyushkin",
    license='MIT',
    url="https://github.com/elisey/hue-utility",
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
