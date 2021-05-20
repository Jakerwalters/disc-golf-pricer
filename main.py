# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Establish chrome driver and go to report site URL
url = "https://www.ebay.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

