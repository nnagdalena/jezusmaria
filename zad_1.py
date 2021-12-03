class Property:
    def __init__(self,area:float,rooms:int,price:float,address:str):
        self._area=area
        self._rooms=rooms
        self._price=price
        self._address=address

class House(Property):
    def __init__(self,area:float,rooms:int,price:float,address:str,plot:int):
        super().__init__(area,rooms,price,address)
        self._plot=plot

    def __str__(self)->str:
        return f'Dom {super().__str__()} o powierzchni działki {self._plot} '

class Flat(Property):
    def __init__(self,area:float,rooms:int,price:float,address:str,floor:int):
        super().__init__(area)
        super().__init__(rooms)
        super().__init__(price)
        super().__init__(address)
        self._floor=floor
    def __str__(self)->str:
        return f'Mieszkanie {super().__str__()} na piętrze {self._floor} '

house=House(122.14,4,35000,"Katowice, Katowicka 14",54)
flat=Flat(55.5,2,200000,"Mazancowice Mazan 1",3)

print(house)
print(flat)