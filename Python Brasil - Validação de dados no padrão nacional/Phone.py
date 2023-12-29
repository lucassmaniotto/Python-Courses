import re

class Phone:
    def __init__(self, number):
        if self.validate(number):
            self.number = number
        else:
            raise ValueError("Número inválido!")
    
    def validate(self, number):
        pattern = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        match = re.findall(pattern, number)
        if match:
            return True
        return False
    
    def format(self):
        pattern = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        match = re.search(pattern, self.number)
        return f"+{match.group(1)} ({match.group(2)}) {match.group(3)}-{match.group(4)}"
    
    def __str__(self):
        return self.format()