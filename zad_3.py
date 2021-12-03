class Property:
    def __init__(self,area:float,rooms:int,price:float,address:str)->None:
        self._area=area
        self._rooms=rooms
        self._price=price
        self._address=address

    @property
    def area(self)->None:
        return self._area

    @area.setter
    def area(self,value:float)->None:
        self._area=value

    @property
    def rooms(self)->None:
        return self._rooms

    @rooms.setter
    def rooms(self,value:int)->None:
        self._rooms=value

    @property
    def price(self)->None:
        return self._price

    @price.setter
    def price(self,value:float)->None:
        self._price=value

    @property
    def address(self)->None:
        return self._address

    @address.setter
    def address(self,value:str)->None:
        self._address=value

    def __str__(self)->str:
        return f"{self._area}, ilość pokoi: {self._rooms}, " \
               f"cena: {self._price}, adres: {self._address}"

class House(Property):
    def __init__(self,area:float,rooms:int,price:float,address:str,plot:int)->None:
        super().__init__(area,rooms,price,address)
        self._plot=plot

    def __str__(self)->str:
        return f"Powierzchnia domu: {super().__str__()}, " \
               f"o powierzchni działki: {self._plot}"

class Flat(Property):
    def __init__(self,area:float,rooms:int,price:float,address:str,floor:int)->None:
        super().__init__(area, rooms, price, address)
        self._floor=floor

    def __str__(self)->str:
        return f"Powierzchnia mieszkania: {super().__str__()}, na piętrze: {self._floor}"

house=House(122.14,4,35000,"Katowice, Katowicka 14",54)
flat=Flat(55.5,2,200000,"Mazancowice Mazan 1",3)

print(house)
print(flat)