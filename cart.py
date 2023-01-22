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
removed_players = set()

# Carrega jogadores removidos do arquivo
with open("removed_players.txt", "r") as f:
    for line in f:
        removed_players.add(line.strip())

with open("previous_players.txt", "a+") as f:
    for line in f:
        previous_players.add(line.strip())

url = input("Insira a URL da partida a ser monitorada: ")
interval = int(input("Insira o intervalo de verificação em segundos: "))
driver = uc.Chrome()
while True:

    driver.get(url)
    driver.maximize_window()
    time.sleep(6)
    #close_cock = driver.find_element(By.CSS_SELECTOR, '.ccm-CookieConsentPopup_Accept')
    
    time.sleep(1)
    mercado = WebDriverWait(driver, timeout=60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ipe-GridHeaderTabLink:nth-child(9) > div:nth-child(1)'))).click()
    time.sleep(1)
    close_Gol = WebDriverWait(driver, timeout=60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sip-MarketGroup_Open > div:nth-child(1)'))).click()
    time.sleep(1)
    show_cart = WebDriverWait(driver, timeout=60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.sip-MarketGroup:nth-child(4) > div:nth-child(1) > div:nth-child(1)'))).click()
    time.sleep(1) 
 
    game_name = driver.find_element(By.CSS_SELECTOR, '.ipe-EventHeader_Fixture')
    current_game = str(game_name.text)
    time.sleep(1)
    players_list = driver.find_elements(By.CSS_SELECTOR,'div.sip-TotalBandParticipant > span:nth-child(1)')
    current_players = set({item.get_attribute('outerText') for item in players_list})
    # Identifica jogadores que sairam da lista
    removed_players = removed_players.union(previous_players.difference(current_players))
    removed_players = removed_players.difference(current_players)
    if removed_players:
       print("Jogadores que saíram da lista: ", removed_players)
    print("Jogadores que saíram da lista: ", len(removed_players))    
    
    # Identifica jogadores que voltaram para a lista
    returned_players = current_players.intersection(removed_players)
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

# Save previous_players to a file
    with open("previous_players.txt", "w") as f:
         for player in previous_players:
            f.write(player + "\n")

# Save removed_players to a file
    with open("removed_players.txt", "w") as f:
         for player in removed_players:
            f.write(player + "\n")

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


