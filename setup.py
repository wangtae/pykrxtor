from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('pykrx/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name            = 'pykrx',
    version         = main_ns['__version__'],
    description     = 'KRX data scraping',
    url             = 'https://github.com/sharebook-kr/pykrx',
    author          = 'Brayden Jo, Jonghun Yoo',
    author_email    = 'brayden.jo@outlook.com, jonghun.yoo@outlook.com, pystock@outlook.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires= ['requests', 'pandas', 'datetime', 'numpy', 'xlrd',
                       'deprecated', 'multipledispatch'],
    license         = 'MIT',
    packages        = find_packages(include=['pykrx', 'pykrx.*', 'pykrx.stock.*']),
    python_requires = '>=3',
    zip_safe        = False
)