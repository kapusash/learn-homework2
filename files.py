"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(f'Длина строки: {len(content)}')
        print(f'Количество слов: {len(content.split())}')
        new_referat = content.replace('.','!')
        with open('referat2.txt', 'w', encoding='utf-8') as f:
            f.write(new_referat)
if __name__ == "__main__":
    main()
