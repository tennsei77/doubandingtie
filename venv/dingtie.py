# 豆瓣具体帖子
url = "https://www.douban.com/group/topic/129122199/"
# 豆瓣具体帖子回复的接口，格式是帖子链接+/add_comment
comment_url = url + "/add_comment"
cookie = 'cookie'
referer = url
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
headers = {
    "Host": "www.douban.com",
    "Referer": referer,
    'User-Agent': agent,
    "Cookie": cookie
}
params = {
    "rv_comment": '?',
    "ck": re.findall("ck=(.*?);", headers["Cookie"])[-1],
    'start': '0',
    'submit_btn': '发送'
}
response = requests.post(comment_url, headers=headers, allow_redirects=False,
                         data=params, verify=False)
