import requests

def test_login():
    global headers
    url="http://localhost:82/dev-api/login"
    body={"username":"admin","password":"admin123"}
    res=requests.post(url,json=body)
    assert res.status_code == 200,"登入失败"
    headers={"Authorization":"Bearer "+res.json()["token"]}
    print("登录成功，header获取完成：", headers)
