# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

template = """
Network:
{0:<9} {1:<9} {2:<9} {3:<9}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{5:<9} {6:<9} {7:<9} {8:<9}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
"""

address = input("Введите IP в формате: 10.1.1.0/24 \n")
ip, mask = address.split("/")

ip_str = ip.split(".")
ip1, ip2, ip3, ip4 = [
    int(ip_str[0]),
    int(ip_str[1]),
    int(ip_str[2]),
    int(ip_str[3]),
]

mask_int = int(mask)
mask_bin = "1" * mask_int + "0" * (32 - mask_int)
mask1, mask2, mask3, mask4 = [
    int(mask_bin[0:8], 2),
    int(mask_bin[8:16], 2),
    int(mask_bin[16:24], 2),
    int(mask_bin[24:32], 2),
]

print(template.format(ip1, ip2, ip3, ip4, mask_int, mask1, mask2, mask3, mask4))
