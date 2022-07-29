from setuptools import setup, find_packages

requires = ["click"]

dev_requires = ["bump2version", "pytest", "pytest-sugar"]

setup(
    name="Anagram Checker",
    version="1.0.0",
    description="Anagram checking implementations for teaching purposes.",
    author="Tobias Knuth",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requires,
    extras_require={"dev": dev_requires},
)
