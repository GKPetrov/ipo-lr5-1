string = input("Введите cтроку ") #Ввод строки
glas='уеыаоэяиюУЕЫАОЭЯИЮ' #строка гласных
sogl ='йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ'
glas_count=0 #инициализация переменных
sogl_count=0
space_count=0
for i in string: #перебор строки
    if i in glas:
        glas_count+=1
    elif i in sogl:
        sogl_count+=1
print(f"длина строки {len(string)}") #вывод
print(f"количество гласных {glas_count}")
print(f"количество согласных {sogl_count}")
        


