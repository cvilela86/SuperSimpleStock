import datetime as dt

class RecordTrade:
    def __init__(self):
        self.trades = {}
    
    def AddTrade(self, symbol="Unknown", quantity=None, action=None, price=None):
        """
        Record a trade for a specif stock
        
        args:
            quantity : quantity of share for the trade
            action   : is it a buy or sell trade
            price    : trade price
        """
        
        timestamp = dt.datetime.now()
        
        self.trades[timestamp] = {
                "symbol"  : symbol,
                "quantity": quantity,
                "action"  : action,
                "price"   : price
        }

    def getTrades(self, symbol, T=15):
        """
        get a list of trades for a specific stock in a given time range
        
        args:
        symbol : stock symbol
        T      : time range
        
        returns: list of trade quantity and price within the time range
        """

        delta = dt.datetime.now() - dt.timedelta(minutes=15)

        listTrades = []
        for trade in self.trades.keys():
            if ( self.trades[trade]["symbol"] != symbol): continue
            if ( trade < delta ): break

            listTrades.append(
                              [self.trades[trade]["quantity"],
                               self.trades[trade]["price"] ]
                              )

        return listTrades
