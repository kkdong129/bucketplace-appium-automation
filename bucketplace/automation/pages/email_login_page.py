from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class EmailLoginPage(BasePage):
    # 로케이터 정의
    EMAIL_LOGIN_TEXT = (AppiumBy.ID, 'net.bucketplace:id/emailLogInText') # 진입점
    EMAIL_TITLE = (AppiumBy.ID, 'net.bucketplace:id/title')
    BACK_ICON = (AppiumBy.ID, 'net.bucketplace:id/backIcon')
    EMAIL_ID_FIELD = (AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="net.bucketplace:id/inputField" and @text="이메일"]')
    EMAIL_PW_FIELD = (AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="net.bucketplace:id/inputField" and @text="비밀번호"]')
    EMAIL_LOGIN_BTN = (AppiumBy.ID, 'net.bucketplace:id/loginButton')
    PW_FIND_BTN = (AppiumBy.ID, 'net.bucketplace:id/passwordFindingButton')
    EMAIL_EMPTY_TOAST = (AppiumBy.XPATH, '//android.widget.Toast[@text="이메일을 입력해주세요."]')
    PW_EMPTY_TOAST = (AppiumBy.XPATH, '//android.widget.Toast[@text="비밀번호를 입력해주세요."]')
    INVALID_PW_TOAST = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "10번 실패하면 10분간 로그인이 제한돼요.")]')
    LIMMIT_LOGIN_TOAST = (AppiumBy.XPATH, '//android.widget.TextView[@text="로그인이 제한되었어요. 10분 후 다시 시도해주세요."]')

    def enter_account_infos(self, email=None, password=None):
        '''이메일과 비밀번호 입력 (값이 있을 때만 입력)'''
        if email:
            self.type(self.EMAIL_ID_FIELD, email)
        if password:
            self.type(self.EMAIL_PW_FIELD, password)

    def click_login(self):
        '''로그인 버튼 클릭'''
        self.click(self.EMAIL_LOGIN_BTN)

    def is_at_email_login_page(self):
        '''이메일 로그인 페이지의 구성 요소 확인'''
        return all([
            self.is_displayed(self.EMAIL_TITLE),
            self.is_displayed(self.BACK_ICON),
            self.is_displayed(self.EMAIL_ID_FIELD),
            self.is_displayed(self.EMAIL_PW_FIELD),
            self.is_displayed(self.EMAIL_LOGIN_BTN),
            self.is_displayed(self.PW_FIND_BTN)
        ])

    def are_fields_empty(self):
        '''입력 필드 초기화 여부 확인'''
        return self.is_input_empty(self.EMAIL_ID_FIELD, '이메일') and \
               self.is_input_empty(self.EMAIL_PW_FIELD, '비밀번호')

    def check_toast_message(self, locator):
        '''토스트 메시지 존재 여부 확인'''
        return self.check_element(locator)
