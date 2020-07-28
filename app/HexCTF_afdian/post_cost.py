import time
import requests
import re
post_url = "http://love.0xctf.com:9888/api_cost0x0x.php"
daa = "cost-买超算-100000000000000000"
qq_num = [1175078221, 912309920]
sess = requests.session()

def send_cost_data(QQ,price,action,url):
    send_data = {
        "cost": '{{"QQ": "{}","price": "{}","time": "{}","action": "{}","url": "{}"}}'.format(QQ, price, round(time.time()), action, url)
    }
    res = sess.post(url = post_url, data = send_data)
    return res.text

def team_cost(msg, img_url, user_id):
    if user_id not in qq_num:
        return [False]
    if not (msg[:5]=="cost-"):
        return [False]
    msg=(msg[5:]).split("-")
    price=re.findall(r"[0-9]+.{1}[0-9]{2}",msg[1])
    if len(msg) != 2 or len(price)!=1:
        return [True,"请按照“cost-买超算-1.00”的格式"]
    return [True, send_cost_data(user_id,price[0],msg[0],img_url)]
