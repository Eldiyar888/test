text = input("Введите текст:")
search = input("Поиск слова:")
word = 0
spl_text = text.split(" ")
search.find(search)
for i in spl_text:
        if i == search:
                word += 1
                
if word > 0:
        print("Слово найдено")
else:
        print("Слово не найдено")

