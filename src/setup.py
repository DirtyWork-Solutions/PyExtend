from setuptools import setup, find_packages

setup(
    name='pyextend',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'omegaconf',
        'configparser',
        'pyutils'
    ],
    entry_points={
        'console_scripts': [
            'pyextend-util=pyextend.utils.ecosystem:determine_util',
        ],
    },
    package_data={
        '': ['*.yaml', '*.ini'],
    },
    include_package_data=True,
    description='A Python project with utility functions and configuration management',
    author='DirtyWork Solutions Limited',
    author_email='pyextend@open.dirtywork.solutions',
    url='https://github.com/DirtyWork-Solutions/pyextend',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13',
)