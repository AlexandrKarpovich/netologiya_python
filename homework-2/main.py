def match_pairs(boys, girls):
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары.")
        return

    boys.sort()
    girls.sort()

    print("Идеальные пары:")
    for boy, girl in zip(boys, girls):
        print(f"{boy} и {girl}")




def main():
    # Пример 1
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    match_pairs(boys, girls)

    # Пример 2
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    match_pairs(boys, girls)


if __name__ == "__main__":
    main()