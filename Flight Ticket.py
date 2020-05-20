import time
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import timedelta, datetime
import pandas as pd


def cheap_flight_app():
    while True:
        print("Welcome to an application of cheap flight ticket")
        print("I will provide information of the best price ticket based on the website : Kayak")
        cmd = input("[info], [leave] ")
        if cmd == "leave":
            break
        elif cmd == "info":
            origin = input("Please tell me your origin city (in term of airport code e.g. Hong Kong International Airport: HKG)")
            destination = input("Please tell me your destination city (in term of airport code e.g. Hong Kong International Airport: HKG)")
            startdate = input("Depart On (yyyy-mm-dd)")
            enddate = input("Return On (yyyy-mm-dd)")
            print("Loading info...")
            print("--------------------------------------------------------------------------------------")
            cheap_flight_ticket_app(origin,destination,startdate,enddate)
            print("--------------------------------------------------------------------------------------")




def cheap_flight_ticket_app(origin, destination, startdate, enddate):
    try:

        url = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + startdate + "/" + enddate + "?sort=bestflight_a"
        #Your path of Google Chrome
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
        driver.implicitly_wait(30)
        driver.get(url)

        time.sleep(10)

        # The cheapest and the best price of the flight from Kayak
        html = BeautifulSoup(driver.page_source, 'html.parser')
        cheapest_price = html.find("span", attrs={"class": "js-label js-price _itL _ibU _ibV _idj _kK7"}).text.strip()
        print("The cheapest price of the flight from {} to {} is {}".format(startdate, enddate, cheapest_price))
        cheapest_price_dur = html.find("span", attrs={"class": "js-subLabel js-duration _ibU _ibV _idj _kLa _kLb _kLc _kK7 _kLe"}).text.strip()
        print("And the duration of the flight is {}".format(cheapest_price_dur))

        print("--------------------------------------------------------------------------------------")

        best_price = html.find("span", attrs={"class": "js-label js-price _itL _ibU _ibV _idj _kKW"}).text.strip()
        print("The best price of the flight from {} to {} is {}".format(startdate, enddate, best_price))
        best_price_dur = html.find("span", attrs={"class": "js-subLabel js-duration _ibU _ibV _idj _kLa _kLb _kLc _kKW _kLe"}).text.strip()
        print("And the duration of the flight is {}".format(best_price_dur))

        price_list = []
        dur_list = []
        price_list.append(best_price)
        dur_list.append(best_price_dur)

        print("--------------------------------------------------------------------------------------")
        print("loading more information...")
        print()

        # Best price comparision 1
        startdate1 = datetime.strptime(startdate, '%Y-%m-%d').date() + timedelta(2)
        startdate1 = startdate1.strftime('%Y-%m-%d')
        enddate1 = datetime.strptime(enddate, '%Y-%m-%d').date() + timedelta(2)
        enddate1 = enddate1.strftime('%Y-%m-%d')

        url1 = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + startdate1 + "/" + enddate1 + "?sort=bestflight_a"
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
        driver.implicitly_wait(30)
        driver.get(url1)

        time.sleep(10)

        html1 = BeautifulSoup(driver.page_source, 'html.parser')
        best_price1 = html1.find("span", attrs={"class": "js-label js-price _itL _ibU _ibV _idj _kKW"}).text.strip()
        best_price_dur1 = html1.find("span", attrs={"class": "js-subLabel js-duration _ibU _ibV _idj _kLa _kLb _kLc _kKW _kLe"}).text.strip()

        price_list.append(best_price1)
        dur_list.append(best_price_dur1)

        # Best price comparision 2
        startdate2 = datetime.strptime(startdate, '%Y-%m-%d').date() + timedelta(7)
        startdate2 = startdate2.strftime('%Y-%m-%d')
        enddate2 = datetime.strptime(enddate, '%Y-%m-%d').date() + timedelta(7)
        enddate2 = enddate2.strftime('%Y-%m-%d')

        url2 = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + startdate2 + "/" + enddate2 + "?sort=bestflight_a"
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
        driver.implicitly_wait(30)
        driver.get(url2)

        time.sleep(10)

        html2 = BeautifulSoup(driver.page_source, 'html.parser')
        best_price2 = html2.find("span", attrs={"class": "js-label js-price _itL _ibU _ibV _idj _kKW"}).text.strip()
        best_price_dur2 = html2.find("span", attrs={"class": "js-subLabel js-duration _ibU _ibV _idj _kLa _kLb _kLc _kKW _kLe"}).text.strip()

        price_list.append(best_price2)
        dur_list.append(best_price_dur2)

        # Best price comparision 3
        startdate3 = datetime.strptime(startdate, '%Y-%m-%d').date() + timedelta(14)
        startdate3 = startdate3.strftime('%Y-%m-%d')
        enddate3 = datetime.strptime(enddate, '%Y-%m-%d').date() + timedelta(14)
        enddate3 = enddate3.strftime('%Y-%m-%d')

        url3 = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + startdate3 + "/" + enddate3 + "?sort=bestflight_a"
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
        driver.implicitly_wait(30)
        driver.get(url3)

        time.sleep(10)

        html3 = BeautifulSoup(driver.page_source, 'html.parser')
        best_price3 = html3.find("span", attrs={"class": "js-label js-price _itL _ibU _ibV _idj _kKW"}).text.strip()
        best_price_dur3 = html3.find("span", attrs={"class": "js-subLabel js-duration _ibU _ibV _idj _kLa _kLb _kLc _kKW _kLe"}).text.strip()

        price_list.append(best_price3)
        dur_list.append(best_price_dur3)



        startdate_list = [startdate,startdate1,startdate2,startdate3]
        enddate_list = [enddate,enddate1,enddate2,enddate3]


        # Pandas Dataframe
        dataframe = pd.DataFrame({"Origin": origin,
                                  "Destination": destination,
                                  "Start Date": startdate_list,
                                  "End Date": enddate_list,
                                  "Price ($USD)": price_list,
                                  "Duration": dur_list})

        print("Table of Comparison:")
        print(dataframe)
    except AttributeError:
        print("Sorry, we cannot provide the information of the best price\nPlease try again")
    except ValueError:
        print("Sorry, please enter a valid date")


cheap_flight_app()