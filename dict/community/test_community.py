import requests
import common.login.admin as admin

headers = {}

def test_addCommunity():
    url="http://localhost:82/dev-api/dict/community"
    body={
    "name": "汤1",
    "alias": "汤臣一品",
    "firstLetter": "T",
    "streetCode": 1,
    "streetName": "陆家嘴街道",
    "roadCode": 441223001010,
    "roadName": "花园石桥路",
    "address": "花园石桥路28弄",
    "longitude": 121.5064,
    "latitude": 31.2364,
    "boundaryPoints": "[[121.506,31.236],[121.507,31.237]]",
    "entranceImg": "https://example.com/entrance.jpg",
    "parkingEntranceImg": "https://example.com/parking.jpg",
    "gardenImg": "https://example.com/garden.jpg",
    "sportAreaImg": "https://example.com/sport.jpg",
    "appearanceImg": "https://example.com/appearance.jpg",
    "serviceCenterImg": "https://example.com/service.jpg",
    "noticeBoardImg": "https://example.com/notice.jpg",
    "plotArea": 50000.00,
    "constructionArea": 150000.00,
    "plotRatio": 2.8,
    "greenRate": 35.5,
    "totalBuildings": 12,
    "totalHouseholds": 800,
    "buildType": "板楼",
    "structureForm": "钢筋混凝土结构",
    "finishYear": "2005年",
    "usageTerm": "70年",
    "developer": "汤臣集团有限公司",
    "propertyCompany": "汤臣物业",
    "heatingMode": "集中供暖",
    "gasType": "管道天然气",
    "waterSupply": "市政供水",
    "powerSupply": "市政供电",
    "parkingRatio": "1:1.5",
    "hasElevator": "Y",
    "propertyFee": "12.8元/㎡/月",
    "parkingFee": 1200.00,
    "waterFee": 3.45,
    "elecFee": 0.56,
    "gasFee": 2.80,
    "deptId": 221,
    "status": "1"
    }

    res=requests.post(url,json=body,headers=headers)
    assert res.status_code == 200,"操作失败"
    print("返回结果：" ,res.json())
    print("msg：" , res.json()["msg"])

if __name__ == '__main__':
    test_login()
    test_addCommunity()