class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        points = 0  # Изначально количество очков равно нулю

        if place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return None
        elif place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return None
        else:
            points = 101 - place
            return points


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        """
        Рассчитывает очки в зависимости от расстояния броска.
        :param meters: целое число — расстояние в метрах
        :return: количество очков или None в случае ошибки
        """
        points = 0  # Изначально количество очков равно нулю

        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return None
        else:
            points = meters * 0.5
            return points



class TotalPoints(PointsForPlace, PointsForMeters):
    @staticmethod
    def get_total_points(meters, place):
        """
        Суммирует очки за место и за расстояние.
        :param meters: целое число — расстояние в метрах
        :param place: целое число — место, занятое спортсменом
        :return: общее количество очков
        """
        # Получаем очки за место
        points_place = PointsForPlace.get_points_for_place(place)
        if points_place is None:  # Если была ошибка при расчёте очков за место
            return None

        # Получаем очки за расстояние
        points_meters = PointsForMeters.get_points_for_meters(meters)
        if points_meters is None:  # Если была ошибка при расчёте очков за расстояние
            return None

        total = points_place + points_meters
        return total
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 
