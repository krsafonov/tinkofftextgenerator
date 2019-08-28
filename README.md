# tinkofftextgenerator

##gtmodel.py
gtmodel.py отвечает за биграммнную языковую модель. В файле есть 2 класса: word и gentext. 
Объект класса word - это слово (name) и слова, которые в текстах стоят после name (deps). Count считает, сколько раз в тексте слово name. Каждому слову в deps соответсвует значение, сколько раз оно встечается после name. Метод random случайно выбирает слово из deps, учитывая вес слова.
Объект класса gentext и есть сама модель. В data каждому слову из текстов соответствует объект word с таким же name. Allwordsquantity - количество слов в моделе, учитывая повторения. 
Метод learn читает файл, делит его на слова и вызывает метод add_pair.
Метод get_random_word выбирает случайное первое слово для генерации, учитывая вес слова.

##learn.py
learn.py инициализирует модель и принимает на вход файл для анализа. Команда из консоли: python3 learn.py file_name

##generator.py
generator.py генерирует текст введеной длины. Команда из консоли: python3 generator.py length


