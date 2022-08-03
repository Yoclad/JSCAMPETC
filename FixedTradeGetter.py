#Creates empty list
mslist, bondlist, gslist, valbzlist, valelist, wfclist = [], [], [], [], [], []

	#Returns the first "number" values from "list"
        def getListValues(list, number):
			if len(list) < number: 
				return list
            returnList=[]
            for x in range(0, number):
              returnList.add(list[len(list)-x])
                
            return returnList

        #Add to the list of print statements, these will create a list containing the last 5 trades for a given symbol
        elif message["type"] == "trade": 
            print(message)
            
            #Creates list
            if (message["symbol"]) == "MS": 
                mslist.append(message["price"])

            if (message["symbol"]) == "BOND": 
                bondlist.append(message["price"])
                
            if (message["symbol"]) == "GS": 
                gslist.append(message["price"])

            if (message["symbol"]) == "VALBZ": 
                valbzlist.append(message["price"])
            
            if (message["symbol"]) == "VALE": 
                valelist.append(message["price"])
               
            if (message["symbol"]) == "WFC": 
                wfclist.append(message["price"])
                
