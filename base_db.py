import sqlite3
import datetime

# db 구축
conn = sqlite3.connect('contacts.db', isolation_level=None) # isolation_level : 트랜젝션 사용 x  -> auto commit
cursor = conn.cursor() # 커서 객체


class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print('Name :', self.name)
        print('phone number : ', self.phone_number)
        print('email : ', self.e_mail)
        print('address : ', self.addr)

        print('='*30)


def input_check(title):  # 입력값이 2자리 아래이면 오류발생
    while True:
        try:
            val = input(title)
            if len(val) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("%s is too short" % title)
    return val


def set_contact():
    name = input_check("name : ")
    phone_number = input_check("phone number : ")
    e_mail = input_check("e mail : ")
    addr = input_check("address : ")

    # for i in contact_list:
    #     if name == i.name:
    #         print("find")
    #         break
    # else:
    sql1 = """insert into contacts(name, phone_number, e_mail, address, regdate)
        values(?, ?, ?, ?, ?)"""

    curtime = datetime.datetime.now().strftime('%Y- %m-%d %H:%M:%S')

    cursor.execute(sql1, (name, phone_number, e_mail, addr, curtime))


def print_contact():
    rows = cursor.execute("SELECT * from contacts").fetchall() # db의 모든 데이터 가져온다
    for row in rows:
        print(row) # 등록된 데이터 튜플로 출력

    if len(rows) < 1:
        print('contact is empty')


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    print("5. 데이터 삭제")
    menu = input("메뉴 선택 : ")
    return int(menu)


def delete_contact(name2):
    sql = "delete form contacts where name = ?"
    cnt = cursor.execute(sql, (name2,)).rowcount
    if cnt > 0:
        print('data delete')
    else:
        print('no data to delete')


def load_contact():
    # db 테이블 생성, 확인
    cursor.execute("""
    create table if not exists contacts
    (
        id integer primary key AUTOINCREMENT,
        name text,
        phone_number text,
        e_mail text,
        address text,
        regdate tet
    )
    """)

def clear_contact():
    sql = "delete form contacts"  # 모든 데이터 삭제
    cursor.execute(sql).rowcount
    print("초기화 완료")

def run():
    while 1:
        menu = print_menu()
        if menu == 1:
            # contact = set_contact(contact_list) # set_contact 에서 입력을 받고 리턴값을 받아 contact 에 저장
            # contact_list.append(contact) # contact 를 리스트에 저장

            set_contact()
        elif menu == 2:
            print_contact()

        elif menu == 3:
            name2 = input('name : ')
            delete_contact(name2)
        elif menu == 4:
            clear_contact()


# if __name__ == "__name__":
run()

