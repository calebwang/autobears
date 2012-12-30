import telebears

class autoRegistrar:

    def __init__(self):
        self.tb = telebears.Telebears()

    def parse_regfile(self, filename):
        """
        Parse a plaintext file to determine registration behavior.
        Format:
            action ccn; 1st section choice > 2nd > ... > last; 1st lab choice> 2nd > ... > last;
            action ccn; ...
        Example:
            add 12345; 54321 > 43215 > 23415; 12536 > 13464 > 12534
        """

    def register(self, filename):
        """register"""
