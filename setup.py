from setuptools import find_packages, setup

with open("./awesome_lib/README.md", "r") as f:
    long_description = f.read()

setup(
    name="my_awesome_lib",
    packages=find_packages(include=["awesome_lib"]),
    version="0.1.2",
    description="My first Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="g00z-g00z",
    license="MIT",
    install_requires=[],
    test_requires=["pytest"],
    extras_require={"dev": ["pytest", "twine"]},
    setup_requires=["pytest-runner"],
    test_suite="awesome_lib/tests",
    python_requires=">=3.9",
)
