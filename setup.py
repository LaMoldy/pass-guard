from setuptools import setup, find_packages

setup(
    name="Pass Guard",
    version="0.0.1",
    description="A GUI application for storing and generating passwords",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nikkolas \"LaMoldy\" Jackson",
    author_email="NikkolasJ@outlook.com",
    url="https://github.com/LaMoldy/pass-guard",
    packages=find_packages(),
    install_requires=[
        "bcrypt",
        "customtkinter",
    ],
    extras_require={
        "dev": ["pytest"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public",
        "Operating System :: OS Independent",
        "Framework :: Tkinter"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "pass-guard=pass-guard.main:main"
        ]
    },
    include_package_data=True,
    package_data={
        "project_name": [
            "resources/images/*",
            "resources/styles/*",
            "resources/config.json"
        ]
    },
    zip_safe=False
)