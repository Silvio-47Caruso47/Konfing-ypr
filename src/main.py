import tkinter as tk
import getpass
import socket

def parse_command(line):
    parts = line.split() #создания массива parts из слов line ( .split() убрал пробелы
    if not parts: # если строка пустая
        return "", [] #веруть пустую строчку и список
    command = parts[0] # первое слово команда
    args = parts[1:] # остальное аргументы
    return command, args #вернуть слово и массив из оставшихся

def run_command(command, args):
    if command == "exit":
        # Команда exit — закрыть окно
        return "Выход.", True

    elif command == "ls": #заглушка ls
        return "ls\n" + " ".join(args), False

    elif command == "cd": #заглушка cd
        return "cd\n" + " ".join(args), False

    else:
        # Неизвестная команда
        return "Ошибка: неизвестная команда '" + command + "'", False

def main():
    user = getpass.getuser() #имя польхователя где getpass библиотека а getuser функция
    host = socket.gethostname() #имя компьютера где socket библиотека а gethostname функция

    root = tk.Tk() #создание окна root
    root.title("Эмулятор - [" + user + "@" + host + "]")  #заголовок окна
    root.geometry("700x500") #размер

    output_1 = tk.Text(root, height=20, width=80) #создание поле вывода высотой 20 строк и широтой 80 символов окна root ( с помощью функции tk.Text() )
    output_1.pack(padx=10, pady=10) #начальное расположение по отношению к изнчальным размерам окна по x и y

    input_1 = tk.Entry(root, width=80) #создание строки ввода длиной 80 символов ( с помощью tk.Entry() )
    input_1.pack(padx=10, pady=5) #начальное расположение по отношению к изнчальным размерам окна по x и y

    output_1.insert(tk.END, "Добро пожаловать!\n")
    output_1.insert(tk.END, "Доступные команды: ls, cd, exit\n")
    output_1.insert(tk.END, "\n")

    def on_run():
        line = input_1.get() #метод который читает содержимое ввода
        input_1.delete(0, tk.END) #очистка где 0 начала а tk.END конец

        if not line.strip(): #если пользователь ничего не ввёл выходим ( strip убирает пробелы в начале и конце ) 
            return

        command, args = parse_command(line) #вызов метода parse_command со строкой line и последующим присвоением результата

        command, args = parse_command(line)
        result, should_exit = run_command(command, args)

        output_1.insert(tk.END, "> " + line + "\n") #начальный вид
        output_1.insert(tk.END, result + "\n\n") #результат
        output_1.see(tk.END) #прокручиваем поле вниз чтобы было видно новые ответы

        if should_exit==True:
            root.destroy() #закрытие окна

    # Кнопка с привязкой к обработчику
    run_1 = tk.Button(root, text="Выполнить", command=on_run)  #создание кнопки с надписью "..." ( с помощью tk.Button() ) + ( command=on_run это вызов функции on_run )
    run_1.pack(pady=5) #начальное расположение по отношению к изнчальным размерам окна по y
    input_1.bind("<Return>", lambda event: on_run()) #Enter в поле ввода делает то же, что кнопка (lambda - одноразовая функция )

    input_1.focus() #палочка в строке ввода

    root.mainloop() #запуск окна


if __name__ == "__main__": #если запущено то дейсвия ниже
    main()
