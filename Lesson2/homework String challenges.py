from collections import counter

#1. Вывести последнюю букву в слове
word = 'Архангельск'
all_letters = len(word)-1 
last_letter = word[all_letters:] 
#print (last_letter)


#2. Вывести количество букв "а" в слове
word = 'Архангельск'

i = 0
finding_letter = 'A'
while i < len(word):
        if string[i] == finding_letter:
            return i
        i = i + 1

print (i) 

#3. Вывести количество гласных букв в слове
word = 'Архангельск'
# ???


#4. Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
#print (len(sentence))


#5. Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# 


#6. Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???