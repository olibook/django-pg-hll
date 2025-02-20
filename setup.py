from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = []
with open('requirements.txt') as f:
    for line in f.readlines():
        line = line.strip()  # Remove spaces
        line = line.split('#')[0]  # Remove comments
        if line:  # Remove empty lines
            requires.append(line)

setup(
    name='django-pg-hll',
    version='2.1.0',
    packages=['django_pg_hll'],
    package_dir={'': 'src'},
    url='https://github.com/M1hacka/django-pg-hll',
    license='BSD 3-clause "New" or "Revised" License',
    author='Mikhail Shvein',
    author_email='work_shvein_mihail@mail.ru',
    description='Provides a django wrapper for postgresql-hll library by CitusData',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requires
)
