import json
import requests

urlNew = 'https://www.kardionet.ru/public/process'  # На программу
headers = {
    'Authorization': 'Bearer 2D8565ABDA6DE35ECED6DCD004B1B6B44937A1D6E4F081829796605D6862AEAF',
    'Content-Type': 'application/json'
}


def CreateDiag(num, date, arr):
    diag = json.dumps({
        "stageId": num,  # Тип анкеты
        "birthDay": date,  # Дата рождения
        "data": arr  # Массив параметров диагностики
    })
    return diag


def UseProgramNew(diag):
    response2 = requests.request("POST", urlNew, headers=headers, data=diag)
    print(response2.text)
    if response2.status_code != requests.codes.ok:
        print(response2.status_code)
        return 'Ошибка'
    print('Использую программу')
    return response2.text


def GetStringNumber(item):
    return f"{item}"


def GetResultArr(num, bdate, arr):
    # создание JSON
    diag = CreateDiag(num, bdate, arr)
    # отправка запроса на адрес внешних запросов Kardionet
    # и получение результатов
    mylist = UseProgramNew(diag)
    # приведение результатов к итоговому формату
    mylist = mylist.replace('[', '')
    mylist = mylist.replace(']', '')
    ready = list(map(float, mylist.split(',')))
    if len(ready) == 7:
        temp = max(ready[0], ready[1], ready[2])
        ready.insert(3, temp)
    return ready