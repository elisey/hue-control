from setuptools import setup, find_packages
from app.hue import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="hue-control",
    version=__version__,
    description="Utility for controling Hue smart lams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Elisey Ravnyushkin",
    license='MIT',
    url="https://github.com/elisey/hue-control",
    packages=find_packages(),
    install_requires=[
        "phue"
    ],
    entry_points={
        "console_scripts": [
            "hue=app.hue:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
