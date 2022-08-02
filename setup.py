from setuptools import find_packages, setup

setup(
    name="test_task",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.*",
    version='0.1.0',
    description='Python Bootcamp Test Tasks',
    author='KyrylR',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
