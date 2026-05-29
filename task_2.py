class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
#Создаем подкласс комедии
class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'
#Создаем подкласс драмы
class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'

# Создаём объект Комедии и вызываем 
comedy = Comedy()
result_comedy = comedy.add_movie('Большой куш')
print(result_comedy)

# Создаём объект Драма и вызываем 
drama = Drama()
result_drama = drama.add_movie('Оружейный барон')
print(result_drama)
