from Modules.Module_Basic import *
from config.config import config

def Instgram_Upload():
    # try:
        img_path = Lunch_Img()
        cl = Client()
        cl.login(config('Instagram_ID'), config('Instagram_PW')) # 별그램 아이디, 패스워드 

        try:
            print('Log | Uploading. . .')
            media = cl.photo_upload(
                img_path,
                f"{datetime.datetime.now().strftime('%Y. %m. %d')} 급식 \n#대진전자통신고등학교 #오늘의급식 #오급",
                extra_data={
                    "custom_accessibility_caption": "",
                    "like_and_view_counts_disabled": 1,
                    "disable_comments": 1,
                }
            )
            print('Log | Upload True \n', media.caption_text)
        except Exception as e:
            print("Error |", e)
    # except Exception as e:
    #     print(e)
        # main()