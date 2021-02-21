import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome("chromedriver.exe")
# def test_fullpage_screenshot():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--start-maximized')
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     time.sleep(2)
#     ele=driver.find_element("xpath", '//div[@class="react-grid-layout layout"]')
#     total_height = ele.size["height"]+1000
#
#     driver.set_window_size(1920, total_height)      #the trick
#     time.sleep(2)
#     driver.save_screenshot("screenshot1.png")

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cwd = os.getcwd()
print(cwd)
# sys.exit()
path = os.path.join(cwd, f"{sys.argv[1]}")
os.mkdir(path)
for alpha in alphabets:
    path = os.path.join(cwd + "/" + f"{sys.argv[1]}", f"{sys.argv[1]}" + "_" + f"{alpha}")
    os.mkdir(path)
    os.chdir(cwd + "/" + f"{sys.argv[1]}" + "/" + f"{sys.argv[1]}" + "_" + f"{alpha}")
    url1 = "https://" + f"codeforces.com/problemset/problem/{sys.argv[1]}/" + f"{alpha}"
    print(url1)
    try:
        driver.get(url1)
    except:
        sys.exit()
    test_fullpage_screenshot()
    save = True
    i = 1

    while save:
        url = "//*[@id='pageContent']/div[3]/div[2]/div/div[5]/div[2]/div[" + f"{i}" + "]"
        try:
            val = driver.find_element_by_xpath(url)
        except:
            save = False
            break
        inputx = val.get_attribute("innerText")
        print(inputx)
        f = open("input" + f"{int((i+1)/2)}" + ".txt", "w")
        f.write(inputx)
        f.close()
        i+=1
        url = "//*[@id='pageContent']/div[3]/div[2]/div/div[5]/div[2]/div[" + f"{i}" + "]"
        try:
            val = driver.find_element_by_xpath(url)
        except:
            save = False
            break
        outputx = val.get_attribute("innerText")
        print(outputx)
        f = open("output" + f"{int(i/2)}" + ".txt", "w")
        f.write(outputx)
        f.close()
        i += 1
