from setuptools import setup, find_packages

setup(
    name='hello_mars',
    version='0.1.0',
    author='Krishna Agarwal',
    author_email='krishnacool781@gmail.com',
    description='Type different strings from different planets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
