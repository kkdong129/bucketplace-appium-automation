from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):
    # 로케이터
    # 인앱 팝업
    DONT_SHOW_TODAY_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="다시 보지 않기"]')
    POPUP_CLOSE = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]')

    # 상단 영역 아이콘
    LINE3_ICON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Line3Horizontal icon"]')
    SEARCH_FIELD = (AppiumBy.XPATH, '//android.widget.EditText/android.view.View')
    BELL_ICON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Bell icon"]')
    BOOKMARK_ICON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Bookmark icon"]')
    CART_ICON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Cart icon"]')

    # 하단 영역 메뉴
    WRITING_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@text="글쓰기"]')
    TAP_HOME = (AppiumBy.XPATH, '(//android.widget.TextView[@text="홈"])[2]')
    TAP_COMMUNITY = (AppiumBy.XPATH, '//android.widget.TextView[@text="커뮤니티"]')
    TAP_SHOP = (AppiumBy.XPATH, '//android.widget.TextView[@text="쇼핑"]')
    TAP_LIFE = (AppiumBy.XPATH, '//android.widget.TextView[@text="인테리어/생활"]')
    TAP_PROFILE = (AppiumBy.XPATH, '//android.widget.TextView[@text="마이페이지"]')

    def is_home_page_displayed(self):
        '''로그인 성공 후 홈 화면 확인'''
        results = [
            self.is_displayed(self.LINE3_ICON),
            self.is_displayed(self.SEARCH_FIELD),
            self.is_displayed(self.BELL_ICON),
            self.is_displayed(self.BOOKMARK_ICON),
            self.is_displayed(self.CART_ICON),
            self.is_displayed(self.WRITING_BTN),
            self.is_displayed(self.TAP_HOME),
            self.is_displayed(self.TAP_COMMUNITY),
            self.is_displayed(self.TAP_SHOP),
            self.is_displayed(self.TAP_LIFE),
            self.is_displayed(self.TAP_PROFILE)
        ]
        # 모든 요소가 True(표시됨)여야 True 반환
        return all(results)

    def in_app_popup_close(self):
        '''인앱 팝업 닫기'''
        self.close_popup_if_exists(self.POPUP_CLOSE)
