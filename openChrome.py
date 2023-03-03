from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to the location of your Chrome driver executable
#chrome_driver_path = "/path/to/chromedriver"
chrome_driver_path = "C:/Users/chris/Documents/USC/AV Scripting/chromedriver_win32"

# Set the URL of the Google Slides presentation you want to present
#presentation_url = "https://https://docs.google.com/presentation/d/1wWHrYJAHt8SIfCbk-g2oTiQUP0HNjTx89V3wud4wEJ4/edit#slide=id.p7"
presentation_url = "https://www.wsj.com/"
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the presentation URL
driver.get(presentation_url)

# Wait for the presentation to load
driver.implicitly_wait(10)

# Print the URL of the presentation to the console
print("Presentation URL: " + driver.current_url)

# Put the presentation in presentation mode
#presentation_mode_button = driver.find_element_by_xpath("//div[@class='punch-viewer-toolbar']/div[3]/div[2]")
#presentation_mode_button.click()

# Wait for the presentation to enter presentation mode
driver.implicitly_wait(10)

# Close the Chrome window
#driver.quit()
