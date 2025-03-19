import requests
import os
import re

def checkin():
    # 从环境变量获取cookie和formhash
    cookie = os.environ.get('COOKIE')
    formhash = os.environ.get('FORMHASH')
    
    # 从环境变量获取网站地址
    website = os.environ.get('WEBSITE', 'www.gamemale.com')
    
    # 处理网站地址，移除可能的http://或https://前缀和尾部斜杠
  
    # 移除协议前缀
    website = re.sub(r'^https?://', '', website)
    # 移除尾部斜杠
    website = website.rstrip('/')
  
    
    # 构建完整URL
    base_url = f"https://{website}/k_misign-sign.html"
    
    # 检查必要环境变量
    if not cookie:
        print("错误: 未设置COOKIE环境变量")
        return None
    
    # 准备参数
    params = {
        "operation": "qiandao",
        "format": "button",
        "formhash": formhash,
        "inajax": 1,
        "ajaxtarget": "midaben_sign"
    }
    
    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Referer": f"https://{website}/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": cookie
    }
    
    try:
        # 发送GET请求
        print(f"正在访问: {base_url}")
        response = requests.get(base_url, params=params, headers=headers)
        
        # 确保使用正确的编码
        response.encoding = response.apparent_encoding
        
        # 打印响应状态和内容
        print(f"状态码: {response.status_code}")
        print("响应内容:")
        print(response.text)
        
        return response.text
    except Exception as e:
        print(f"请求出错: {e}")
        return None

if __name__ == "__main__":
    # 直接执行签到
    checkin()
