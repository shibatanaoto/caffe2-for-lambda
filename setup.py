# coding: utf8

from setuptools import setup

requires = ["requests>=2.18.0"]

long_description = """
"""

setup(
    name='caffe2-for-lambda',
    version='0.0.1',
    description='add links to readme',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Queue-inc/caffe2-for-lambda',
    author='shibatanaoto',
    author_email='shibata@queue-inc.com',
    license='MIT',
    keywords=['lambda'],
    packages=[
        "caffe2-for-lambda",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python'
    ],
)