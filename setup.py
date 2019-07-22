import setuptools

setuptools.setup(
    name='restaurantapi',
    version='0.1.0',
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask-restplus',
        'Flask-Migrate',
        'Flask-Script',
        'flask_testing',
        'psycopg2-binary'
    ],
)