expected = {"name": "Jan Kowalski",
        "salary": 8000,
        "age": 30,
        "position": "Mid QA",
        "on_leave": False
        }

for k in expected.keys():
    print(k)

for v in expected.values():
    print(v)

for k, v in expected.items():
    print(k, v)