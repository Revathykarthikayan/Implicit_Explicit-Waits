from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Imdb_Search:

    def __init__ (self) :
        
        #initialise the webdriver
        self.driver=webdriver.Chrome()
    

    def navigate_to_webpage(self,url):
           
        # Navigate to the webpage
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def insert_data(self):
    
       
         try:

            # clicking expand all to make all input fields visible
            expand=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="ipc-icon ipc-icon--expand-more ipc-btn__icon ipc-btn__icon--post"]')))
            expand.click()

            #sending keys to name textbox
            name= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//input[@id="text-input__3"]')))
            name.send_keys("A.R. Rahman")
            print(" Input- Name given")

            #scroll into webpage
            self.driver.execute_script("window.scrollBy(0, 500);") 

            #sending keys to birthday textbox
            birthday=WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//input[@id="text-input__4"]')))
            birthday.send_keys("06-01-1967")
            print(" Input - Birthday given")

            #clicking  awards section
            enterenter_Awards=WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[text()="Oscar-Winning"]')))
            pyautogui.typewrite('enter')
            print(" Oscar-Winning is selected")

             #scroll into webpage
            self.driver.execute_script("window.scrollBy(0, 500);") 


            #sending keys to place of birth textbox
            place_of_birth=WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='ipc-chip__text'])[20]")))
            birthday.send_keys("Chennai")
            print(" place of birth given")

            #clicking  gender section
            Gender=WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='ipc-chip__text'])[26]")))
            pyautogui.typewrite('enter')
            print(" Gender selected")

            #enableing radio button
            Adult_names=WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="include-adult-names"]')))
            pyautogui.typewrite('enter')
            print(" Include adult name is Enabled")


            #search results button is clicked
            Submit=self.driver.find_element(By.XPATH,"(//span[@class='ipc-btn__text'])[10]")
            pyautogui.typewrite('enter')
            print(" See Results button is clicked")


         except Exception as e:

            print(f"An error occurred: {e}")

    #Quiting browser
    def quit(self):
         self.driver.quit()
         print(" Search successful browser closed")


if __name__ == "__main__":
    url = "https://www.imdb.com/search/name/"
    test = Imdb_Search()
    test.navigate_to_webpage(url)
    test.insert_data()
    test.quit()