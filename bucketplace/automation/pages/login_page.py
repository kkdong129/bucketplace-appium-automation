from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    # 로케이터 정의
    LOGO_IMG = (AppiumBy.ID, 'net.bucketplace:id/logo')
    GUIDE_IMG = (AppiumBy.ID, 'net.bucketplace:id/guideImage')
    KAKAO_QUICK_LOGIN_BTN = (AppiumBy.ID, 'net.bucketplace:id/kakaoLoginButton')
    NAVER_LOGIN_BTN = (AppiumBy.ID, 'net.bucketplace:id/naverLoginButton')
    FACEBOOK_LOGIN_BTN = (AppiumBy.ID, 'net.bucketplace:id/facebookLoginButton')
    APPLE_LOGIN_BTN = (AppiumBy.ID, 'net.bucketplace:id/appleLoginButton')
    EMAIL_LOGIN_TEXT = (AppiumBy.ID, 'net.bucketplace:id/emailLogInText')
    EMAIL_SIGNUP_TEXT = (AppiumBy.ID, 'net.bucketplace:id/emailSignUpText')
    CS_TEXT = (AppiumBy.ID, 'net.bucketplace:id/customerServiceText')
    ORDER_CHECK = (AppiumBy.ID, 'net.bucketplace:id/anonymousOrderCheck')

    def is_login_page_displayed(self):
        '''로그인 화면 확인'''
        results = [
            self.is_displayed(self.LOGO_IMG),
            self.is_displayed(self.GUIDE_IMG),
            self.is_displayed(self.KAKAO_QUICK_LOGIN_BTN),
            self.is_displayed(self.NAVER_LOGIN_BTN),
            self.is_displayed(self.FACEBOOK_LOGIN_BTN),
            self.is_displayed(self.APPLE_LOGIN_BTN),
            self.is_displayed(self.EMAIL_LOGIN_TEXT),
            self.is_displayed(self.EMAIL_SIGNUP_TEXT),
            self.is_displayed(self.CS_TEXT),
            self.is_displayed(self.ORDER_CHECK)
        ]
        # 모든 요소가 True(표시됨)여야 True 반환
        return all(results)
