from abc import ABC,abstractmethod

class stock:
    def __init__(self,iphone_stock,samsung_stock,iqoo_stock,vivo_stock):
        self.iphone_stock=iphone_stock
        self.samsung_stock=samsung_stock
        self.iqoo_stock=iqoo_stock
        self.vivo_stock=vivo_stock
class alert(ABC):
    @abstractmethod
    def display_message():
        pass
class iphone(alert):
    def display_message(self,uname,email,phtype):
        if iphone_stock>0:
            print(f'stock is available,{self.uname} can buy from your {self.phtype}')
            return True
        else:
             print(f'stock is not  available,{self.uname} Kindly wait for some time')
             return False
class samsung(alert):
    def display_message(self,uname,email,phtype):
        if samsung_stock>0:
            print(f'stock is available,{self.uname} can buy from your {self.phtype}')
            return True
        else:
             print(f'stock is not  available,{self.uname} Kindly wait for some time')
             return False
class iqoo(alert):
    def display_message(self,uname,email,phtype):
        if iqoo_stock>0:
            print(f'stock is available,{self.uname} can buy from your {self.phtype}')
            return True
        else:
             print(f'stock is not  available,{self.uname} Kindly wait for some time')
             return False
class vivo(alert):
    def display_message(self,uname,email,phtype):
        if vivo_stock>0:
            print(f'stock is available,{self.uname} can buy from your {self.phtype}')
            return True
        else:
             print(f'stock is not  available,{self.uname} Kindly wait for some time')
             return False

class user:
    def __init__(self,uname,email,phtype):
        self.uname=uname
        self.email=email
        self.phtype=phtype
        self.notified=False
def update_stock(st):

    st.iphone_stock=st.iphone_stock+ int(input("Enter the new stock:"))
    st.iqoo_stock=st.iqoo_stock+int(input("Enter the new stock:"))
    st.samsung_stock_stock=st.samsung_stock_stock+int(input("Enter the new stock:"))
    st.vivo_stock=st.st.vivo_stock+int(input("Enter the new stock:"))
def check_stock_availability(l,st):
    l1=[]
    for i in l:
        if i.phtype == "iphone":
            if iphone.display_message(i.uname,i.email,i.phtype):
                st.iphone_stock-=1
            else:
                l1.append(i)
        if i.phtype == "samsung":
            if samsung.display_message(i.uname,i.email,i.phtype):
               st.samsung_stock-=1
            else:
                l1.append(i)
        if i.phtype == "iqoo":
            if iqoo.display_message(i.uname,i.email,i.phtype):
                   st.iqoo_stock-=1
            else:
                l1.append(i)

        if i.phtype == "vivo":
            if vivo.display_message(i.uname,i.email,i.phtype):
               st.vivo_stock-=1
            else:
                l1.append(i)
    return l1


if __name__== "__main__":
    st=stock(0,0,0,0)
    l=[]
    while True:
        person =input("Enter if you are admin or user: ")
        if person=="admin":
            update_stock(st)
        else:
            name=input()
            email=input()
            phtype=input()
            if int(input("Enter 1 to click notify me button: "))==1:
                l.append(user(name,email,phtype))
            l=check_stock_availability(l,st)
        if int(input("Enter 1 to exit:"))==1:
            break

            
