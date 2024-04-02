import mysql.connector

class Connection:
    def __init__(self,host,password,database,user):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.Start()
        
    def Start(self):
        self.databs = mysql.connector.connect(
            user = self.user,
            host = self.host,
            password = self.password,
            database = self.database
        )
        self.databsCursor = self.databs.cursor()


class BookCategoryRepsitry:
    def __init__(self):
        self.boglanish = Connection(
            user='root',
            password='shaxriyor',
            database='letcode',
            host='localhost'
        )

# malumotlar shunday tartibda kiritilgan 
#create table Bookcategory (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),price INT NOT NULL)
# yani id o'zi ortib boradi


    def Barcha_kitob_malumotlari(self):
        self.boglanish.databsCursor.execute("SELECT * FROM Bookcategory")
        print(self.boglanish.databsCursor.fetchall())
        print("Barcha kitob malumotlari ekranga chiqarildi! ")


    def Getlist(self,size,page,search):
        query = "SELECT * FROM bookcategory WHERE name like CONCAT ('%',%s,'%') LIMIT %s OFFSET %s"
        self.boglanish.databsCursor.execute(query,(search, size, (size * (page - 1))))
        data = self.boglanish.databsCursor.fetchall()
        print(data)


    def create(self, categoryName,price):
        if not categoryName.isdigit():
            javob = "INSERT INTO bookcategory (name,price) values(%s,%s)"
            self.boglanish.databsCursor.execute(javob,(categoryName,price,))
            self.boglanish.databs.commit()
            print("Muvvafiqatli Yartildi! ")
        else:
            print("Iltimos kitob nomi kiriting: ")


    def delebyCategory(self, id):
        data = "DELETE FROM bookcategory WHERE id = %s"
        self.boglanish.databsCursor.execute(data,(id,))
        deleted = self.boglanish.databsCursor.rowcount
        self.boglanish.databs.commit()
        if deleted > 0:
            print("Muvvafiqatli o'chirildi ! ")
        else:
            print("O'chirish uchun malumot topilmadi yoki ushbu malumot allaqachon o'chirilgan!")


    def GetBYid(self, id):
        data = "SELECT * FROM bookcategory WHERE id = %s"
        self.boglanish.databsCursor.execute(data,(id,))
        kitob = self.boglanish.databsCursor.fetchone()
        if kitob : 
            print(kitob)
        else:
            print("Ushbu kitob ro'yxatda mavjud emas!")


    def umumiy_kitoblarSoni(self):
        data = "SELECT COUNT(id) FROM bookcategory"
        self.boglanish.databsCursor.execute(data)
        soni= self.boglanish.databsCursor.fetchone()
        print("Barcha kitoblar soni {} ta".format(*soni))


    def deleteAllBookInformation(self):
        data = "DELETE FROM Bookcategory WHERE id"
        self.boglanish.databsCursor.execute(data)
        self.boglanish.databs.commit()
        print("Muvvafiqiyatli yo'q qilindi! ")
        


obj = BookCategoryRepsitry()


while True:
    print("""
1. Barcha kitob malumotlarini ko'rish;
2. Kitobni pagenatsiya orqali topish va qidirish;
3. Kitob yaratish Qismi;
4. Kitobni id si bo'yicha o'chirish;
5. Bitta kitobni id si bo'yicha olish;
6. Umumiy kitoblar soni;
7. Barcha kitob malumotlarini o'chirish;
8. Dasturdan chiqish uchun 8 - ni bosing;

""")
    
    choose = input("Tanlag: ")
    try :
        if choose.isdigit():
            choose = int(choose)
            if choose == 1:
                obj.Barcha_kitob_malumotlari()

            if choose == 2:
                page = int(input("Nechta malumot ko'rmoqchisiz: "))
                size = int(input(f"Nechanchi {page} talikni ko'rmoqchisiz: "))
                search = input("Qaysi harf qatnashgan so'zlarni topishni istaysiz: ")
                obj.Getlist(page,size,search)

            if choose == 3:
                name = input("Yaratmoqchi bo'lgan Kitob nomini kiriting: ")
                price = int(input("Kitob narxini kiriting: "))
                obj.create(name,price)

            if choose == 4:
                delete = int(input("O'chirmoqchi bo'lgan kitob id sini kiriting: "))
                obj.delebyCategory(delete)

            if choose == 5:
                get = int(input("Olmoqchi bo'lgan kitob id sini kiriting: "))
                obj.GetBYid(get)

            if choose == 6:
                obj.umumiy_kitoblarSoni()

            if choose == 7:
                obj.deleteAllBookInformation()
            
            if choose == 8:
                break

        else:
            print("Iltimos raqam kiriting: ")
    except Exception as err:
        print(f"Dasturda xatolik yuz bedi {err}")    

print("Dastur tugatildi! ")

