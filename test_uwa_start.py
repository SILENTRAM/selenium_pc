import pytest
import time,os
from selenium import webdriver
import requests

Debug =True
#time.sleep()
#函数和类，类一定是() ,函数遇到@property，然后这个函数并且在IDE推荐不是用methods
#函数当成变量用
class TestUWA_START(): #<---继承

    def setup_class(self): #100个任务 def test >pytest
        self.driver = webdriver.Chrome() #methods
        self.driver.get("https://www.uwa4d.com/")
        self.driver.implicitly_wait(5.3)

    def teardown_class(self):
        self.driver.quit()

    #css选择器
    def test_index_html(self):
        """
        判断进入到了官网页面，元素正确
        :return:
        """
        assert "https://www.uwa4d.com" in self.driver.current_url
        link_login_ele = self.driver.find_element_by_xpath('//*[@id="header-container"]/div/div/div[2]/ul[2]/a')
        if link_login_ele:
            assert bool(link_login_ele) == True
        else:
            raise Exception("元素找不到")

    def test_html_logo(self):
        """
        判断官网页面的logo存在
        :return:
        """
        logo_ele = self.driver.find_element_by_xpath('//*[@id="header-container"]/div/div/div[1]/a/img')
        if not logo_ele:#bool(logo_ele)
            raise Exception("元素找不到")
        #if Debug:time.sleep(2)
        pic_ele= logo_ele.get_attribute("src")
        if pic_ele:
            #接口调用这个pic_ele的结果看他的返回。
            #if Debug: print("test_html_logo--->验证attribute",pic_ele)
            assert requests.get(pic_ele).status_code == 200
            assert ".png" in pic_ele
            #if Debug:time.sleep(2)

    def test_first_page(self):
        """
        use:验证“首页”按钮
        :return:
        """
        first_page_ele = self.driver.find_element_by_link_text("首页")
        if first_page_ele:
            href_ele = first_page_ele.get_attribute("href")
            assert "index" in href_ele


     def test_get_field_func(self):
        """
        use:验证“功能”按钮
        :return:
        """
        func_ele = self.driver.find_element_by_link_text("功能")
        if not func_ele:
            raise Exception("元素找不到")
        func_button_ele = func_ele.get_attribute("href")
        if func_button_ele:
            assert requests.get(func_button_ele).status_code == 200
            assert "javascript:void(0)" in func_button_ele


    def test_get_field_first_func(self):
        """
        use:验证“功能”下拉栏中“性能诊断与优化”按钮
        :return:
        """
        func_ele = self.driver.find_element_by_xpath('//*[@id="feature_dropdown"]/a')
        if not func_ele:
            raise Exception("元素找不到")
        func_ele.click()
        func_ele_below_first_button = self.driver.find_element_by_xpath('//*[@id="feature_dropdown"]/ul/li[1]/a')
        if not func_ele_below_first_button:
            raise Exception("元素找不到")
        first_button_ele = func_ele_below_first_button.get_attribute("href")
        if first_button_ele:
            assert requests.get(first_button_ele).status_code == 200                            
            assert "feature" in first_button_ele


    def test_get_field_second_func(self):
        """
        use:验证“功能”下拉栏中“资源监测与分析”按钮
        :return:
        """
        func_ele = self.driver.find_element_by_xpath('//*[@id="feature_dropdown"]/a')
        if not func_ele:
            raise Exception("元素找不到")
        func_ele.click()
        func_ele_below_second_button = self.driver.find_element_by_xpath('//*[@id="feature_dropdown"]/ul/li[2]/a')
        if not func_ele_below_second_button:
            raise Exception("元素找不到")
        second_button_ele = func_ele_below_second_button.get_attribute("href")
        if second_button_ele:
            assert requests.get(second_button_ele).status_code == 200
            assert "assetbundle" in second_button_ele
            

    def test_get_field_third_func():
        """
        use:验证“功能”下拉栏中“Game Opitimization ToolKit”按钮
        :return:
        """
        func_ele = self.driver.find_element_by_xpath('//*[@id="feature_dropdown"]/a')
        if  not func_ele:
            raise Exception("元素找不到")
        func_ele.click()
        func_ele_below_third_button = self.driver.find_element_by_xpath('//*[@id="feature_dropdown"]/ul/li[3]/a')
        if not func_ele_below_third_button:
            raise Exception("元素找不到")
        third_button_ele = func_ele_below_third_button.get_attribute("href")
        if third_button_ele:
            assert requests.get(third_button_ele).status_code == 200
            assert "uwagot" in third_button_ele


    def test_get_field_qa(self):
        """
        use:验证“问答”按钮
        retrun:
        """
        QA_button = self.driver.find_element_by_xpath("//*[@id="header-container"]/div/div/div[2]/ul[1]/li[3]/a")
        if not QA_button:
            raise Exception("元素找不到")
        QA_button_ele = QA_button.get_attribute("href")
        if QA_button_ele:
            assert requests.get(QA_button_ele).status_code == 200
            assert "https://answer.uwa4d.com" in QA_button_ele


 def test_get_field_open_source_library(self):
        """
        use:验证“开源库”按钮
        retrun:
        """
        OSL_button = self.driver.find_element_by_xpath("//*[@id="header-container"]/div/div/div[2]/ul[1]/li[4]/a")
        if not OSL_button:
            raise Exception("元素找不到")
        OSL_button_ele = OSL_button.get_attribute("href")
        if OSL_button_ele:
            assert requests.get(OSL_button_ele).status_code == 200
            assert "https://lab.uwa4d.com" in OSL_button_ele


 def test_get_field_blog(self):
        """
        use:验证“博客”按钮
        retrun:
        """
        Blog_button = self.driver.find_element_by_xpath("//*[@id="header-container"]/div/div/div[2]/ul[1]/li[5]/a")
        if not Blog_button:
            raise Exception("元素找不到")
        Blog_button_ele = Blog_button.get_attribute("href")
        if Blog_button_ele:
            assert requests.get(Blog_button_ele).status_code == 200
            assert "https://lab.uwa4d.com" in Blog_button_ele


 def test_get_field_price(self):
        """
        use:验证“价格”按钮
        retrun:
        """
        Price_button = self.driver.find_element_by_xpath("//*[@id="header-container"]/div/div/div[2]/ul[1]/li[6]/a")
        if not Price_button:
            raise Exception("元素找不到")
        Price_button_ele = Price_button.get_attribute("href")
        if Price_button_ele:
            assert requests.get(Price_button_ele).status_code == 200
            assert "price" in Price_button_ele


 def test_get_field_cooperate(self):
        """
        use:验证“价格”按钮
        retrun:
        """
        Cooperate_button = self.driver.find_element_by_xpath("//*[@id="header-container"]/div/div/div[2]/ul[1]/li[7]/a")
        if not Price_button:
            raise Exception("元素找不到")
        Cooperate_button_ele = Cooperate_button.get_attribute("href")
        if Cooperate_button_ele:
            assert requests.get(Cooperate_button_ele).status_code = 200
            assert "activity-us" in Cooperate_button_ele


 def test_get_field_download(self):
        """
        use:验证“下载”按钮并点击“下载”按钮
        return:
        """
        Download_button = self.driver.find_element_by_xpath('//*[@id="header-container"]/div/div/div[2]/ul[1]/li[8]/a')
        if not Download_button:
            raise Exception("元素找不到")
        Download_button_ele = Download_button.get_attribute("href")
        if Download_button_ele:
            assert requests.get(Download_button_ele).status_code == 200
            assert "download" in Download_button_ele
        Download_button.click()


 def test_download_html(self):
        """
        use:判断进入到了下载页面，windowspc版本元素正确，点击下载
        :return:
        """
        assert "https://www.uwa4d.com/#download" in self.driver.current_url
        link_windowspc_button = self.driver.find_element_by_xpath('//*[@id="content-container"]/div/div/div[3]/div[1]/div[2]/div[1]/a[3]')
        if not link_windowspc_button:
            raise Exception("元素找不到")
        windowspc_button_ele = link_windowspc_button.get_attribute("href")
        if windowspc_button_ele:
            assert requests.get(windowspc_button_ele).status_code == 200
            assert "https://uwa-download.oss-cn-beijing.aliyuncs.com/plugins/standalone/Windows%20v1.2.1.zip" in windowspc_button_ele
        link_windowspc_button.click()





      
