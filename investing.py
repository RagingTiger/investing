#!/usr/bin/env python

"""
Author: John D. Anderson
Email: jander43@vols.utk.edu
Description: Investing calculator for command line
Usage: TODO
"""


# class
class Investing(object):
    """Contains convenience functions for investing calculatios.

    Given the initial funds, yearly appreciation, expense percentage, and the
    number of years, various information can be calculated, including: total
    funds, total dividends, current dividends, monthly dividends, and
    expenses (NOTE: Dividends are reinvested)
    """
    def __init__(self):
        self.data = {'years': 30, 'funds': 10000.0, 'apr': 0.04,
                     'epr': 0.0011
                     }
        self._statement = self._gen_statement()

    def _gen_column_padding(self):
        # return dict of length data
        return {'yl': len(str(self.data['years'])),
                'fl': len(str(self.data['funds'])),
                'al': len(str(self.data['apr'])),
                'el': len(str(self.data['epr']))
                }

    def _gen_statement(self):
        # get column temp/paddding
        padtemp = '{{{}:>{}.0f}}'
        pad = self._gen_column_padding()

        # generate statement with correct padding
        statement = ('Year {0} | total funds: {1} | total '
                     'dividends: {2} | current dividends {3}, '
                     'monthly dividends:{4}  total expense: {5}'
                     ).format('{0:>3}',
                              padtemp.format('1', pad['fl']),
                              '{2:>6.0f}',
                              '{3:>6.0f}',
                              '{4:>6.0f}',
                              '{5:>6.0f}'
                              )

        return statement

    def calculate(self):
        # first shorten variables for temporary reasons
        data = self.data
        years = data['years']
        funds = data['funds']
        apr = data['apr']
        epr = data['epr']
        expense = 0.0
        netdiv = 0.0

        # now calculate
        for i in range(years):
            roi = funds * apr
            funds = funds + roi
            expense = expense + (funds * epr)
            netdiv = netdiv + roi
            print self._statement.format(i + 1, funds, netdiv, roi, roi/12.0,
                                         expense)

    def _enterprise(self):
        # TODO
        pass

    def _defensive(self):
        # TODO
        pass


if __name__ == '__main__':
    # grab 'fire' libary
    import fire

    # bang bang
    fire.Fire(Investing)
