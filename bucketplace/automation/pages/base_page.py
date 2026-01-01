from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 기본 대기 시간

    def find_element(self, locator):
        '''단일 요소가 화면에 나타날 때까지 기다린 후 반환'''
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Error: 요소를 찾을 수 없습니다 -> {locator}')
            self.save_screenshot(f'timeout_{str(locator)}')
            raise

    def click(self, locator):
        '''요소를 클릭할 수 있을 때까지 기다린 후 클릭'''
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f'Click 실패: {locator}')
            raise e

    def type(self, locator, text):
        '''텍스트 입력 필드에 값을 입력'''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        '''요소가 현재 화면에 보이는지 여부 확인'''
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    def press_back(self):
        '''안드로이드 시스템 뒤로가기 동작 실행'''
        self.driver.back()

    def close_popup_if_exists(self, locator):
        try:
            close_btn = self.wait.until(EC.presence_of_element_located(locator))
            close_btn.click()
        except (NoSuchElementException, TimeoutException, InvalidSelectorException):
            # 팝업이 없으면 에러 없이 그냥 통과
            pass

    def check_element(self, locator, timeout=3):
        '''에러를 발생시키지 않고 요소의 존재 여부만 빠르게 확인'''
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def is_input_empty(self, locator, placeholder, timeout=5):
        '''입력란이 비어 있는지 확인합니다.'''
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            current_text = element.text
            # 1. 텍스트가 아예 없거나 (None 또는 '')
            if not current_text:
                return True
            # 2. 혹은 힌트 텍스트(placeholder)와 일치하는지 확인
            return current_text == '' or current_text == placeholder
        except:
            return False

    def save_screenshot(self, name):
        '''스크린샷을 특정 폴더에 절대 경로로 저장'''
        folder_path = os.path.join(os.getcwd(), 'screenshots')

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f'폴더 생성됨: {folder_path}')

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        # 파일명에 포함될 수 없는 특수문자(:, /, \)를 언더바로 치환
        safe_name = str(name).replace(':', '_').replace('/', '_').replace('\\', '_')
        file_name = f'{safe_name}_{timestamp}.png'
        file_path = os.path.join(folder_path, file_name)

        result = self.driver.save_screenshot(file_path)

        if result:
            print(f'스크린샷 저장 완료: {file_path}')
        else:
            print('스크린샷 저장 실패: 드라이버 연결 상태를 확인하세요.')
