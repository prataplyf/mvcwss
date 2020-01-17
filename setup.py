from setuptools import setup, find_packages

PACKAGE_NAME = 'wsspackages'

REQUIRED_PACKAGES = [
    'requests>=2.19.1',
    'tqdm>=4.25.0',
]

setup(
    name= PACKAGE_NAME,
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    package_data={ '': [] },
)

# export/set FLASK_APP=yourapplication  -> export for terminal
# export/set FLASK_ENV=development  -> set for win cmd prompt