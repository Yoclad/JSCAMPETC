# Zeke


import FixedTradeGetter
from FixedTradeGetter import *
import time


class Trader:

    def __init__(self, flux_range, past_trade_feed, symbol, correction_rate):
        self.fair_price_est = fair_price_est
        self.past_trade_feed = past_trade_feed
        self.correction_rate = correction_rate
        self.position = position
        self.symbol = symbol
        self.flux_range = flux_range

    def correction_rate_finder(self):
        self.past_trade_feed = 5

        trade_list = FixedTradeGetter.getListValues(self.symbol, self.past_trade_feed)
        base_trade = 1
        negs = [], False
        pos = [], True
        avg_list = [], True
        for trade in range(len(trade_list)):
            diff = trade_list[trade] - trade_list[base_trade]
            base_trade += 1
            if diff <= 0:
                negs[0].append(abs(diff))
            else:
                pos[0].append(abs(diff))
        if len(pos) > len(negs):
            avg_list = pos
        else:
            avg_list = negs
        if avg_list[1]:
            self.correction_rate = int(mean(avg_list[0]))
        else:
            self.correction_rate = -(int(mean(avg_list[0])))

        return self.correction_rate

    def fair_price_finder(self):

        trade_list = (FixedTradeGetter.getListValues(symbol, self.past_trade_feed))
        last_trade = trade_list[(len(FixedTradeGetter.getListValues(self.symbol, self.past_trade_feed))) - 1]

        self.fair_price_est = last_trade + self.correction_rate
        return self.fair_price_est

    def position_range(self, fair_price_est):
        upper = fair_price_est + self.flux_range
        lower = fair_price_est - self.flux_range

        self.position = [lower, upper]
        return self.position

    def make_trades(self):
        while self.correction_rate_finder() > self.flux_range:
            Positions = Trader.position_range(self.fair_price_finder())  # if volatile  new positions
        # if within range make trades
        sell = Positions[1]+1
        buy = Positions[0]-1
        return sell, buy


def main(flux_range, past_trade_feed, symbol, correction_rate):
    trader = Trader(flux_range, past_trade_feed, symbol, correction_rate)
    sell_position = trader.make_trades()[0]
    buy_position = trader.make_trades()[1]
    return sell_position, buy_position


if __name__ == "__main__":
    main()



