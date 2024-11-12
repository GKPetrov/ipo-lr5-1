a =str(input("Введите cтроку "))
gl=('у','е','ы','а','о','э','я','и','ю','У','Е','Ы','А','О','Э','Я','И','Ю')
gl_count=0
space_count=0
for i in range(len(a)):
    for b in range(len(gl)):
        if(gl[b]==a[i]):
            gl_count+=1
            b+=1
        elif(a[i]==''):
            space_count+=1
          

    
sogl_count=len(a)-gl_count-space_count
print(f"длина строки {len(a)}")
print(f"количество гласных {gl_count}")
print(f"количество согласных {sogl_count}")

        


