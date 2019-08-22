"""pip setup file for restgun"""
from setuptools import setup

with open("README.md", "r") as readme:
    DESC = readme.read()

setup(
    name="backdoorgery",
    version="1.0.0",
    author="Samuel Waugh",
    author_email="samuel.swaugh@gmail.com",
    maintainer="Samuel Waugh",
    maintainer_email="samuel.swaugh@gmail.com",
    description="Totally legal and non-ToS breaking API into backloggery.com",
    long_description=DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=["requests>=2.18.4", "pyquery==1.4.0"],
    packages=["backdoorgery"]
)
