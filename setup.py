from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='countrytagger',
    version='0.1.2',
    description="Tag the names of countries and in text.",
    url='https://github.com/alephdata/countrytagger',
    author='OCCRP',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['countrytagger'],
    py_modules=['countrytagger'],
    include_package_data=True,
    install_requires=[
        'normality >= 2.0.0',
        'pyahocorasick >= 1.4.0',
    ],
)
