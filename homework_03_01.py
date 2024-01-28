from datetime import datetime
current_date = datetime.today()

while True:
    dateinput = input("Введіть дату в форматі РРРР-ММ-ДД: ")
    try:
        date = datetime.strptime(dateinput, '%Y-%m-%d').date()    
    except ValueError:
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
    else:
        break

def get_days_from_today(date):
    delta = current_date.toordinal() - date.toordinal()
    return (delta)

print(get_days_from_today(date))