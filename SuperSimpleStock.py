import os
import csv
import BaseStock as bs



Trading_stocks = bs.BaseStock()
Trading_stocks.AddStock("TEA", "Common",    "0",  "", "100")
Trading_stocks.AddStock("POP", "Common",    "8",  "", "100")
Trading_stocks.AddStock("ALE", "Common",   "23",  "",  "60")
Trading_stocks.AddStock("GIN", "Preferred", "8", "2", "100")
Trading_stocks.AddStock("JOE", "Common",   "13",  "", "250")


print("Global Bevarage Corporation Exchange Sample data")
print(Trading_stocks)


while True:
    print( "Choose from the following actions" )
    print( "      load" )
    print( "    record" )
    print( " calculate" )
    print( "      exit" )
    print("")

    action = input("Select an action: ")

    if ( action == "exit" ):
        print( "Exiting program" )
        break

    if ( action == "load"):
        symbol    = input( "Enter Stock symbol: " )
        type      = input( "Enter stock type: " )
        last_div  = input( "Enter Stock last dividend: " )
        if  ( type == "Common"):
            while ( last_div == "" ):
                last_div = input( "Re-enter stock last dividend: " )
        fixed_div = input( "Enter Stock fixed dividend: " )
        if  ( type == "Preferred"):
            while ( fixed_div == "" ):
                fixed_div = input( "Re-enter stock fixed dividend: " )

        par_value = ""
        while( par_value == "" ):
            par_value = input( "Enter Stock par value: " )

        Trading_stocks.AddStock(symbol,type,last_div,fixed_div,par_value)

        print("")
        print("Global Bevarage Corporation Exchange Sample data")
        print(Trading_stocks)
    
    elif ( action == "record" ):
        symbol   = input( "Enter Stock symbol: ")
        quantity = input( "Enter quantity of shares: ")
        BuySell  = input( "Are the share buy or sell: ")
        price    = input( "What is the trade price: ")
        Trading_stocks.recordtrade.AddTrade(symbol,quantity,BuySell,price)
    elif (action == "calculate" ):
        option = ""
        while ( option == ""):
            option = input( "What would you like to calculate (Yield, PEratio, VolWeight, GBCE):")
            if ( option == "Yield" ):
                symbol = input( "Enter Stock symbol: " )
                price = input( "Enter market price: " )
                print("")
                print( "Dividend yield -> %f" % Trading_stocks.dividend_yield(symbol,price) )
                print("")
            elif ( option == "PEratio" ):
                symbol = input( "Enter Stock symbol: " )
                price = input( "Enter market price: " )
                print("")
                print( "P/E ratio -> %f" % Trading_stocks.PE_ratio(symbol,price) )
                print("")
            elif ( option == "VolWeight" ):
                symbol = input( "Enter Stock symbol: " )
                print("")
                print("Volume Weight Stock price -> %f " %  Trading_stocks.volume_weighted(symbol) )
                print("")
            elif ( option == "GBCE" ):
                print( "GBCE all share index -> %f " % Trading_stocks.gbce_all_share_index() )
                print("")
