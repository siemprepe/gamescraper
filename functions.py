from datetime import date

def getToday():
    today = date.today()
    return today.strftime("%d/%m/%Y")

def titlePresent(title, inputList):
    for i in inputList:
        inputPart = i.split(";")
        if checkTitle([title],inputPart[0].split()):
            if (len(inputPart) > 1):
                result = checkExtraParts(title,inputPart)
                if(result):
                    break
            else:
                result=True
                break
        else:
            result = False
    return result

def checkTitle(title, words): 
    res = [] 
    for substring in title: 
        k = [ w for w in words if w in substring.upper() ] 
        if (len(k) == len(words) ): 
            res.append(substring) 
    return res != []

def checkExtraParts(title,inputPart):
    if (len(inputPart) > 1):
        retVal = False
        for x in range(1, len(inputPart)):
            if (inputPart[x] is not None and "NOT" in inputPart[x].upper()):
                if (inputPart[x][3:].upper() not in title.upper()):
                    retVal = True
                else:
                    retVal = False
                    break
        return retVal
    else:
        return False

def buildHTML(results):
    template = """\
    <html>
    <body>
    <table width="100%">
        <thead>
            <tr>
                <td><b>Titel</b></td>
                <td><b>Prijs</b></td>
                <td><b>Shop</b></td>
                <td><b>Link</b></td>
            </tr>
        </thead>
        <tbody>
           {0}
        </tbody>
    </table>
    </body>
    </html>
    """

    itemTemplate = """\
        <tr>
			<td><h3>{0}</h3></td>
			<td>{1}</td>
            <td>{3}</td>
			<td><a href="{2}">Link</a></td>
		</tr>
        """
    content = ""
    for item in results:
        content = content + itemTemplate.format(item.title,item.price,item.url,item.shop)
    
    return template.format(content)