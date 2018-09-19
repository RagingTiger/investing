#!/usr/bin/env python


# class
class Investing(object):
    """Contains convenience functions for investing calculatios.

    Given the initial funds, yearly appreciation, expense percentage, and the
    number of years, various information can be calculated, including: total
    funds, total dividends, current dividends, monthly dividends, and
    expenses (NOTE: Dividends are reinvested)
    """
    def __init__(self):
        self._years = 30
        self._funds = 10000.0
        self._apr = 0.04
        self._epr = 0.0011
        self._expense = 0.0
        self._netdiv = 0.0
        self._statement = 'Year {0} total funds: {1}, total dividends: {2}, current dividends {3}, monthly dividends:{4}  total expense: {5}'

    def calculate(self):
        # first shorten variables for temporary reasons
        years = self._years
        funds = self._funds
        apr = self._apr
        epr = self._epr
        expense = self._expense
        netdiv = self._netdiv

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
