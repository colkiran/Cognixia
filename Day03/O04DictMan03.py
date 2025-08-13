
print("items".center(60, "-"))
# items is a combination of keys and values

emp = {
    'emp1': {'empid': 'EMP111', 'ename': 'Jack', 'gender': 'male', 'dob': '13/04/1997', 'desig': 'MGR', 'salary': 145000},
    'emp2': {'empid': 'EMP202', 'ename': 'Tina', 'gender': 'female', 'dob': '13/04/2002', 'desig': 'TL',  'salary': 85000},
    'emp3': {'empid': 'EMP330', 'ename': 'Mike', 'gender': 'male', 'dob': '13/04/1993', 'desig': 'GM', 'salary': 165000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

