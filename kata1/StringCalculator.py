class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        delimiters = [',','\n']
        if numbers.startswith('//'):
            delimiter, numbers = numbers.split('\n', 1)
            delimiters.append(delimiter[2:])
        
        listOfNumbers = [numbers]
        for delimiter in delimiters:
            tmplist = []
            for numlist in listOfNumbers:
                tmplist += numlist.split(delimiter)
            listOfNumbers = tmplist
        
        result = 0
        for number in listOfNumbers:
            if number.strip() != "":
                numint = int(number)
                if numint >= 0:
                    result += numint
                else:
                    raise Exception("negatives not allowed")
        return result