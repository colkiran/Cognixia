
print("Arithmetic Operator".center(60, "-"))
a = 10
b = 3
print(f"Add :{a} + {b} = {a + b}")
print(f"Sub :{a} - {b} = {a - b}")
print(f"Mul :{a} * {b} = {a * b}")
print(f"Div :{a} / {b} = {a / b}")
print(f"FlrDiv :{a} // {b} = {a // b}")
print(f"Mod :{a} % {b} = {a % b}")
print(f"Power :{a} ** {3} = {a ** 3}")

print('Augmentor'.center(60, "-"))
# =, +=, -=, *=, /=
a = 5
print(f"a :{a}")

a *= 3
print(f"a :{a}")

a /= 5
print(f"a :{a}")

print("Comparison".center(60, "-"))
# ==, >, >=, <, <=, !=
print(f"1 == 1 :{1 == 1}")
print(f"2 == 1 :{2 == 1}")
print(f"2 >= 1 :{2 >= 1}")
print(f"1 != 2 :{1 != 2}")

print("Logical Operators".center(60, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 2 and 2 == 2 :{1 == 2 and 2 == 2}")

print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print(f"2 == 1 or 1 == 2 :{2 == 1 or 1 == 2}")

print(f"not(1 == 1 and 2 == 2) :{not(1 == 1 and 2 == 2)}")
print(f"not(2 == 1 or 1 == 2) :{ not(2 == 1 or 1 == 2)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")      # integer representation of unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("-" * 60)
print(f"chr(97) :{chr(97)}")
print(f"chr(122) :{chr(122)}")
print(f"chr(65) :{chr(65)}")
print(f"chr(90) :{chr(90)}")
