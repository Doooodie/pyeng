# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip = input("IP address: ")
    ip_arr = ip.split(".")
    is_valid = len(ip_arr) == 4

    for address in ip_arr:
        is_valid = address.isdigit() and 0 <= int(address) <= 255 and is_valid

    if not is_valid:
        print("Неправильный IP-адрес")
    else:
        break

if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
elif 1 <= int(ip_arr[0]) <= 223:
    print("unicast")
elif 224 <= int(ip_arr[0]) <= 239:
    print("multicast")
else:
    print("unused")
