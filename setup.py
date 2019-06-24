from setuptools import setup

NAME = "linalg"
DESCRIPTION = "A simple linear algebra package written in vanilla python3"
URL = "https://github.com/rocketll/linalg"
EMAIL = "luc4sl33@gmail.com"
AUTHOR = "Lucas Lee"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "1.0.4"


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name=NAME,
    packages=["linalg"],
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    include_package_data=True,
    keywords=["linear algebra", "math"],
    license="MIT",
)

