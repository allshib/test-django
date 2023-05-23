

rekyellow = "Возможно наличие заболевания!\nРекомендуется немедленная консультация кардиолога."
rekgreen = "Наличие сердечно-сосудистого заболевания маловероятно."
rekred = "Высокая степень риска!\nРекомендации:\nПостельный режим.\nОбезболивание: Нитроглицерин под язык, таблетка аспирина, анальгетики внутримышечно или внутривенно.\nНемедленный вызов специализированной бригады скорой медицинской помощи, эвакуация больного в ближайшее отделение, имеющее силы и средства для оказания специализированной помощи."



class Reccom:
    def __init__(self, changes, ready, better, countOfChanges):
        self.changes = changes
        self.ready = ready
        self.better = better / len(ready)
        self.countOfChanges = countOfChanges


class CardioParam:
    def __init__(self, param, better, text):
        self.param = param
        self.better = better
        self.outStr = ""

        if better:
            self.outStr = "снизилась бы на " + str(param) + "%"
        else:
            self.outStr = "возросла бы на " + str(param) + "%"

        self.text = text + self.outStr


class CardioChangeStatistic:
    def __init__(self, avgParam: CardioParam, arrChanges: list):
        self.avgParam = avgParam
        self.arrChanges = arrChanges
        self.betterArr = []
        self.badArr = []

        for i in arrChanges:
            if i.better:
                self.betterArr.append(i)
            else:
                self.badArr.append(i)

        for i in self.betterArr:
            print(i.text)

        # print("better Arr " + str(self.betterArr))
        # print("bad Arr " + str(self.badArr))

        self.betterArr.sort(key=lambda x: x.param, reverse=True)
        self.badArr.sort(key=lambda x: x.param, reverse=True)






def ParseURLParams(params):
    try:
        return [float(num) for num in params.strip('[]').split(',')]
    except:
        return None



def AnalyzeResultsAndGetNotificationForUser(resultArr):
    if resultArr[0] > 75 or resultArr[2] > 75 or resultArr[7] > 75:
        return rekred
    elif resultArr[0] < 50 and resultArr[1] < 50 and resultArr[2] < 50 and resultArr[3] < 50 and resultArr[4] < 50 and resultArr[5] < 50 and \
            resultArr[6] < 50 and resultArr[7] < 50:
        return rekgreen

    return rekyellow




# async def SearchAndPrintChanges(originalResult, newResult):
#     outData = SearchChanges(originalResult, newResult)
#     s = "В среднем вероятность возниконовения болезни " + outData.avgParam.outStr
#
#     betterResult = ""
#     if len(outData.betterArr) > 0:
#         for item in outData.betterArr:
#             if item.param > 0.9:
#                 betterResult += item.text
#
#     badResult = ""
#     if len(outData.badArr) > 0:
#         for item in outData.badArr:
#             if item.param > 0.9:
#                 badResult += item.text
#
#     if s != "":
#         await bot.send_message(message.from_user.id, s)
#     if betterResult != "":
#         await bot.send_message(message.from_user.id, betterResult)
#     if badResult != "":
#         await bot.send_message(message.from_user.id, badResult)


def SearchChanges(originalResult, newResult):
    disease = ["\nВероятность инфаркта миокарда ", "\nВероятность стенокардии стабильной ",
               "\nВероятность стенокардии нестабильной ", "\nВероятность ишемической болезни ",
               "\nВероятность гипертонической болезни ", "\nВероятность аритмии и блокады сердца ",
               "\nВероятность хроническая сердечной недостаточности ",
               "\nВероятность ишемическая сердечной недостаточности "]

    sumOrig = sum(originalResult)
    sumNew = sum(newResult)

    avgProbOrig = sumOrig / len(originalResult)
    avgProbNew = sumNew / len(originalResult)

    print("оригмас: " + str(originalResult) + " Средняя вероятность заболевания: " + str(avgProbOrig))
    print("new: " + str(newResult) + " Средняя вероятность заболевания: " + str(avgProbNew))

    print("\n")

    avg = None
    if sumOrig >= sumNew:
        avg = CardioParam(better=True, param=round(avgProbOrig - avgProbNew, 2),
                          text="Текущая вероятность возникновения болезни равна" + str(
                              avgProbNew) + "\nВ среднем вероятность возниконовения болезни ")
        print("Старое: " + str(avgProbOrig) + "; Новое: " + str(avgProbNew
                                                                ) + " Процент отличия: " + str(
            round(avgProbOrig - avgProbNew, 2)))
    else:
        avg = CardioParam(better=False, param=round(avgProbNew - avgProbOrig, 2),
                          text="Текущая вероятность возникновения болезни равна" + str(
                              avgProbNew) + "\nВ среднем вероятность возниконовения болезни ")
        print("Старое: " + str(avgProbOrig) + "; Новое: " + str(avgProbNew
                                                                ) + " Процент отличия: " + str(
            round(sumNew / 8 - sumOrig / 8, 2)))
    print("\n")
    # CardioParam(better=False, param=round(100 - sumOrig / (sumNew / 100)))
    arrChanges = []

    for i in range(len(originalResult)):
        if originalResult[i] >= newResult[i]:
            arrChanges.append(CardioParam(better=True, param=round(originalResult[i] - newResult[i]), text=disease[i]))
            print("Номер стобца: " + str(i + 1) + "; Старое: " + str(originalResult[i]) + "; Новое: " + str(
                newResult[i]) + " Процент отличия: " + str(round(originalResult[i] - newResult[i])))
        else:
            arrChanges.append(CardioParam(better=False, param=round(newResult[i] - originalResult[i]), text=disease[i]))
            print("Номер стобца: " + str(i + 1) + "; Старое: " + str(originalResult[i]) + "; Новое: " + str(
                newResult[i]) + " Процент отличия: " + str(round(newResult[i] - originalResult[i])))
    return CardioChangeStatistic(avg, arrChanges)