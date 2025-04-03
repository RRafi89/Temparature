import math

def calculate_weeks(initial_amount, final_amount, growth_rate):
    return math.log(final_amount / initial_amount) / math.log(1 + growth_rate/100)

initial = float(input('Enter your initial amount: '))
target = float(input('Enter the target amount: '))
rate = float(input('Enter increase rate: '))

weeks = calculate_weeks(initial, target, rate)
print(f"It will take approximately {weeks:.1f} weeks.")
