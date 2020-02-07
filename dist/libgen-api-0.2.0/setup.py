import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='libgen-api',
    packages=['libgen-api'],
    version='0.2.0',
    description='Search Library genesis by Title or Author',
	long_description=long_description,
    url='https://github.com/harrison-broadbent/libgen-search-api',
    download_url='https://github.com/harrison-broadbent/libgen-api/archive/v0.2.0.tar.gz',
    author='Harrison Broadbent',
    author_email='harrisonbroadbent@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords=['libgen search', 'libgen api', 'search libgen', 'search library genesis'],
    install_requires=['bs4', 'requests', 'lxml']
)