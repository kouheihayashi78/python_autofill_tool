import jpholiday
from time import sleep
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import config

debug = False
print(f"デバッグモード : { "ON" if debug else "OFF"}")

today = date(2024, 11, 14) if debug else date.today()
day = today.day 
# タイムカードページのハンバーガーメニューの中の打刻申請のidを取得
dayStr = f"button_0590218142014" if debug else f"button_05902181420{day:02d}"

driver = webdriver.Chrome()

driver.get("https://s2.ta.kingoftime.jp/independent/recorder2/personal/")
sleep(1)
# ---------------------------------------------------------------
# ログインID入力
loginElement = driver.find_element(By.CLASS_NAME, "input-text")
loginElement.send_keys(config.loginId)
# パスワード入力
passwordElement = driver.find_element(By.ID, "password")
passwordElement.send_keys(config.loginPassword)
sleep(1)
# ログインボタン押下
loginBtnElement = driver.find_elements(By.CLASS_NAME, "btn-control-message")
loginBtnElement[0].click()
sleep(1)

# ---------------------------------------------------------------
# ハンバーガーメニュー押下
menuElement = driver.find_element(By.ID, 'menu_icon')
menuElement.click()
sleep(1)
# タイムカード押下
timeCardLinkElement = driver.find_element(By.XPATH, '//*[@id="menu"]/li[1]/a')
timeCardLinkElement.click()
sleep(1)

# ---------------------------------------------------------------
# 打刻申請押下
options = driver.find_elements(By.TAG_NAME, "option")
# 今日の日付を含むvalue属性を探す
for option in options:
    value = option.get_attribute("value")
    if value and dayStr in value:
        print(f"見つかったvalue: {value}")
        option.click()
        break
else:
    print("今日の日付を含むvalueが見つかりませんでした")
sleep(1)

# ---------------------------------------------------------------
alreadyRequestElements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/h4')
alreadyRequestElement = alreadyRequestElements[0] if alreadyRequestElements else None
print(f"今日の日付 : {today}")
print(f"今日の日付の曜日 : {today.weekday()}")
print(f'jpholiday : {jpholiday.is_holiday(today)}')
if today.weekday() in [5, 6] or jpholiday.is_holiday(today):
    print("今日は土曜日または日曜日または祝日のため申請処理を中止します")
else:
    print("今日は平日のため申請処理を継続します")
    if alreadyRequestElement :
        print(f"申請済みの日付のため申請処理を中止しました")
    else :
        # 出勤セレクト
        optionWorkStartElement = driver.find_element(By.ID, "recording_type_code_1")
        selectWorkStartElement = Select(optionWorkStartElement)
        selectWorkStartElement.select_by_value("1")
        sleep(1)
        # 休憩開始セレクト
        optionWorkEndElement = driver.find_element(By.ID, "recording_type_code_2")
        selectWorkEndElement = Select(optionWorkEndElement)
        selectWorkEndElement.select_by_value("3")
        sleep(1)
        # 休憩終了セレクト
        optionWorkEndElement = driver.find_element(By.ID, "recording_type_code_3")
        selectWorkEndElement = Select(optionWorkEndElement)
        selectWorkEndElement.select_by_value("4")
        sleep(1)
        # 退勤セレクト
        optionWorkEndElement = driver.find_element(By.ID, "recording_type_code_4")
        selectWorkEndElement = Select(optionWorkEndElement)
        selectWorkEndElement.select_by_value("2")
        sleep(1)

        # 出勤時間登録
        inputWorkStartElement = driver.find_element(By.ID, "recording_timestamp_time_1")
        inputWorkStartElement.send_keys(config.workStartTime)
        sleep(1)
        # 休憩開始時間登録
        inputWorkEndElement = driver.find_element(By.ID, "recording_timestamp_time_2")
        inputWorkEndElement.send_keys(config.workStartBreak)
        sleep(1)
        # 休憩終了時間登録
        inputWorkEndElement = driver.find_element(By.ID, "recording_timestamp_time_3")
        inputWorkEndElement.send_keys(config.workEndBreak)
        sleep(1)
        # 退勤時間登録
        inputWorkEndElement = driver.find_element(By.ID, "recording_timestamp_time_4")
        inputWorkEndElement.send_keys(config.workEndTime)
        sleep(1)

        # 出勤メッセージ登録
        inputWorkStartMessageElement = driver.find_element(By.NAME, "request_remark_1")
        inputWorkStartMessageElement.send_keys(config.workMessage)
        sleep(1)
        # 休憩開始メッセージ登録
        inputWorkEndMessageElement = driver.find_element(By.NAME, "request_remark_2")
        inputWorkEndMessageElement.send_keys(config.workMessage)
        sleep(1)
        # 休憩終了メッセージ登録
        inputWorkEndMessageElement = driver.find_element(By.NAME, "request_remark_3")
        inputWorkEndMessageElement.send_keys(config.workMessage)
        sleep(1)
        # 退勤メッセージ登録
        inputWorkEndMessageElement = driver.find_element(By.NAME, "request_remark_4")
        inputWorkEndMessageElement.send_keys(config.workMessage)
        sleep(1)

        # 打刻申請ボタン押下
        requestWorkTimeElement = driver.find_elements(By.ID, "button_01")
        requestWorkTimeElement[0].click()
        print('申請処理が完了しました')
sleep(3)
