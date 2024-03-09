import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Retry mechanism to wait for the element to become clickable
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div/button/span')))
    close_button.click()
except Exception as e:
    print("Error:", e)

import subprocess

# Run the Python program to generate the mnemonic and capture its output
process = subprocess.Popen(['python', 'mmbf.py'], stdout=subprocess.PIPE)
output, _ = process.communicate()

# Split the output string into individual words and assign it to MNEMONIC
MNEMONIC = output.decode().strip().split()

# Continue with the rest of the script...
PASSWORD = '11111111'
#--------------------------------------------------selenium config
chrome_options = Options()
chrome_options.add_extension('MetaMask_Chrome.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(1)
# Wait until at least one window handle is available
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Adjust the number as needed

# Switch to the second window handle
driver.switch_to.window(driver.window_handles[1])

time.sleep(0.5)
#--------------------------------------------------

# fix "Message: unknown error: Runtime.callFunctionOn threw exception: Error: LavaMoat"  
# solution: https://github.com/LavaMoat/LavaMoat/pull/360#issuecomment-1547271080

driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input').click() # agree to TOS 
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button').click() # import 
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div/button[2]').click() # no thanks
time.sleep(0.5)
for i in range(3): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # locate mnemonic box
for word in MNEMONIC:
    driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
    for i in range(2): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    # time.sleep(0.5)
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click() # confirm
time.sleep(0.5)
# After the code block where you tried to click the confirmation button
try:
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click() # confirm
    time.sleep(0.5)
except Exception as e:
    print("Confirmation button click failed. Proceeding with mnemonic input.")
    # Run mnemonic input logic here
    for i in range(3): 
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # locate mnemonic box
    for word in MNEMONIC:
        driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
        for i in range(2): 
            driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    time.sleep(0.5)

driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(PASSWORD) # enter password
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(PASSWORD) # enter password twice
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click() # I understand
driver.find_element('xpath', '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click() # import my wallet
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # got it
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # next page
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # done
time.sleep(1)
driver.find_element('xpath', '/html/body/div[2]/div/div/section/div[1]/div/button/span').click() # close

print('import complete')
time.sleep(999999)