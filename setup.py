import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="gscrape",
    version="0.1",
    author="Malte Bonart",
    author_email="malte@bonart.de",
    description="google scraper tool built-on headless chrome ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/bonartm/gscrape",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['gscrape=gscrape.command_line:main'],
    },
    python_requires='>=3.7',
    include_package_data=True
)
