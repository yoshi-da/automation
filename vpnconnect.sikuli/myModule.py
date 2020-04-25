def getepass(url,username,prefix,row,col):
    import requests
    from bs4 import BeautifulSoup

    # set parameters
    url = url
    username = username
    prefix = prefix
    row = row  # 1-8  
    col = col # 1-13

    # get HTML
    urlparams = {'USERNAME':username}
    res = requests.get(url, params=urlparams)
    soup = BeautifulSoup(res.text, 'html.parser')

    # check HTTP response status code
    code = res.status_code
    assert code == 200, "code should be '200'"

    # check HTML title
    title = soup.title.string
    assert title=="ePass", "title should be 'ePass'"

    # get data from target tag and extract numbers.
    # target tag is tail CSS selector "td".
    # if HTML format chnaged, target tag maybe changed.
    data = soup.find_all("td")[-1] 
    numbers = data.text.replace(" ","").replace("\n","")

    # check length of numbers
    length = len(numbers)
    assert length == 128, "length should be '128'"

    # generate password 
    s = (row-1)*16+col-1
    e = s + 4
    password = prefix + str(numbers[s:e])

    return password

