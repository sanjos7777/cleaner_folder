from setuptools import setup, find_namespace_packages

setup(
    name='cleaner_folder',
    version='0.0.1',
    description='Very useful code for sorting files in selected folder',
    author='Oleksandr Shchyrskyi',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=cleaner_folder.clean:start']}
)