from setuptools import setup, find_packages

setup(
    name='dua',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    'Flask>=3.1,<4.0',
    'requests>=2.32,<3.0',
],
    author='Oskar',
    author_email='mail@oskar.nz',
    description='JSON database allowing for local or remote connection',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oskxzr/dua',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.12',
)