from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='wn-client',
    version=version,
    description='Talk to wn framework over HTTP',
    author='Pratik Vyas',
    author_email='pdvyas@erpnext.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)
