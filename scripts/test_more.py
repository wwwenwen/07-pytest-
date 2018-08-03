from appium import webdriver

class TestMore:

    def setup(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def test_search_number(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("123")

    def test_search_chinese(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("你好")
