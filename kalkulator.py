def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak bisa dibagi nol")
    return a / b

if _name_ == "_main_":
    print("2 + 3 =", tambah(2, 3))
