# TODO Найдите количество книг, которое можно разместить на дискете

symv= 4
chars= 25
string_= 50
page = 100
book=symv*chars*string_*page
book=book/(1024*1024)
books=1.44//book
print("Количество книг, помещающихся на дискету:", int(books))
