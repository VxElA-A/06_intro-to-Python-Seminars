# Пользователь вводит текст (строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

text = input('Введите текст: ')
text1 = text.upper()
print(text1)
text2 = text1.split()
print(text2)
text3 = set(text2)
print(f'Количество слов в списке: {len(text3)}')

# Альтернативное решение, с отсеиванием знаков препинания:

# st = """She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells."""
# stroka = st.replace(".", " ").replace(",", " ").replace("'", " ").replace(";", " ").lower()
# spisok = st.split()
# mnozestvo = set(spisok)
# print(len(mnozestvo))