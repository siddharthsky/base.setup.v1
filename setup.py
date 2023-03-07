from setuptools import find_packages,setup
from typing import List

HYPEN_E_DEOT = "-e ."

def get_requirements(file_path:str):
    rx = []
    with open(file_path) as file_obj:
        rx =file_obj.readlines()
        rx= [x.replace("\n","") for x in rx]
        if HYPEN_E_DEOT in rx:
            rx.remove(HYPEN_E_DEOT)
    return rx


setup(
    name="base.setup",
    version="0.0.1",
    author="Siddharth Kamble",
    author_email="Siddharthsk7t@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)


