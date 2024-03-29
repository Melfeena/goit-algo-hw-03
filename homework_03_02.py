import random

def get_numbers_ticket(min, max, quantity):
    for num in [min, max, quantity]:
        if not (1 <= num <= 1000):
            return []
        unique_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(unique_numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа", lottery_numbers)