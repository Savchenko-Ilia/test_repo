class Realty:
    def __init__(self, n_rooms, area_m2, price, city):
        self.n_rooms=n_rooms
        self.area_m2=area_m2
        self.price=price
        self.city=city

    def __str__(self):
        return "\nCity: {}, price: {}".format(self.city,self.price)

    #def info():
        
if __name__=='__main__':
    one1=Realty(1,40,50000,'Kiev')

    print(one1)
