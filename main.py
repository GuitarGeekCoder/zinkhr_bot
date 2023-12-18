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
            time.sleep(2)
            # Find and fill the employee code field
            productlist[1].clear()
            productlist[1].send_keys(emp_code)
            time.sleep(2)
            # Find and fill the password field
            productlist[2].clear()
            productlist[2].send_keys(password)

            # Wait for a few seconds to allow the login process to complete
            time.sleep(5)

            # Submit the form
            punchin_button = driver.find_element(By.CSS_SELECTOR, 'button[data-status="PUNCHIN"]')
            punchin_button.click()
            print("punchin done")
            time.sleep(5)

            # Perform additional actions if needed
    except Exception as e:
        print("Exception:", str(e))
    finally:
        # Close the browser window
        driver.quit()

def automate_logout(company_code, emp_code, password):
    driver = webdriver.Chrome()
    try:
        # Open the website
        driver.get('https://portal.zinghr.com/2015/pages/authentication/login.aspx')

        # Find and fill the company code field
        productlist = driver.find_elements(By.CLASS_NAME, 'formTextField-input')
        if len(productlist) > 2:
            productlist[0].clear()
            productlist[0].send_keys(company_code)
            time.sleep(2)
            # Find and fill the employee code field
            productlist[1].clear()
            productlist[1].send_keys(emp_code)
            time.sleep(2)
            # Find and fill the password field
            productlist[2].clear()
            productlist[2].send_keys(password)

            # Wait for a few seconds to allow the login process to complete
            time.sleep(5)

            # Submit the form
            punchout_button = driver.find_element(By.CSS_SELECTOR, 'button[data-status="PUNCHOUT"]')
            punchout_button.click()
            print("punchout done")
            time.sleep(5)

            # Perform additional actions if needed
    except Exception as e:
        print("Exception:", str(e))
    finally:
        # Close the browser window
        driver.quit()
         
def job_login():
    # Schedule this job every morning at 9 AM (except Sundays)
    automate_login('writer', '046294', 'Airtel@123')
def job_logout():
    automate_logout('writer', '046294', 'Airtel@123')

# Schedule the job
schedule.every().monday.at("09:00").do(job_login)
schedule.every().tuesday.at("09:00").do(job_login)
schedule.every().wednesday.at("09:00").do(job_login)
schedule.every().thursday.at("09:00").do(job_login)
schedule.every().friday.at("09:00").do(job_login)
schedule.every().saturday.at("09:00").do(job_login)

# Schedule the job
schedule.every().monday.at("19:30").do(job_logout)
schedule.every().tuesday.at("19:30").do(job_logout)
schedule.every().wednesday.at("19:30").do(job_logout)
schedule.every().thursday.at("19:30").do(job_logout)
schedule.every().friday.at("19:30").do(job_logout)
schedule.every().saturday.at("19:30").do(job_logout)

while True:
    schedule.run_pending()
    time.sleep(1)
