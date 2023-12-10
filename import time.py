import time

def generate_random_number(min_val, max_val):
    # Используем текущее время в качестве "зерна" для генерации случайного числа
    seed = int(time.time() * 1000)
    
    # Вычисляем псевдослучайное число на основе зерна
    random_num = (seed % (max_val - min_val + 1)) + min_val
    
    return random_num

# Пример использования
min_value = 1
max_value = 100
random_number = generate_random_number(min_value, max_value)
print(random_number)