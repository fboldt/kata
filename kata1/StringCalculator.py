class StringCalculator:
    def __init__(self) -> None:
        super().__init__()
        self.calledCount = 0

    def getCalledCount(self) -> int:
        return self.calledCount
    
    def add(self, numbers: str) -> int:
        self.calledCount += 1
        # set delimiters
        delimiters = [',','\n']
        if numbers.startswith('//'):
            delimiterstr, numbers = numbers.split('\n', 1)
            delimiterlist = delimiterstr[2:].split("][")
            for delimiter in delimiterlist:
                delimiter = delimiter.replace('[','')
                delimiter = delimiter.replace(']','')
                delimiters.append(delimiter)
        # split numbers
        listOfNumbers = [numbers]
        for delimiter in delimiters:
            tmplist = []
            for numlist in listOfNumbers:
                tmplist += numlist.split(delimiter)
            listOfNumbers = tmplist
        # string to int
        result = 0
        negatives = []
        for number in listOfNumbers:
            if number.strip() != "":
                numint = int(number)
                if numint < 0:
                    negatives.append(numint)
                elif numint <= 1000:
                    result += numint
        # raise exception for negative values
        if len(negatives)>0:
            msg = "negatives not allowed:"
            for value in negatives:
                msg += " " + str(value)
            raise Exception(msg)
        return result
