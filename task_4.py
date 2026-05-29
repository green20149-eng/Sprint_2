class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is not None:
            return self.hours
        elif self.rest_days is not None:
            self.hours = (7 - self.rest_days) * 8
            return self.hours
        else:
            raise ValueError("Недостаточно данных для расчёта часов: не заданы ни hours, ни rest_days")

    def get_email(self):
        if self.email is not None:
            return self.email
        else:
            self.email = f"{self.name}@email.com"
            return self.email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        hours = self.get_hours()  # Получаем количество часов (рассчитанное или заданное)
        return hours * self.hourly_payment
    
    # Пример с сотрудников
employee1 = EmployeeSalary(name="Сергей", rest_days=11)

# Получаем рассчитанные часы
print(f"Отработанные часы: {employee1.get_hours()} ч.")  # (7 - 2) * 8 = 40 ч.

# Получаем сгенерированный email
print(f"Email: {employee1.get_email()}")  # Иван@email.com

# Рассчитываем зарплату
print(f"Зарплата: {employee1.salary()} руб.")  # 40 * 400 = 16 000 руб.

# Меняем почасовую оплату для всех сотрудников
EmployeeSalary.set_hourly_payment(500)

# Пересчитываем зарплату с новой ставкой
print(f"Новая зарплата: {employee1.salary()} руб.")  # 40 * 500 = 20 000 руб.
