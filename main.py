name = input("Adınızı daxil edin: ")
age = int(input("Yaşınızı daxil edin: "))
weight = float(input("Çəkinizi daxil edin (kq): "))
height = float(input("Boyunuzu daxil edin (metr): "))
hourly_salary = float(input("Saatlıq maaşınızı daxil edin: "))
worked_hours = float(input("İşlədiyiniz saat sayını daxil edin: "))

current_year = 2026
birth_year = current_year - age
bmi = weight / (height * height)
total_salary = hourly_salary * worked_hours

print("\n--- NƏTİCƏ ---")
print(f"Ad: {name}")
print(f"Yaş: {age}")
print(f"Doğum ili: {birth_year}")
print(f"BMI: {bmi:.2f}")
print(f"Maaş: {total_salary} AZN")