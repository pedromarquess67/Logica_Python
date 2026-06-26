def fahrenheit_para_celsius(f):
    """Converte temperatura de Fahrenheit para Celsius"""
    celsius= (f-32)*5/9
    return celsius
temp=90
celsius=fahrenheit_para_celsius(temp)
print(celsius)
temp_f=98.6
resultado= fahrenheit_para_celsius(temp_f)
print(f"{temp_f}°F equivalem a {resultado:.2f}°C")