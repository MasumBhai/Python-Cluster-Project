import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import sys


def main():
    link = input("Just copy & paste your Favourite MIST department's Faculty website's link:\n")

    def isValidURL(lnk):
        # Regex to check valid URL
        if (lnk == None):
            return False
        regex = ("((http|https)://)(www.)?" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                 "{2,256}\\.[a-z]" +
                 "{2,6}\\b([-a-zA-Z0-9@:%" +
                 "._\\+~#?&//=]*)")

        # Compile the ReGex
        p = re.compile(regex)
        if (re.search(p, lnk)):
            return True
        else:
            return False

    if (isValidURL(link) == True):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify())
        faculty_names = soup.findAll('h5')
        # print(faculty_names)
        teachers = [nam.get_text() for nam in faculty_names]
        # print(teachers)
        portfolioes = soup.findAll(class_="portfolio-desc")
        # print(portfolioes)
        teacherrs_name = [portfolio.find('h5').get_text() for portfolio in portfolioes]
        teacherrs_post = [portfolio.find('span').text for portfolio in portfolioes]
        teacherrs_email = []
        information = soup.find_all('div', {'class': 'portfolio-desc'})
        for info in information:
            # print(info)
            email = info.find_next('span').find_next('span').text
            teacherrs_email.append(email)
            # print(email)

        # print(teacherrs_name)
        # print(teacherrs_post)
        # print(teacherrs_email)

        # for x in range(0, len(teacherrs_name)):
        #     print("##################################")
        #     print(teacherrs_name[x])
        #     print(teacherrs_post[x])
        #     print(teacherrs_email[x])

        faculty_stuffs = pd.DataFrame({
            'Teacher_name': teacherrs_name,
            'Teacher_Signature': teacherrs_post,
            'email_address': teacherrs_email,
        })
        # print(faculty_stuffs)
        file_name = input("Giva a Name your file to store these data: ")
        faculty_stuffs.to_csv(file_name + "_poweredby_HackerMan_Masum" + ".csv")
        print("\nNow go to your File Explorer(where this .exe is located)\n& you will see a csv file with extension '_poweredby_HackerMan_Masum'\nHa Ha..Open that file..have fun...")

    else:
        print("That was not url...maybe..")


if __name__ == "__main__":
    main()
    while True:
        ans = input("\nDo You Want to Try Again?(press: Enter)\nOr you want to quit?(press: any key)\n")
        if ans == "":
            main()
        else:
            break
    sys.exit("C U SOON")
