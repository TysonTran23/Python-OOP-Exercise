"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.original_string = start

    def __repr__(self):
        return f"SerialGenerator start={self.start} next={self.start + 1}"

    def generate(self):
        """Increments the start number by 1 each time it is called"""

        self.start += 1
        return self.start
    
    def reset(self):
        """Resets the start variable back to the original number"""
        self.start = self.original_string




