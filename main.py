from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule

def automate_login(company_code, emp_code, password):
    driver = webdriver.Chrome()
    try:
        # Open the website
        driver.get('https://portal.zinghr.com/2015/pages/authentication/login.aspx')

        # Find and fill the company code field
        productlist = driver.find_elements(By.CLASS_NAME, 'formTextField-input')
        if len(productlist) > 2:
            productlist[0].clear()
            productlist[0].send_keys(company_code)

            # Find and fill the employee code field
            productlist[1].clear()
            productlist[1].send_keys(emp_code)

            # Find and fill the password field
            productlist[2].clear()
            productlist[2].send_keys(password)

            # Wait for a few seconds to allow the login process to complete
            time.sleep(5)

            # Submit the form
            punchin_button = driver.find_element(By.CSS_SELECTOR, 'button[data-status="PUNCHIN"]')
            punchin_button.click()
            time.sleep(8.5 * 60 * 60)
                
            punchout_button = driver.find_element(By.CSS_SELECTOR, 'button[data-status="PUNCHOUT"]')
            punchout_button.click()
            time.sleep(5)

            # Perform additional actions if needed
    except Exception as e:
        print("Exception:", str(e))
    finally:
        # Close the browser window
        driver.quit()

def job():
    # Schedule this job every morning at 9 AM (except Sundays)
    automate_login('writer', '046294', 'Airtel@123')

# Schedule the job
schedule.every().monday.at("09:00").do(job)
schedule.every().tuesday.at("09:00").do(job)
schedule.every().wednesday.at("09:00").do(job)
schedule.every().thursday.at("09:00").do(job)
schedule.every().friday.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
