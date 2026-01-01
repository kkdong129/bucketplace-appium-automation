import unittest
import time
from appium import webdriver
from tests.base_capability import BaseOptions
from pages.login_page import LoginPage
from pages.email_login_page import EmailLoginPage
from pages.home_page import HomePage

class Test_01_Login_Page(BaseOptions):
    def setUp(self):
        options = self.get_common_options()
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        self.login_pg = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_TC_01_install_and_activate(self):
        '''TC-01: 앱 설치 여부 확인 및 실행 테스트'''
        package_name = 'net.bucketplace'
        self.assertTrue(self.driver.is_app_installed(package_name), '앱이 설치되지 않음')

        self.driver.activate_app(package_name)
        self.assertTrue(self.login_pg.is_login_page_displayed(), '앱 실행 후 로그인 화면 진입 실패')

    def test_TC_02_main_login_ui(self):
        '''TC-02: 로그인 화면 UI 확인'''
        is_login_page_visible = self.login_pg.is_login_page_displayed()
        self.assertTrue(self.login_pg.is_login_page_displayed(), '로그인 화면 UI 요소 미노출')

class Test_02_Email_Login_Page(BaseOptions):
    def setUp(self):
        options = self.get_common_options()
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        self.login_pg = LoginPage(self.driver)
        self.email_pg = EmailLoginPage(self.driver)
        self.home_pg = HomePage(self.driver)

        # 모든 TC가 이메일 로그인 화면에서 시작하므로 공통 진입 처리
        self.login_pg.click(self.login_pg.EMAIL_LOGIN_TEXT)

    def tearDown(self):
        self.driver.quit()

    def test_TC_03_ui_verification(self):
        '''TC-03: 이메일 로그인 화면 UI 확인'''
        self.assertTrue(self.email_pg.is_at_email_login_page())

    def test_TC_04_return_to_login_page_by_back_key(self):
        '''TC-04: 이메일 로그인 화면에서 로그인 화면으로 복귀 동작 (back key)'''
        self.email_pg.press_back()
        self.assertTrue(self.login_pg.is_displayed(self.login_pg.LOGO_IMG))

    def test_TC_05_return_to_login_page_by_back_icon(self):
        '''TC-05: 이메일 로그인 화면에서 로그인 화면으로 복귀 동작 (icon)'''
        self.email_pg.click(self.email_pg.BACK_ICON)
        self.assertTrue(self.login_pg.is_displayed(self.login_pg.LOGO_IMG))

    def test_TC_06_input_field_reset_by_back_key(self):
        '''TC-06: 이메일 로그인 화면 재진입시, 입력한 내용 초기화 동작 (back key)'''
        # 입력 후 back key로 이탈 및 재진입
        user = self.config['accounts']['temp_user']
        self.email_pg.enter_account_infos(user['email'], user['password'])
        self.email_pg.press_back()
        self.login_pg.click(self.login_pg.EMAIL_LOGIN_TEXT)
        self.assertTrue(self.email_pg.are_fields_empty())

    def test_TC_07_input_field_reset_by_back_icon(self):
        '''TC-07: 이메일 로그인 화면 재진입시, 입력한 내용 초기화 동작 (icon)'''
        # 입력 후 백 아이콘(<-)으로 이탈 및 재진입
        user = self.config['accounts']['temp_user']
        self.email_pg.enter_account_infos(user['email'], user['password'])
        self.email_pg.click(self.email_pg.BACK_ICON)
        self.login_pg.click(self.login_pg.EMAIL_LOGIN_TEXT)
        self.assertTrue(self.email_pg.are_fields_empty())

    def test_TC_08_empty_email_input_toasts(self):
        '''TC-08: 이메일 미입력시, 안내 토스트 확인'''
        # 이메일 미입력
        self.email_pg.click_login()
        self.assertTrue(self.email_pg.check_toast_message(self.email_pg.EMAIL_EMPTY_TOAST))

    def test_TC_09_empty_password_input_toasts(self):
        '''TC-09: 비밀번호 미입력시, 안내 토스트 확인'''
        # 비밀번호 미입력
        user = self.config['accounts']['temp_user']
        self.email_pg.enter_account_infos(email=user['email'])
        self.email_pg.click_login()
        self.assertTrue(self.email_pg.check_toast_message(self.email_pg.PW_EMPTY_TOAST))

    def test_TC_10_email_login_sucess(self):
        '''TC-10: 이메일계정 로그인 성공 동작'''
        user = self.config['accounts']['valid_user']
        self.email_pg.enter_account_infos(email=user['email'], password=user['password'])
        self.email_pg.click_login()
        self.home_pg.in_app_popup_close()
        self.assertTrue(self.home_pg.is_home_page_displayed())

class Test_03_Home_Page(BaseOptions):
    def setUp(self):
        options = self.get_common_options()
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        self.login_pg = LoginPage(self.driver)
        self.email_pg = EmailLoginPage(self.driver)
        self.home_pg = HomePage(self.driver)

        user = self.config['accounts']['valid_user']
        self.login_pg.click(self.login_pg.EMAIL_LOGIN_TEXT)
        self.email_pg.enter_account_infos(email=user['email'], password=user['password'])
        self.email_pg.click_login()

    def test_TC_11_home_ui(self):
        '''TC-11: 계정 로그인 이후, 홈 화면 UI 확인'''
        self.home_pg.in_app_popup_close()
        self.assertTrue(self.home_pg.is_home_page_displayed())

class Test_100_Login_Failure_Limits(BaseOptions):
    def setUp(self):
        options = self.get_common_options()
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        self.login_pg = LoginPage(self.driver)
        self.email_pg = EmailLoginPage(self.driver)
        self.login_pg.click(self.login_pg.EMAIL_LOGIN_TEXT)

    def test_TC_12_invalid_password_toast(self):
        '''TC-12: 유효하지않은 비밀번호 입력시, 이메일 계정 로그인 실패'''
        user = self.config['accounts']['temp_user']
        self.email_pg.enter_account_infos(email=user['email'], password='1234')
        self.email_pg.click_login()
        self.assertTrue(self.email_pg.check_toast_message(self.email_pg.INVALID_PW_TOAST))

    def test_TC_13_login_blocked_toast(self):
        '''TC-13: 유효하지않은 비밀번호 10회 이상 입력시, 이메일 계정 로그인 제한 동작'''
        user = self.config['accounts']['block_test']
        wrong_pw = 'wrong_123'
        self.email_pg.enter_account_infos(email=user['email'])
        for i in range(10):
            self.email_pg.enter_account_infos(password=wrong_pw)
            self.email_pg.click_login()
            time.sleep(1)
        self.assertTrue(self.email_pg.check_toast_message(self.email_pg.LIMMIT_LOGIN_TOAST))
