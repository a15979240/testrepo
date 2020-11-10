import pymysql
from T0923178_p import SSq1
import time



class PoJie():
    def __init__(self,path):
        self.file=open(path,"r",errors="ignore",encoding="utf-8")
    def readP(self):
        print("start 導入")
        l=self.file.readline()
        while l:
            l=self.file.readline()
            sq1='insert into animeyearmonth values(0,"'+x+'","'+l+'",'+'"N"'+',"NA")'
            self.sqlinp(sq1)
            # print(l)
        self.file.close()
        
    def sqlinp(self,sqx):
        db=pymysql.connect("127.0.0.1","root","admin","animeym")
        # 創建一個cursor
        cursor=db.cursor()
        print(sqx)
        # 插入值
        # sq1='insert into bandcard values(0,'+x+','+x+','+fs+','+',00,'+',NA)'
        try:
            cursor.execute(sqx)
            # db.commit()
            db.commit()
        except:
        # 若失敗，則回滾
            db.rollback()

        data=cursor.fetchone()
        print("DV: %s" %data)
# 段開
        cursor.close()
        db.close()
        #     res=cursor.fetchall()
        #     return res
        # except:
        # # 若失敗，則回滾
        #     print("error")
        #     db.rollback()
            
        # data=cursor.fetchone()
        # print("DV: %s" %data)
        # cursor.close()
        # db.commit()
        # db.close()
def searchP(x,y):
    db=pymysql.connect("127.0.0.1","root","admin","animeym")
    # 創建一個cursor
    cursor=db.cursor()
        
    # 插入值
    sq1="select * from animeyearmonth where "+x+" like '"+y+"%'"
    print(sq1)
    try:
        cursor.execute(sq1)
        reslist=cursor.fetchall()
        
        for row in reslist:
            print("%s//%s//%s//"%(row[0],row[1],row[2]))
    except:
    # 若失敗，則回滾
        db.rollback()

    data=cursor.fetchone()
    print("DV: %s" %data)
# 段開
    cursor.close()
    db.close()


inpu=str(input("輸入操作(EX:input、search):"))
if inpu == 'input':
    x=str(input("輸入檔名(EX:201901):"))
    path=r'Z:\\我的雲端硬碟\\python\\'+x+'.txt'
    s=PoJie(path)
    s.readP()
elif inpu == 'search':
    x=str(input("輸入搜尋要件1(EX:id、name etc.):"))
    y=str(input("輸入搜尋要件2(EX:對應內容等 etc.):"))

    searchP(x,y)
# res=s.get_all('select * from bandcard where money>500')
# for row in res:
#     print("%d--%d"%(row[0],row[1]))