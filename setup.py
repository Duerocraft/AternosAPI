import setuptools

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setuptools.setup(
    name="AternosAPI",
    version="1.0.0",
    description="A Python Aternos API",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Duerocraft/AternosAPI",
    packages=["aternosapi"],
    install_requires=requirements,
    license="GNU",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
