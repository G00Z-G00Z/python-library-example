from setuptools import find_packages, setup

with open("./monkey_example_lib/README.md", "r") as f:
    long_description = f.read()

setup(
    name="monkey-lab-lib-example",
    packages=find_packages(include=["./monkey_example_lib"]),
    version="0.0.1",
    description="Monkey Lab example library for understaning how to create a library in Python",
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
