import json
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



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
# Assuming the condition is true, start the loop
try:
    while True:
        # Run the Python program to generate the mnemonic and capture its output
        process = subprocess.Popen(['python', 'mmbf.py'], stdout=subprocess.PIPE)
        output, _ = process.communicate()

        # Split the output string into individual words and assign it to MNEMONIC
        MNEMONIC = output.decode().strip().split()
        
        # Loop through the input fields
        for i, word in enumerate(MNEMONIC, start=1):
            # Construct the XPath dynamically
            xpath = f'/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[{i}]/div[1]/div/input'
            # Locate the input field
            input_field = driver.find_element(By.XPATH, xpath)
            # Select all text in the input field
            input_field.send_keys(Keys.CONTROL, 'a')
            # Delete the selected text
            input_field.send_keys(Keys.DELETE)
            # Input the word from MNEMONIC list for each loop iteration
            input_field.send_keys(word)
            # If it's not the last input field, send TAB key
            if i < len(MNEMONIC):
                input_field.send_keys(Keys.TAB)
            # Check if the confirm button is clickable
            try:
                confirm_button = WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button')))
                if confirm_button:
                    # If confirm button is clickable, break the loop
                    raise StopIteration
            except TimeoutException:
                pass
except StopIteration:
    pass
# Click the confirm button
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click() # confirm
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(PASSWORD) # enter password
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(PASSWORD) # enter password twice
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click() # I understand
driver.find_element('xpath', '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click() # import my wallet
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # got it
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # next page
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # done
time.sleep(1)
driver.find_element('xpath', '/html/body/div[2]/div/div/section/div[1]/div/button/span').click() # close
# Locate the element
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/span[1]')

# Get the text value of the element
value = element.text

# Print or use the value as needed
print("Value:", value)

driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/button/span').click()
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/button[6]').click()
driver.find_element('xpath', '/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/button[4]').click()
driver.find_element('xpath', '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/button').click()
driver.find_element('xpath', '/html/body/div[3]/div[3]/div/section/button[1]').click()
driver.find_element('xpath', '/html/body/div[3]/div[3]/div/section/button[2]').click()
driver.find_element('xpath', '/html/body/div[3]/div[3]/div/section/button[1]').click()
driver.find_element('xpath', '/html/body/div[3]/div[3]/div/section/button[1]').click()
driver.find_element('xpath', '/html/body/div[3]/div[3]/div/section/button[1]').click()
driver.find_element('xpath', '/html/body/div[1]/div/div[3]/div/form/div/input').send_keys(PASSWORD)
driver.find_element('xpath', '/html/body/div[1]/div/div[3]/div/div[2]/button[2]').click()
element = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div[2]/button/span')

# Perform a long click for 5 seconds
action = ActionChains(driver)
action.click_and_hold(element).pause(5).release().perform()

driver.find_element('xpath', '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/button').click()

print('import complete')
time.sleep(20)

