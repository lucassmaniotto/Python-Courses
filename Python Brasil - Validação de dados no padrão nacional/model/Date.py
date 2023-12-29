from datetime import datetime

class Date:
    def __init__(self):
        self.register_moment = datetime.today()

    def __str__(self):
        return self.format_date()

    def month(self):
        months = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]

        month = self.register_moment.month - 1
        return months[month]

    def day(self):
        day_list = [
            "Segunda-feira", "Terça-feira",
            "Quarta-feira", "Quinta-feira", "Sexta-feira",
            "Sábado", "Domingo"
        ]

        day = self.register_moment.weekday()
        return day_list[day]
    
    def format_date(self):
        return self.register_moment.strftime("%d/%m/%Y %H:%M")
    