def is_lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if len(ticket_str) != 6 or not ticket_str.isdigit():
        return 'Некорректный номер билета. Введите шестизначное число.'
    first_half_sum = sum(int(digit) for digit in ticket_str[:3])
    second_half_sum = sum(int(digit) for digit in ticket_str[3:])
    if first_half_sum == second_half_sum:
        return 'Счастливый билет'
    else:
        return 'Несчастливый билет'

def main():
    while True:
        ticket_input = input('Введите номер проездного билета (или напишите "exit" для завершения):')
        if ticket_input.lower() == 'exit':
            print('Bye.')
            break
        result = is_lucky_ticket(ticket_input)
        print(result)

if __name__ == "__main__":
    main()