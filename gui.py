from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pymysql.cursors
import openpyxl
import csv


def process_item(self, item, spider):
    self.cursor.execute()


wb = openpyxl.load_workbook('table_1.xlsx')
ws = wb.active

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='autoset',
    db='lecture',
    charset='utf8'
)
name_data = []
time_1st_data = []
time_2nd_data = []
place_1st_data = []
place_2nd_data = []
professor_data = []
#############테이블 초기화 부분############################
sql = """truncate class"""
curs = conn.cursor()
curs.execute(sql)
#############액셀 데이터 삽입 부분#########################
for r in ws.rows:
    row_index = r[0].row
    name = r[0].value
    time_1st = r[1].value
    time_2nd = r[2].value
    place_1st = r[3].value
    place_2nd = r[4].value
    professor = r[5].value
    curs = conn.cursor()
    sql = """insert into class(name,time_1st,time_2nd,place_1st,place_2nd,professor) values(%s, %s, %s, %s, %s, %s)"""
    curs.execute(sql, (name, time_1st, time_2nd, place_1st, place_2nd, professor))
    name_data.append(r[0].value)
    time_1st_data.append(r[1].value)
    time_2nd_data.append(r[2].value)
    place_1st_data.append(r[3].value)
    place_2nd_data.append(r[4].value)
    professor_data.append(r[5].value)
    conn.commit()
new_lecture_list = []
admin_password = ""
if os.path.isfile("admin.txt"):
    f = open('admin.txt',mode='rt',encoding='utf-8')
    admin_password = f.read()
    f.close()

else:
    print("관리자 정보가 없습니다. 새로 생성하세요")
    admin_password = input("비밀번호 >> ")
    f = open('admin.txt', mode='wt', encoding='utf-8')
    f.write(admin_password)
    f.close()
    

while True:
    print("사용하실 기능을 선택하세요!")
    print("1. 수강편람")
    print("2. 수강신청 목록 만들기")
    print("3. 수강신청 목록 조회")
    print("4. 수강신청 목록 구글 캘린더 동기화")
    print("5. 관리자 메뉴")
    print("6. 종료")
    func = int(input(">> "))
    if func == 1:
        query = "SELECT  * FROM class"
        curs.execute(query)
        conn.commit()
        datas = curs.fetchall()
        for data in datas:
            print(data)
        print()
    if func == 2:
        print("신청 목록에 넣을 강의 인덱스를 입력하세요")
        index = int(input())
        new_lecture_list.append(name[index], time_1st_data[index],time_2nd_data[index], place_1st_data[index],place_2nd_data[index],professor_data[index]);
        print(new_lecture_list)
    if func == 3:
        print(new_lecture_list)
    if func == 4:
        print()
    if fumc == 5:
        print("관리자 메뉴입니다.")
        print("관리자 비밀번호를 입력하세요")
        password = input(">>")
        if password == password_init:
            print("1. 수강편람 수정")
            print("2. 관리자 비밀번호 변경")
            func_admin = int(input(">> "))

        
        
    if func == 6:
        exit()