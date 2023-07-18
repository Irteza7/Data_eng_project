from setuptools import setup, find_packages

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="weather_project",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'utils': ['*.ini'],
    },
    py_modules=['fetch_n_publish', 'consume_n_store'],
    install_requires=requirements,  # use requirements read from the requirements.txt
)
