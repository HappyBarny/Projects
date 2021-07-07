# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:15:29 2021

@author: paolo
"""

stringa = '<a href="https://www.newegg.com/msi-geforce-gtx-1660-super-gtx-1660-super-gaming-x/p/N82E16814137476?Description=graphic%20card&amp;cm_re=graphic_card-_-14-137-476-_-Product&amp;quicklink=true" class="item-img"><img src="https://c1.neweggimages.com/ProductImageCompressAll300/14-137-476-V01.jpg" title="MSI GeForce GTX 1660 SUPER DirectX 12 GTX 1660 SUPER GAMING X 6GB 192-Bit GDDR6 PCI Express 3.0 x16 HDCP Ready Video Card" alt="MSI GeForce GTX 1660 SUPER DirectX 12 GTX 1660 SUPER GAMING X 6GB 192-Bit GDDR6 PCI Express 3.0 x16 HDCP Ready Video Card" class="checkedimg"></a>'
print(len(stringa))

for i in range(0, len(stringa), 1):
    new_word = stringa[:i]
    if stringa[i:i+1] == '?':
        print('found: ' + stringa[i:i+1])
        break

new_word = (new_word+'?')
position = 0

for i in range(0, len(new_word), 1):
    if new_word[:i] == '<a href="':
        print("yes")
        link = ""
        position = i
    link = new_word[position:]
print(link)

stringa = '<a class="item-img combo-img-0" href="https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4190581"><img alt="GIGABYTE GeForce RTX 3070 DirectX 12 GV-N3070GAMING OC-8GD 8GB 256-Bit GDDR6 PCI Express 4.0 x16 ATX Video Card + GIGABYTE GP-P750GM 750W ATX 12V v2.31 80 PLUS GOLD Certified Full Modular Active PFC Power Supply" class="" src="https://c1.neweggimages.com/ProductImageCompressAll300/combo4190581.jpg" title="GIGABYTE GeForce RTX 3070 DirectX 12 GV-N3070GAMING OC-8GD 8GB 256-Bit GDDR6 PCI Express 4.0 x16 ATX Video Card + GIGABYTE GP-P750GM 750W ATX 12V v2.31 80 PLUS GOLD Certified Full Modular Active PFC Power Supply"/></a>'

    
print(link)


