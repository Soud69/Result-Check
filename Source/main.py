try:
    import requests

    import time

    import sys

    from os import system

    from bs4 import BeautifulSoup

    system("title " + "Soud Was Here - @_agf - Soud#0737")

except Exception as m:

    print(m)

    input("Press Any Key To Exit...")


print("""

░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝

                        Credit @_agf - Soud#0737
                        
                        """)
print("This is simple tool by Soud to check school result\n")

sys.setrecursionlimit(10000000)

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
        '__VIEWSTATE': '/wEPDwULLTE5NjY5MDI3OTQPZBYCZg9kFgICAw9kFgICAQ9kFgICAQ9kFgRmD2QWAmYPZBYCAgEPDxYCHgRUZXh0ZWRkAgMPFgIeB1Zpc2libGVnFgJmD2QWAgIBD2QWAmYPZBYCZg9kFg4CAQ8PFgIfAAUw2YXYrdmF2K8g2LnYqNivINin2YTZhNi32YrZgSDYrtmE2YEg2KfZhNi52YbYstmJZGQCAw8PFgIfAAUMMzA4MDUwMzAwMDYxZGQCBQ8PFgIfAAU42YrZiNiz2YEg2KjZhiDYqtin2LTZgdmK2YYg2KfZhNmF2KrZiNiz2LfYqSDZhNmE2KjZhtmK2YZkZAIHDw8WAh8ABRXYp9mE2LXZgSDYp9mE2LPYp9io2LlkZAIJDw8WAh8ABQQ4NS4xZGQCCw8PFgIfAAUBNGRkAg0PDxYCHwAFAjMwZGRk6LKA0rBL6Yx5cS2Hl2NEwSUbmlX5+yavx0UvV8Z01sg=',
        '__VIEWSTATEGENERATOR': 'FE2B3F1E',
        '__EVENTVALIDATION': '/wEdAAM3LIpD9FKmw2qsjajZ2HvX/LoBA+N6yzyjsmmTaOURj5+I/HPZ86NEZcbXwR9jxA53QBWH6lve2Tb7cOeQATtEPHViQReZQIO2qpx+yXKhdw==',
        'ctl00$MainContent$txtCivilID': h,
        'ctl00$MainContent$btnSearch': 'بحث'
    }

    vv = a.post(url, data=data, headers=headers)

    v = vv.text

    if v.find("الرجاء التاكد من إدخال الرقم المدني بشكل صحيح") >= 0:

        print("[Wrong Number] Pls Enter Correct One\n")

        input("Press Any Key To Exit...")

    elif v.find("الرجاء التاكد ان المدرسة قامت برفع النتائج") >= 0:

        co += 1

        print(f"[Waiting] Attempt: {co}")

        time.sleep(4)

        checkk()

    else:
        co += 1
        print(f"[Found !] Attempt: {co} \n")
        
        soup = BeautifulSoup(v, "html.parser")
        
        name = soup.find("span", id="MainContent_lblName")
        
        cid = soup.find("span", id="MainContent_lblCid")
        
        school = soup.find("span", id="MainContent_lblSchool")
        
        grade = soup.find("span", id="MainContent_lblLevel")
        
        result = soup.find("span", id="MainContent_lblPercent")
        
        pp = f"""
           ______     _ _  ______                      _   
           |  ___|   | | | | ___ \                    | |  
           | |_ _   _| | | | |_/ /___ _ __   ___  _ __| |_ 
           |  _| | | | | | |    // _ \ '_ \ / _ \| '__| __|
           | | | |_| | | | | |\ \  __/ |_) | (_) | |  | |_ 
           \_|  \__,_|_|_| \_| \_\___| .__/ \___/|_|   \__|
                                     | |                   
                                     |_|
            
           ~______________________________________________________~               
                        Credit: @_agf - Soud#0737
           Name: {name.text}
           CID: {cid.text}
           School: {school.text}
           Grade: {grade.text}
           Result: %{result.text}
                                                            Bye <3
           ~______________________________________________________~          
           
           \n"""
        print(pp)
        with open("Result.txt", "a", encoding="utf-8") as wr:
            wr.write(pp)
        input("Press Any Key To Exit...")  


checkk()
