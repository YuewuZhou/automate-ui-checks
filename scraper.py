from selenium import webdriver

# Set up the Selenium WebDriver
driver = webdriver.Chrome('path_to_chromedriver')  # Replace with the path to your ChromeDriver executable

# Navigate to the webpage you want to scrape
driver.get('https://example.com')  # Replace with the URL of the website you want to scrape

# Example: Scrape the title of the webpage
title = driver.find_element_by_tag_name('h1').text
print(title)

# Clean up and close the browser
driver.quit()