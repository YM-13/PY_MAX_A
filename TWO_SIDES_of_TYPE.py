Car = type(
    "Car",
    (object,),
    {
        "model": "Тойота",
        "color": "Розовый",
        "number": "П111УУ77"
    }
)



a = Car()

type(a) == Car
print(type(a))
print(Car.__dict__['color'])