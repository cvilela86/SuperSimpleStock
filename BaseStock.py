import datetime as dt
import RecordTrades as rt

class BaseStock:
    header = ["Stock symbol","Type","Last dividend","Fixed Dividend","Par value"]
    
    def __init__(self):
        """
        Initialize the BaseStock class object.
        No arguments necessary as this will only create an empty dictionary
        which will be use as a placeholder for adding stocks, their values and trades
        """
        self.stock = {}
        self.recordtrade = rt.RecordTrade()
 
    def __str__(self):
        h = '\t'.join("%+6s" % item for item in self.header)
        print(h)
        for st in self.stock.keys():
            line = "\t".join( "%10s" % item for item in [st,self.stock[st]["type"],
                                                       str(self.stock[st]["last_div"]),
                                                       str(self.stock[st]["fixed_div"]),
                                                       str(self.stock[st]["Par_value"])
                                                      ] )
            print(line)
        return ""
    
    def validate(self,symbol):
        if ( symbol in self.stock): return True
        else: return False
    
    def AddStock(self,
                 symbol="Unknown", type="Unknown",
                 last_div=None, fixed_div=None, Par_value=None
                 ):
        """
        Add/Initialize a new stock
        
        args:
        symbol: Stock symbol
        type: type of stock to add
        last_div: last dividend associated with the stock.
        This can have a NULL/None value.
        fixed_div: fixed dividend associated with stock.
        This can have a NULL/None value.
        Par_value: value associated with the stock.
        This cannot be NULL/NONE.
        """
        
        if ( (symbol != "Unknown") and
             (symbol is not None) ):
            self.symbol    = symbol
            self.type      = type
            
            if (not last_div): last_div = None
            try: self.last_div  = last_div if (last_div is None) else float(last_div)
            except ValueError: print( "last dividend value provided is not a number" )
            
            if (not fixed_div): fixed_div = None
            try: self.fixed_div = fixed_div if (fixed_div is None) else float(fixed_div)/100.
            except ValueERROR: print( "fixed dividend value provided is not a number" )
            
            if (not Par_value): Par_value = None
            if ( Par_value is not None): self.Par_value = float(Par_value)
            else:
                print("ERROR: Par value of a stock not given")
                print("       Check that par value was given")
                exit(999)
        
        
            if ( self.symbol in self.stock):
                print( "Stock %s has already been added \n" % self.symbol )
                print( "with the following values:" )
                print( "Type : %s" % self.stock[self.symbol]["type"] )
                print( "last dividend : %s" %
                        ( self.stock[self.symbol]["last_div"] is None and " " or
                          str(self.stock[self.symbol]["last_div"])
                        )
                     )
                print( "Fixed dividend : %s" %
                        ( self.stock[self.symbol]["fixed_div"] is None and " " or
                          str(self.stock[self.symbol]["fixed_div"])
                        )
                     )
                print("Par value : %s" % str(self.stock[self.symbol]["Par_value"]) )
                print("Skipping Stock %s" % self.symbol)
            else:
                self.stock[self.symbol] = {
                    "type"     : self.type,
                    "last_div" : self.last_div,
                    "fixed_div": self.fixed_div,
                    "Par_value": self.Par_value,
                }
        else:
            print("ERROR: No stock was given")
            print("       call AddStock() function as follows")
            print("       object_name.AddStock(<symbol>,<type>,<last_div>,<fixed_div>,<Par_value>)")
            print("       arguments cannot be empty")


    def dividend_yield(self, symbol, price):
        """
        Calculate a stocks dividend yield given a market price
        
        args:
        symbol: Stock symbol
        price: Stock's market price
        """
        
                
        if (symbol is None):
            print("ERROR: the stock you have entered does not exist")
            print("       Dividend yield cannot be calculated")
            print("SUGGESTIONS: ")
            print("     1. check the stock symbol is correct")
            print("     2. or initialize stock by running BaseStock.AddStock(symbol,type,last_div,fixed_div,par_value)")
            exit(999)
        
        
        stock = self.stock[symbol]
        if   ( stock["type"] == "Common"    ):
            div_yield = stock["last_div"] / float(price)
        elif ( stock["type"] == "Preferred" ):
            div_yield = (stock["fixed_div"] * stock["Par_value"]) / float(price)
        else:
            print( "ERROR: unable to calculate dividend yield for Stcok %s" % symbol )
            print( "       Stock symbol %s provided does not have a type" % symbol )
            print( "       Check stock symbol or proivide Stock information")
            exit(999)
        
        return div_yield


    def PE_ratio(self, symbol, price):
        """
        Calculate P/E ratio of a stock given a market price
        
        args:
        symbol: Stock symbol
        price: Stock's market price
        """
        
        if (symbol is None):
            print("ERROR: the stock you have entered does not exist")
            print("       Dividend yield cannot be calculated")
            print("SUGGESTIONS: ")
            print("     1. check the stock symbol is correct")
            print("     2. or initialize stock by running BaseStock.AddStock(symbol,type,last_div,fixed_div,par_value)")
            exit(999)
        
        div_yield = self.dividend_yield(symbol, price)

        return float(price)/div_yield
    
    def volume_weighted(self, symbol, T=15):
        """
        Calculate Volume weighted stock price of a stock in the last T minutes
        
        args:
        symbol: Stock symbol
        T: time range in minutes for which to calculate the stock price
        """
                
        ListofTrades = self.recordtrade.getTrades(symbol,T)
        
        if ( not ListofTrades ):
            if ( symbol not in self.stock ):
                print( "ERROR: there is no record or information on stock %s " % symbol)
                exit(999)
            else:
                print( "WARNING: No trade records were found for stock %s" % symbol )
        
        sum   = 0
        total = 0
        for q,p in ListofTrades:
            sum   += float(p) * float(q)
            total += float(q)

        if ( total == 0 ): return 0
        else: return sum/total

    def gbce_all_share_index(self):
        """
        Calculate the GBCE all share index using a geometric mean
        """

        prod = 1
        p    = 0
        for trade in self.recordtrade:
            p += 1
            prod *= trade["price"]

        if ( p == 0 ): return 0
        else: return float(prod)**(1./float(p))
