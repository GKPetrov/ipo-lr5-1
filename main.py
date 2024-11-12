a =str(input("Введите cтроку ")) #Ввод строки
gl=('у','е','ы','а','о','э','я','и','ю','У','Е','Ы','А','О','Э','Я','И','Ю') #список гласных
gl_count=0 #инициализация переменных
space_count=0
for i in range(len(a)): #перебор строки
    for b in range(len(gl)):
        if(gl[b]==a[i]):
            gl_count+=1
            b+=1
        elif(a[i]==''):
            space_count+=1
          

    
sogl_count=len(a)-gl_count-space_count #подсчет числа согласных 
print(f"длина строки {len(a)}") #вывод
print(f"количество гласных {gl_count}")
print(f"количество согласных {sogl_count}")

        


