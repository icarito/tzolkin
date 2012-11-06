from setuptools import setup, find_packages

setup(
    name="tzolkin",
    version="0.1",

    data_files=[
            ('/usr/share/applications', ['tzolkin.desktop']),
            ('/usr/share/pixmaps', ['tzolkin.png'])
    ],

    packages=find_packages(),
    package_data={
        '': ['images/*.png', 'images_big/*.png', 'tonos/*.png'],
    },

    # metadata for upload to PyPI
    author="Sebastian Silva",
    author_email="sebastian@fuentelibre.org",
    description="Tzolkin es un applet para escritorios libres para usar " +
                "el calendario de las 13 lunas.",
    license="GPLv3",
    keywords="tzolkin maya calendar",
    url="http://icarito.github.com/tzolkin/",
    entry_points={
        'console_scripts': [
            'tzolkin-applet = tzolkin.tzolkintray:run',
        ],
    }
)
