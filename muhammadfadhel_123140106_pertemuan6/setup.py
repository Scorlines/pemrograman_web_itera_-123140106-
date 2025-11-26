from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_chameleon',
    'sqlalchemy',
    'alembic',
    'waitress',
    'pyramid_debugtoolbar',
    'psycopg2-binary',
]

setup(
    name='matakuliah_app',
    version='1.0',
    description='Aplikasi Manajemen Matakuliah dengan Pyramid',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Muhammad Fadhel',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = matakuliah_app:main',
        ],
    },
)
