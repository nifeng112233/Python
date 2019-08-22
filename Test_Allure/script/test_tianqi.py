import pytest
import requests
import allure
from Test_Allure.Commonlibs.ReadExc import Read_Ex


class Test_Tq:
    @allure.step(title="天气接口测试")
    @allure.severity('blocker')
    def test_01(self):
        allure.attach("相应的描述")
        res = Read_Ex()
        data = res.read_excel()
        for i in data:
            url = "http://v.juhe.cn/weather/index"
            para = {"cityname":i["cityname"], "key":i["key"]}
            res = requests.get(url, params=para)
            r = res.json()
            assert r["error_code"] == int(i["exp"])

