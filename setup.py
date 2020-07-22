from setuptools import setup


setup(
    packages=['pynindo'],
    include_package_data=True,
    use_scm_version=True,
    install_requires=[
        'requests',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    entry_points={
        'console_scripts': [
            'pynindo=pynindo.cli:main',
        ],
    },
)
