# coding=UTF-8
import requests
import re
from bs4 import BeautifulSoup
import json
import os
import sys

reload(sys)
sys.setdefaultencoding("UTF-8")

if __name__ == '__main__':
    #海贼王
    #url = 'http://www.iqiyi.com/a_19rrhb3xvl.html'
    videoName = sys.argv[1]
    url = sys.argv[2]
    print(videoName,url)
    headers = {
        'Access-Control-Allow-Credentials': 'true',
        'Cache-Control': 'max-age=900',
        'Content-Encoding': 'gzip',
        'Content-Language': 'zh-CN',
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Referer': 'http://so.iqiyi.com/so/q_%E8%88%AA%E6%B5%B7%E7%8E%8B?source=default&sr=12476510953584158&ssrt=20200829152144709&ssra=313d3e6029a7281b2ce992131f8f86ac',
        'Upgrade-Insecure-Requests': '1'
    }
    target = requests.get(url=url,headers=headers).text

    soup = BeautifulSoup(target,'html.parser')
    returnSoup = soup.find_all("ul", attrs={"class": "site-piclist site-piclist-180101"})[0]
    listSoup = returnSoup.find_all("li", attrs={"data-albumlist-elem":"playItem"})

    videolist = ""
    for liSoup in listSoup:
        linkSoup = liSoup.find("a", attrs={"class": "site-piclist_pic_link"})
        idx = liSoup.get("data-order")
        link = linkSoup.get("href")
        title = linkSoup.get("title")
        #print(idx,link,title)
        video = '<button align="center" type="button" onclick="onPlay(\'https:' + link + '\')">' +idx+ '</button>\n'
        videolist = videolist + video

    fileName = videoName+".html"
    file = open(fileName,"w")
    htmlContent = '''
    <html>
<head>
  <SCRIPT LANGUAGE="JavaScript">
        var curUrl = ""
        function fnChange(){
            onPlay(curUrl);
        }
        function onPlay(url){
                curUrl = url
                var oJK = document.getElementById("jk");
                var sJK=oJK.options[oJK.selectedIndex].value;
                var oWin = document.getElementById("play");
                oWin.src=sJK + url;
                var curJxTxt = document.getElementById("curJx")
                curJxTxt.value = "当前解析地址：" + sJK + url;
        }
        function manPlay(){
            var url = document.getElementById("u");
            onPlay(url.value);
        }
  </SCRIPT>
  <title>    titleToReplace视频播放器    </title>
</head>
<body onload="onload()" bgcolor=#000000>
<table  width="100%" align="center" height="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
	<title>titleToReplace</title>
	<div class="form-group form-group-lg input-group input-group-lg">
        buttonToReplace
		<br>
    </div>
	<div class="am-panel-bd player-box">
		<iframe src="" name="play" id="play" width="100%" align="center" height="100%" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" allowTransparency="true"allowfullscreen="true"></iframe>
	</div>
    <div class="form-group form-group-lg input-group input-group-lg">
        <form method="post" action="">
        <select name="jk" id="jk" size=1 onchange="fnChange()" style="width:100px;height:30px">
                <option value="http://api.bbbbbb.me/jiexi/?url=">思古解析</option>
                <option value="https://okjx.cc/?url=" selected>ok解析</option>
                <option value="https://17kyun.com/jx.php?url=">线路1</option>
                <option value="http://17kyun.com/api.php?url=">线路2</option>
                <option value="https://2.08bk.com/?url=&url=">线路3</option>
                <option value="https://jx.idc126.net/jx/?url=">线路4</option>
                <option value="http://jx.drgxj.com/?url=">线路5</option>
        </select>
    </div>
    <div>
        <textarea id="curJx" rows="1" cols="80" style="width:600px;height:25px" readonly>当前解析地址：</textarea>
    </div>
    <div class="form-group form-group-lg input-group input-group-lg style="height:100px"> 
       <input class="form-control" id="u" type="text" style="width:500px;height:50px" value="" placeholder="请输入视频地址，如:http://v.youku.com/v_show/id_XMTY1Njc5MTgwOA==.html" /> 
       <button class="btn btn-default btn-warning" type="button" onclick="manPlay()" style="width:100px;height:50px">播放</button> 
    </div>
    <br>
    <div class="unit-100">
        <div class="language">
            <a class="btn2 btn-outline2" href="https://www.iqiyi.com/" rel="nofollow" target="_blank" style="color:#ffffffff;">进入奇艺视频</a>
            <a class="btn2 btn-outline2" href="http://www.le.com/" rel="nofollow" target="_blank"  style="color:#ffffffff;">进入乐视视频</a>
            <a class="btn2 btn-outline2" href="http://www.mgtv.com/" rel="nofollow" target="_blank" style="color:#ffffffff;">进入芒果视频</a>
            <a class="btn2 btn-outline2" href="http://www.tudou.com/" rel="nofollow" target="_blank" style="color:#ffffffff;">进入土豆视频</a>     
            <br>
            <a class="btn2 btn-outline2" href="https://v.qq.com/" rel="nofollow" target="_blank" style="color:#ffffffff;">进入腾讯视频</a>     
            <a class="btn2 btn-outline2" href="https://www.youku.com/" rel="nofollow" target="_blank" style="color:#ffffffff;">进入优酷视频</a>
            <a class="btn2 btn-outline2" href="https://tv.sohu.com/" rel="nofollow" target="_blank" style="color:#ffffffff;">进入搜狐视频</a>
            <a class="btn2 btn-outline2" href="http://www.pptv.com/" rel="nofollow" target="_blank" style="color:#ffffffff;">进入pptv视频</a>
        </div>
        <br>
    </div>
</tr>

</table>
</body>
</html>
    '''
    htmlContent = htmlContent.replace("buttonToReplace",videolist).replace("titleToReplace",videoName)

    file.write(htmlContent)    
    file.close()
    os.startfile(fileName)