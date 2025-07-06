def total_salary(path):
    try:
        total = 0
        count =0
        with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    try:
                        name ,salary = line.strip().split(",")
                        count +=1
                        salary = int(salary)
                        total = total+salary
                    except ValueError:
                         print("Помилка")
        
        average = total / count
        return total,average
    except FileNotFoundError:
        return f"Файл за шляхом '{path}' не знайдено!"
        
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
#я не розумію чому тут необроблються помилки я вже чата питав а він якусь дуристику пише  