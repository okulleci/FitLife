
print("Добро пожаловать! Я ваш бот FitLife.")
print("Я помогу вам рассчитать индекс массы тела и норму воды.")

user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))

user_weight = float(input("Укажите ваш вес (в кг, например, 75.5): "))
user_height = float(input("Укажите ваш рост (в метрах, например, 1.75): "))

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

water_ml = user_weight * 30
water_l = water_ml / 1000

print(f"Отчет для пользователя: {user_name} ({user_age} лет)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("Расчет окончен. Будьте здоровы!")
