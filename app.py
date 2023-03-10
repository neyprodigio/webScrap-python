import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import json
import undetected_chromedriver.v2 as uc
from plyer import notification

previous_players = set()
with open("previous_players.txt", "a+") as f:
    for line in f:
        previous_players.add(line.strip())
url = input("Insira a URL da partida a ser monitorada: ")
interval = int(input("Insira o intervalo de verificação em segundos: "))
driver = uc.Chrome()
while True:

    driver.get(url)
    driver.maximize_window()
    time.sleep(8)
    mercado = WebDriverWait(driver, timeout=30).until(EC.invisibility_of_element((By.CSS_SELECTOR, 'div.ipe-GridHeaderTabLink:nth-child(9) > div:nth-child(1)'))).click()
    time.sleep(1)
    show_more = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sip-ShowMore_Link'))).click() 
    time.sleep(3)
    #close_list = driver.find_element(By.CSS_SELECTOR, '.sip-MarketGroup_Open > div:nth-child(1)').click()
    #show_carts = driver.find_element(By.CSS_SELECTOR, 'div.sip-MarketGroup:nth-child(4) > div:nth-child(1) > div:nth-child(1)').click()
    #time.sleep(5)
    game_name = driver.find_element(By.CSS_SELECTOR, '.ipe-EventHeader_Fixture')
    current_game = str(game_name.text)
    time.sleep(1)
    players_list = driver.find_elements(By.CSS_SELECTOR,'div.sip-SubInParticipant > div')
    current_players = set({item.get_attribute('outerText') for item in players_list})
    # Identifica jogadores que sairam da lista
    time.sleep(1)
    removed_players = previous_players.difference(current_players)
    if removed_players:
       notification.notify(
       title=('Jogador saiu da lista no jogo: '+current_game),
       message=str(removed_players),
       timeout=5
    )
       print("Jogadores que saíram da lista: ", removed_players)
    print("Jogadores que saíram da lista: ", len(removed_players))    
    
    # Identifica jogadores que voltaram para a lista
    returned_players = previous_players.intersection(current_players)
    returned_players = returned_players.difference(current_players)
    if returned_players:
       notification.notify(
       title=('Voltou pra lista no jogo: '+current_game),
       message=str(returned_players),
       timeout=5
    )
       print("Jogadores que voltaram para a lista: ", returned_players)
    print("Jogadores que voltaram para a lista: ", len(returned_players))
    
    # Atualiza a lista anterior de jogadores
    previous_players = current_players

    previous_players_list = [{"jogador": player} for player in previous_players]
    with open("previous_players.txt", "w") as pp:
        json.dump(previous_players_list, pp)
    time.sleep(interval)














    #click = driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-PageView > div > div > div > div.wcl-PageContainer_Colcontainer > div > div > div.cm-CouponModule > div > div > div:nth-child(2) > div').click()
    #pyautogui.moveTo(734, 460)
    #pyautogui.click(button='left',x=745, y=479)
    #mostrar_mais = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/div[12]/div[2]/div/div[2]/div').click()



    # Login
    # usuario_input = driver.find_element(By.CSS_SELECTOR, 'body > div.lms-LoginModule > div > div.lms-StandardLogin_Container > div > div:nth-child(2) > input')
    # usuario_input.send_keys('neneiilson')
    # senha_input = driver.find_element(By.CSS_SELECTOR,'body > div.lms-LoginModule > div > div.lms-StandardLogin_Container > div > div.lms-StandardLogin_InputsContainer.lms-StandardLogin_InputsContainer-password > input')
    # senha_input.send_keys('121298@Nei')
    # senha_input.send_keys(Keys.RETURN)
    # time.sleep(7)


