from Modules.Module_Basic import *

def main():
    try:
        schedule.every().day.at("13:45").do(Instgram_Upload)
    except Exception as e:
        print(e)

    while True:
        schedule.run_pending()
        time.sleep(1)

asyncio.run(main())

########

# Instgram_Upload