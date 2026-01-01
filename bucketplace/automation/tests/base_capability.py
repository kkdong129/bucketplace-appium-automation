import unittest
import json
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

class BaseOptions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''테스트 시작 전 config 데이터를 한 번만 로드합니다.'''
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            cls.config = json.load(f)

    def get_common_options(self):
        '''모든 테스트에서 공통으로 사용하는 옵션을 정리합니다.'''
        options = UiAutomator2Options()
        options.platform_name = device['platform_name']
        options.automation_name = device['automation_name']
        options.udid = device['udid']
        options.app_package = 'net.bucketplace'
        options.app_activity = 'se.ohou.screen.splash.SplashActivity'
        options.no_reset = False
        options.set_capability(
            'appWaitActivity',
            'se.ohou.screen.main.MainActivity, se.ohou.screen.splash.SplashActivity'
        )
        options.set_capability('newCommandTimeout', 300)

        return options
