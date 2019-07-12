import pickle
import os


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


def set_contact(contact_list):
    name = input_check("name : ")
    phone_number = input_check("phone number : ")
    e_mail = input_check("e mail : ")
    addr = input_check("address : ")

    for i in contact_list:
        if name == i.name:
            print("find")
            break
    else:
        contact = Contact(name, phone_number, e_mail, addr)
        contact_list.append(contact)


def print_contact(contact_list):
    for i in contact_list:
        i.print_info()


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    print("5. 데이터 삭제")
    menu = input("메뉴 선택 : ")
    return int(menu)


def delete_contact(contact_list, name2):
    if len(contact_list) > 0:
        for i, contact in enumerate(contact_list):
            if (contact.name == name2):
                del contact_list[i]

                with open("temp.bin", 'wb') as f:
                    pickle.dump(contact_list, f)
                    # for i in contact_list:
                    #     f.write(i.name + '\n')
                    #     f.write(i.phone_number + '\n')
                    #     f.write(i.e_mail + '\n')
                    #     f.write(i.addr + '\n')
                break
        else:
            print("no data to delete")
    else:
        print('저장된 파일 X')


def store_contact(contact_list):
    try:
        with open("temp.bin", 'wb') as f:
            pickle.dump(contact_list, f)
            print('데이더 저장완료')
        # for i in contact_list:
        #     f.write(i.name + '\n')
        #     f.write(i.phone_number + '\n')
        #     f.write(i.e_mail + '\n')
        #     f.write(i.addr + '\n')
    except Exception as e:
        print(e)


def load_contact():
    # print(os.path.isfile('temp.txt')) # 파일 존재 여부 확인
    contact_list = []
    if os.path.isfile('temp.bin'):
        try:
            with open('temp.bin', 'rb') as f:
                contact_list = pickle.load(f)
                print('파일 로드 완료')
                # line = f.readlines()
                # num = int(len(line) / 4)
                # for i in range(num):
                #     name = line[i*4].rstrip('\n') # 값 출력
                #     phone_number = line[i * 4+1].rstrip('\n')
                #     e_mail = line[i * 4+2].rstrip('\n')
                #     addr = line[i * 4+3].rstrip('\n')
                    # contact = Contact(name,phone_number, e_mail, addr)
                    # contact_list.append(contact)
        except FileExistsError as err:
            print(err)
    else:
        print('no file')
    return contact_list

def clear_contact():
    # os.unlink("temp.txt")
    if os.path.isfile('temp.bin'):
        try:
            os.unlink('temp.bin')
            print('삭제 완료')

        except Exception as err:
            print(err)
    else:
        print('파일없음')


def run():
    contact_list = load_contact()
    while 1:
        menu = print_menu()
        if menu == 1:
            # contact = set_contact(contact_list) # set_contact 에서 입력을 받고 리턴값을 받아 contact 에 저장
            # contact_list.append(contact) # contact 를 리스트에 저장

            set_contact(contact_list)
        elif menu == 2:
            print_contact(contact_list)

        elif menu == 3:
            name2 = input('name : ')
            delete_contact(contact_list, name2)
        elif menu == 4:
            store_contact(contact_list)
            break
        elif menu == 5:
            clear_contact()


# if __name__ == "__name__":
run()