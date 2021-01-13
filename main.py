try:
    import requests
    import time
    from os import system

    system("title " + "Soud Was Here - @_agf - Soud#0737")

except Exception as m:
    print(m)
    input("Press Any Key To Exit")


print("""

░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝

                        Credit @_agf - Soud#0737
                        
                        """)
print("")
print("")
print("")
print("This is simple tool by Soud to check school result")

h = int(input("Enter Your Number: "))

a = requests.Session()

co = 0


def checkk():

    global a
    global co

    url = "http://app.moe.edu.kw/Resultcloud/PResults.aspx"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "app.moe.edu.kw",
        "Origin": "http://app.moe.edu.kw",
        "Referer": "http://app.moe.edu.kw/Resultcloud/PResults.aspx",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUKMTQxODQ4OTM2Mw9kFgJmD2QWAgIDD2QWAgIBD2QWAgIBD2QWAmYPZBYCZg9kFgICAQ8PFgIeBFRleHQFVNin2YTYsdis2KfYoSDYp9mE2KrYp9mD2K8g2YXZhiDYpdiv2K7Yp9mEINin2YTYsdmC2YUg2KfZhNmF2K/ZhtmKINio2LTZg9mEINi12K3ZititIGRkZGBGXLrj8pXT5w2Xx3op5V9/NuKX7TijOaC9gnM3YQSV',
        '__VIEWSTATEGENERATOR': 'FE2B3F1E',
        '__EVENTVALIDATION': '/wEdAAOFzIxjRv5KV6X14+YhJHjI/LoBA+N6yzyjsmmTaOURj5+I/HPZ86NEZcbXwR9jxA6vD3mSgpRENQqhkkGpjH0XJxKuhkw4gULSrz5xk71dWQ==',
        'ctl00$MainContent$txtCivilID': h,
        'ctl00$MainContent$btnSearch': 'بحث'
    }

    vv = a.post(url, data=data, headers=headers)
    if vv.text.find("الرجاء التاكد من إدخال الرقم المدني بشكل صحيح") >= 0:
        print("[Wrong Number] Pls Enter Correct One\n")
        input("Press Any Key To Exit...")
    elif vv.text.find("الرجاء التاكد ان المدرسة قامت برفع النتائج") >= 0:
        co += 1
        print(f"[Waiting] Attempt: {co}")
        time.sleep(1.5)
        checkk()
    else:
        print(f"[Found !] Attempt: {co} \n")
        print(f"{vv.text}\n")
        input("Press Any Key To Exit...")


checkk()
