import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}   
symbol_value = {
    "A": 10,
    "B": 8,
    "C": 6,
    "D": 4
}   

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("Quanto você gostaria de depositar? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Por favor, insira um valor positivo.")
        else:
            print("Por favor, insira um número.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Quantas linhas gostaria de apostar (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Insira um valor de linhas válido.")
        else:
            print("Por favor, insira um número.")

    return lines

def get_bet():
    while True:
        amount = input("Quanto você gostaria de apostar em cada linha? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"A aposta deve ser entre ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Por favor, insira um número.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"Seu saldo é insuficiente. Seu saldo é de ${balance}.")
        else:
            break
 
    print(f"Você está apostando ${bet} em {lines} linhas. Aposta total é de ${total_bet}.")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Você ganhou ${winnings}.")
    print(f"Linhas ganhas:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Seu saldo é de ${balance}")
        answer = input("Pressione enter para jogar ou 'q' para sair: ")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"Seu saldo final é de ${balance}")

main()