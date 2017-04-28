# 图片链接列表，标题 
# url是详情页链接 
def getPiclink(url): 
    sel = html.fromstring(requests.get(url).content) 
    # 图片总数 倒数第二项里 
    total = sel.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0] 
    # 标题 
    title = sel.xpath('//h2[@class="main-title"]/text()')[0] 

    # 接下来的链接放到这个列表 
    jpgList = [] 
    
    for i in range(int(total)): 
        # 每一页 
        link = '{}/{}'.format(url, i+1) 
        s = html.fromstring(requests.get(link).content) 
        # 图片地址在src标签中 
        jpg = s.xpath('//div[@class="main-image"]/p/a/img/@src')[0] 
        # 图片链接放进列表 
        jpgList.append(jpg) 

    return title, jpgList