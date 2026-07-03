from setuptools import setup, find_packages

setup(
    name="renderlib",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Divy Patel",
    description="A library to render scientific formulas easily.",
    python_requires=">=3.7",
)
