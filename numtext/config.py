from .mappings import mapping_am_short, mapping_eu_long

naming_schemes = {
    'am_short': mapping_am_short,
    'eu_long': mapping_eu_long
}

class Configuration:
    def __init__(self):
        self._naming_scheme = naming_schemes['am_short']

    @property
    def naming_scheme(self):
        return self._naming_scheme

    @naming_scheme.setter
    def naming_scheme(self, value):
        if value not in naming_schemes:
            names = ', '.join([name for name in naming_schemes])
            raise ValueError('Unsupported naming scheme. Supported naming schemes: ' + names)
        self._naming_scheme = naming_schemes[value]

config = Configuration()
