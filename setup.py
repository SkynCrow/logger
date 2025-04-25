from setuptools import setup, find_packages

setup(
    name='logger',
    version='0.1.0',
    author='Franco Tardones',
    author_email='ftardones@gmail.com',
    description='A simple logging customization library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/skyncrow/logger',  # Update with your repository URL
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here, for example:
        # 'somepackage>=1.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)