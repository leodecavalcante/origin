import setuptools

setuptools.setup(
    name="origin-financial",
    version="0.0.1",
    author="Leonardo Cavalcante",
    author_email="oleocavalcante@gmail.com",
    description="Resolution to Origin Backend Take-Home Assignment",
    url="https://github.com/leodecavalcante/origin",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'datetime']
)
