from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='django-celery-progress',
    version=version,
    description='',
    #long_description=open('README.md').read(),
    author='Rob Golding',
    author_email='rob@robgolding.com',
    license='BSD',
    url='https://github.com/robgolding63/django-celery-progress',
    download_url=(
        'https://github.com/robgolding63/django-celery-progress/downloads'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'celery',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
)
