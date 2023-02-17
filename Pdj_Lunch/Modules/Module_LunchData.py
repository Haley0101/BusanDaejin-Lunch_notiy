from Modules.Module_Basic import *
from config import config

def Lunch_Info():
    neis = Neispy.sync(KEY=config('API_KEY'))
    now = datetime.datetime.now().strftime("%Y%m%d")
    
    scmeal = neis.mealServiceDietInfo(config('School_AE'), config('School_SE'), MLSV_YMD=str(now))
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든 뒤 출력
    meal = re.sub(r"\s+", " ", meal)
    meal = str(meal).replace(' ', '\n')
    return meal

def Lunch_Img():
    img = Image.open("./Img/Basic_Img.png")
    fnt = ImageFont.truetype("./Font/ttf/Happiness-Sans-Bold.ttf", 40, encoding="UTF-8")
    
    text = f"""{Lunch_Info()}"""
    draw = ImageDraw.Draw(img)
    _, _, w, h = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((1080-w)/2, 400), text, font=fnt, fill="Grey", align='center')
    
    result_img = img.convert("RGB")
    result_img.save("./Img/Result_Img.jpg")
    return "./Img/Result_Img.jpg"