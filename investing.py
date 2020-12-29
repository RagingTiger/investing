#!/usr/bin/env python

"""
Description: Investing calculator for command line
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
        # make shorter reference (for ease of use)
        data = self.data

        # calculate lengths for each variable
        years = len(str(data['years'])) + 1
        totalfunds = years + len(str(data['funds']))
        totaldiv = totalfunds
        currentdiv = totaldiv - 2
        monthlydiv = currentdiv
        totalexp = monthlydiv

        # return dict of length data
        return {'years': years,
                'totalfunds': totalfunds,
                'totaldiv': totaldiv,
                'currentdiv': currentdiv,
                'monthlydiv': monthlydiv,
                'totalexp': totalexp
                }

    def _gen_statement(self):
        # get column temp/paddding
        padtemp = '{{{}:>{}.0f}}'
        pad = self._gen_column_padding()

        # generate statement with correct padding
        statement = ('Year {0} {6} total funds: {1} {6} total '
                     'dividends: {2} {6} current dividends {3} {6} '
                     'monthly dividends:{4} {6} total expense: {5}'
                     ).format(padtemp.format('0', pad['years']),
                              padtemp.format('1', pad['totalfunds']),
                              padtemp.format('2', pad['totaldiv']),
                              padtemp.format('3', pad['currentdiv']),
                              padtemp.format('4', pad['monthlydiv']),
                              padtemp.format('5', pad['totalexp']),
                              '{}|{}'.format(3 * ' ', 3 * ' ')
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
            print(self._statement.format(i + 1, funds, netdiv, roi, roi/12.0,
                                         expense))

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
