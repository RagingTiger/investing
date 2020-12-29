#!/usr/bin/env python

"""
Description: Misc inflation calculation tools
"""

# class
class Inflation(object):
    """
    Misc inflation calculation tools.
    """
    def __init__(self, rate=0.0246, capital=100, time=10):
        # cache initial vars for repeated usage
        self.rate = rate
        self.init_capital = capital
        self.time = time

    def inflated_value(self):
        """
        Returns "capital" purchasing power after "time" based on "rate" of
        inflation.
        """
        # setup temp var for calculating capital purchasing power and time
        capital = self.init_capital
        time = self.time

        # results container
        results = {}

        # compound
        while time:
            # adjust capital for inflated value every time
            capital = capital - (capital * self.rate)

            # subtract time
            time = time - 1

            # update results dict
            results[self.time - time] = capital

        # results
        return results

    def print_purch_power_decay(self):
        """
        Prints out each year that the inflation eats away at the purchase power.
        """
        # get results from inflation calculations
        results = self.inflated_value()

        # compound
        for year, value in results.items():
            # output
            output_text = (
                           'Purchasing value of {} capital after {} years at an '
                           'inflation rate of {}: {}'
                          ).format(self.init_capital,
                                   year,
                                   '{}%'.format(self.rate * 100),
                                   value)

            # print text
            print(output_text)

    def print_purch_power(self):
        """
        Prints out the "purchasing power" of "capital" after a certain "time"
        and a certain inflation "rate."
        """
        # output
        output_text = (
                       'Purchasing value of {} capital after {} years at an '
                       'inflation rate of {}: {}'
                      ).format(self.init_capital,
                               self.time,
                               '{}%'.format(self.rate * 100),
                               self.inflated_value()[self.time])

        # print text
        print(output_text)


# executable
if __name__ == '__main__':
    # grab 'fire' libary
    import fire

    # bang bang
    fire.Fire(Inflation)
