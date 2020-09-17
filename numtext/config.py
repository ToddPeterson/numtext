from .mappings import mapping_am_short

naming_schemes = {
    'am_short': mapping_am_short
}

class Configuration:
    def __init__(self):
        self._naming_scheme = naming_schemes['am_short']

    @property
    def naming_scheme(self):
        return self._naming_scheme

    @naming_scheme.setter
    def naming_scheme(self, value):
        try:
            self._naming = naming_schemes[value]
        except KeyError:
            names = '/n'.join([f'    {name}' for name in naming_schemes])
            raise ValueError('Unsupported naming scheme. Supported naming schemes are:/n' + names)

config = Configuration()
