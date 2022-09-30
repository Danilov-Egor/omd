def menu():
    """Show menu for user"""
    print('\n------------Меню-------------')
    print('1. Вывести департаменты и входящие в них отделы.')
    print('2. Вывести сводный отчет по департаментам.')
    print('3. Сохранить отчет из пункта 2 в csv-файл.')


def valid_user_input():
    """takes an input from user and provides validation"""
    user_input = input('Выберите пункт: ')
    if user_input.isdigit() and int(user_input) in {1, 2, 3}:
        return int(user_input)
    else:
        print('Выберите верную опцию!')
        return valid_user_input()


def read_file():
    """read data from file, returns list[list]"""
    with open('Corp_Summary.csv', 'r', encoding='utf8') as file:
        lines = file.readlines()
        table = list(map(lambda r: r.strip().split(';'), lines))[1:]
    return table


def dep_ierarchy():
    """Department ierarchy with branches, 1 menu option """
    table = read_file()
    departments = {row[1]:[] for row in table}
    for department in departments:
        for row in table:
            if row[1] == department:
                branch = row[2]
                if branch not in departments[department]:
                    departments[department].append(row[2])
    print()
    for dep, br in departments.items():
        print(f'{dep} : {", ".join(br)}')


def dep_info():
    """
    Second option, department information
    return list[list]
    """
    table = read_file()
    # create dict{dep : [численность, [зарплата]]}
    dep_info = {row[1] : [0, list().copy()] for row in table}
    for dep in dep_info:
        for row in table:
            if row[1] == dep:
                # increment number of people
                dep_info[dep][0] += 1

                # append salary
                if row[-1].isdigit():
                    dep_info[dep][1].append(int(row[-1])) 
    # resulting list of lists, where each list corresponds for one dep
    resulting = []
    for dep, info in dep_info.items():
        # [департамент, численность, мин.зп, макс.зп, средняя зп]
        row = [dep, str(info[0]), str(min(info[1])), str(max(info[1])), 
            str(round(sum(info[1])/len(info[1]), 2))]
        
        resulting.append(row)
    return resulting


def show_dep_info():
    """Print department information"""
    table_dep_info = dep_info()
    col_name = ['Департамент', 'Численность', 
        'Мин.зарплата', 'Макс.зарплата', 'Средняя зарплата']
    # print in a format of a table
    print('\n{:<12}  {:>12}  {:>12}  {:>12}  {:>12}'.format(*col_name))
    for dep in table_dep_info:
        print('{:<12}  {:>12}  {:>12}  {:>12}  {:>12}'.format(*dep))


def write_to_file():
    """write department information to csv file"""
    table_dep_info = dep_info()
    col_name = ['Департамент', 'Численность', 
        'Мин.зарплата', 'Макс.зарплата', 'Средняя зарплата']
    with open('Department_data.csv', 'w', encoding='utf8') as file:
        file.write(",".join(col_name) + '\n')
        for row in table_dep_info:
            file.write(",".join(row) + '\n')
    print('\nСохранено!')


def main():
    """main function with all logic """
    menu()
    user_input = valid_user_input()

    if user_input == 1:
        dep_ierarchy()
        return main()
    elif user_input == 2:
        show_dep_info()
        return main()
    elif user_input == 3:
        write_to_file()
        return main()
    else:
        print('\nНеверный ввод!')
        return main()


if __name__ == '__main__':
    main()
