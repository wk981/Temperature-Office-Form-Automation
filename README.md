# Python Office Form Automate Using Selenium
I have been using python to automate temperature recording office form using selenium. My country has decided to lift the covid 19 restriction recently and I have decided to share my project.
Due to the confidential and restricted contents from the form, I am only allowed to show the templates of my scripts.

## Technologies used
Selenium
PythonTelegramBotAPI
Raspberry pi Crontab

## Project Setup
### PythonTelegramBotAPI
pip install pyTelegramBotAPI

### dotenv
pip install python-dotenv

### Selenium
pip install selenium

### Chromium driver in Raspberry pi
sudo apt install chromium-chromedriver
sudo apt install chromium-browser

### Crontab
crontab - 0 * * * *  DISPLAY=:0 python my_script.py

## To use the telegrambot 
1) Ensure that you have an .env created to store all your related API keys
2) Open a terminal, key in python main.py

### How to use Selenium?
1) Inspect the Web by right clicking and pressing inspect
2) Hover your mouse over the textbox or radio button and peer into the inspection menu on the right side
3) Example - Clicking the Radio button. RadioButton = web.find_element_by_css_selector("input[type='radio'][value='Value']").click()
4) Example - Writing into the textbox. Textbox = web.find_element_by_css_selector('input[aria-labelledby="QuestionId_re8865ca7664940f58f276cd4834dfcf6 QuestionInfo_re8865ca7664940f58f276cd4834dfcf6"]') 
5) Textbox.sendkey('HELLO WORLD')

Head over to [Instructions](https://github.com/wk981/Temperature-Office-Form-Automation/tree/main/Instructions) for how to do it.

### How does my script works?
Selenium will be using chromedriver to browse the web and perform the instructions given in the script. I preferred web browser features for chromedriver are listed in my script as options. If you do not want to see your script performing the task physically, you can opt for _headless_ option.
