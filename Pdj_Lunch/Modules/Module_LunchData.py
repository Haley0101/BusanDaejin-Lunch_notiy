from Modules.Module_Basic import *
from config.config import config

def ToDay_Info():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    datetime_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    dateDict = {0: '월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
    result = dateDict[datetime_date.weekday()]
    return result

def ToDay_Lunch():
    try:
        _ToDay = ToDay_Info()
        if _ToDay == '토요일' or _ToDay == '일요일':
            print("info |", _ToDay)
            return f"오늘은 {_ToDay}입니다! \n즐거운 주말 보내시기 바랍니다!"
        else:
            ToDay = datetime.datetime.now().strftime("%Y%m%d")
            response = requests.get(f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={config('API_KEY')}&Type=json&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=C10&SD_SCHUL_CODE=7150597&MLSV_YMD={ToDay}")
            _result_data = response.json()

            meal = _result_data["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
            meal = meal.replace("<br/>", "\n")  # 줄바꿈으로 만든 뒤 출력
            meal = re.sub(r"\s+", " ", meal)
            meal = str(meal).replace(' ', '\n')
            return meal
    except KeyError as e:
        print("error |", e)
        return "단축수업 또는 학사일정이 없습니다. \n오늘의 학사일정을 참고 해주시기 바랍니다!"

def Lunch_Img():
    img = Image.open("./Img/Basic_Img.png")
    fnt = ImageFont.truetype("./Font/ttf/Happiness-Sans-Bold.ttf", 40, encoding="UTF-8")
    
    text = f"""{ToDay_Lunch()}"""
    draw = ImageDraw.Draw(img)
    _, _, w, h = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((1080-w)/2, 400), text, font=fnt, fill="Grey", align='center')
    
    result_img = img.convert("RGB")
    result_img.save("./Img/Result_Img.jpg")
    return "./Img/Result_Img.jpg"