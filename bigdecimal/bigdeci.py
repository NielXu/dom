"""
BigDecimal can guarantee the results of calculatoins are correct
in given precision range, including integer calculations and
floating point calculations.
"""
class bigdeci():
    """
    BigDecimal

    `num` The number in string format

    `precision` The precision range, it controls how many places will
    be calculated in floating point calculatoins. When doing calculation,
    bigdeci will make sure that the precision is correct in the given
    range. Default is 5
    """
    def __init__(self, num, precision=5):
        self.num_arr = list(num)
        self.precision = precision