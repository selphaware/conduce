import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conduce",
    version="0.0.1",
    author="Usman Ahmad",
    author_email="uahmad3013@outlook.com",
    description="A config util package to flatten-reduce long keys",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/selphaware/conduce",
    project_urls={
        "Bug Tracker": "https://github.com/selphaware/conduce/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["PyYAML==5.4.1"]
)
