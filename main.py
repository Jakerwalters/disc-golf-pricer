from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Hardcoded search query for now
search_query = "Discmania d-line p2"

# Establish chrome driver and go to report site URL
url = "https://www.ebay.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

# Enter search query
search_box_element = driver.find_element_by_xpath("/html/body/header/table/tbody/tr/td[5]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
search_box_element.send_keys(search_query)
search_box_element.send_keys(Keys.RETURN)

# Parse search result html elements into list of item dicts
result_list_element = driver.find_element_by_css_selector(".srp-results.srp-list.clearfix")
item_elements = result_list_element.find_elements_by_tag_name("li")

item_list = []

for item_element in item_elements:
    item_dict = {}

    try:
        item_dict["title"] = item_element.find_element_by_css_selector(".s-item__title").text
        item_dict["link"] = item_element.find_element_by_css_selector(".s-item__link").get_attribute("href")
        item_dict["ownership"] = item_element.find_element_by_css_selector(".s-item__subtitle").text
        item_dict["price"] = item_element.find_element_by_css_selector(".s-item__price").text
        item_dict["shipping_cost"] = item_element.find_element_by_css_selector(".s-item__shipping.s-item__logisticsCost").text

        item_purchase_type = item_element.find_element_by_css_selector(".s-item__purchase-options-with-icon").text

        if item_purchase_type == "Buy It Now":
            item_dict["purchase_type"] = "instant"
        else:
            item_dict["purchase_type"] = "auction"

        item_list.append(item_dict)
    except:
        pass

    # Break before "results matching fewer keywords" items begin, we don't want those
    if "s-item__before-answer" in item_element.get_attribute("class"):
        break

print(item_list)