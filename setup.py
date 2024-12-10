import subprocess
from setuptools import Command, find_packages, setup

class BuildExeCommand(Command):
    """Custom command to build an .exe using PyInstaller."""
    description = "Build an .exe file using PyInstaller"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Call PyInstaller to generate the executable
        subprocess.check_call([
            "pyinstaller",
            "--onefile",
            "--name=passguard",
            "--noconsole",
            "pass_guard/main.py"
        ])

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
            "pass-guard=pass_guard.main:main"
        ]
    },
    cmdclass={
        "build_exe": BuildExeCommand,
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