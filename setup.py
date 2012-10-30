from setuptools import setup, find_packages

setup(
    name="tzolkin",
    version="0.1",
    packages=find_packages(),
    scripts=['tzolkin-applet'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires = ['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['images/*.png', 'images_big/*.png', 'tonos/*.png'],
        # And include any *.msg files found in the 'hello' package, too:
        #'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Sebastian Silva",
    author_email="sebastian@fuentelibre.org",
    description="Tzolkin es un applet para escritorios libres para usar " +
                "el calendario de las 13 lunas.",
    license="GPLv3",
    keywords="tzolkin maya calendar"
    #url = "http://example.com/HelloWorld/",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)
