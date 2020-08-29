# coding=UTF-8
import requests
import re
from bs4 import BeautifulSoup
import json
import os

if __name__ == '__main__':

    url = 'http://www.iqiyi.com/a_19rrhb3xvl.html'

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
        strLi = str(liSoup)
        strLi = strLi.replace('\r\n','').replace('\n','').replace(' ','')
        #print(strLi)
        info = re.search('''<lidata-albumlist-elem="playItem"data-order="(.*?)"\
data-order-name=""style=""><divclass="site-piclist_pic"><aclass="site-piclist_pic_link"data-pb="c1=4"href="//(.*?)"\
rseat="708222_sub1_tuwenplay"target="_blank"title="(.*?)"><imgalt="''',strLi)
        #print(info.group(1),info.group(2),info.group(3))
        video = '<button type="button" onclick="onPlay(\'' + info.group(2) + '\')"  style="width:300px">' + info.group(1) + " " + info.group(3) + '</button>\n'
        videolist = video + videolist

    fileName = "one_peace.html"
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
  <title>    one peace    </title>
</head>
<body onload="onload()" bgcolor=#000000>
<table  width="100%" align="center" height="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
    <iframe src="" name="play" id="play" width="100%" align="center" height="100%" frameborder="0" marginheight="0" marginwidth="0" scrolling="no"></iframe>
    <div class="form-group form-group-lg input-group input-group-lg">
        <form method="post" action="">
        <select name="jk" id="jk" size=1 onchange="fnChange()" style="width:100px;height:30px">
                <option value="https://okjx.cc/?url=" selected>ok解析</option>
                <option value="http://www.vipjiexi.com/yun.php?url=">线路1</option>
                <option value="http://api.1008net.com/v.php?url=">线路2</option>
                <option value="http://api.nepian.com/ckparse/?url=">线路3</option>
                <option value="http://player.jidiaose.com/supapi/iframe.php?v=">线路4</option>
                <option value="http://api.pucms.com/index.php?url=">线路5</option>
                <option value="http://api.wlzhan.com/sudu/?url=">线路6</option>
                <option value="http://www.0335haibo.com/yun.php?url=">线路7</option>
                <option value="http://yun.mt2t.com/yun?url=">线路8</option>
                <option value="http://y.mt2t.com/lines?url=">线路9</option>
                <option value="http://www.0335haibo.com/yun.php?url=">线路10</option>
                <option value="http://www.sfsft.com/video.php?url=">线路11</option>
                <option value="http://www.82190555.com/video.php?url=">线路12</option>
                <option value="http://2.jx.72du.com/video.php?url=">线路13</option>
                <option value="http://www.97panda.com/kkflv/index.php?url=">线路14</option>
                <option value="http://jx.vgoodapi.com/jx.php?url=">线路15</option>
                <option value="http://www.dgua.xyz/webcloud/?url=">线路16</option>
                <option value="http://api.91exp.com/svip/?url=">线路17</option>
                <option value="http://vip.jlsprh.com/index.php?url=">线路18</option>
                <option value="http://api.xfsub.com/index.php?url=">线路19</option>
                <option value="http://jiexi.071811.cc/jx.php?url=">线路20</option>
                <option value="http://jiexi.92fz.cn/player/vip.php?url=">线路21</option>
                <option value="http://api.baiyug.cn/vip/index.php?url=">线路22</option>
                <option value="http://api.662820.com/xnflv/index.php?url=">线路23</option>
                <option value="http://www.82190555.com/index/qqvod.php?url=">线路24</option>
                <option value="http://yyygwz.com/index.php?url=">线路25</option>
                <option value="http://www.97panda.com/kkflv/index.php?url=">线路26</option>
                <option value="http://jx.api.163ren.com/vod.php?url=">线路27</option>
                <option value="http://lookxw.com/yingzi/?url=">线路28</option>
                <option value="http://www.0335haibo.com/tong.php?url=">线路29</option>
                <option value="http://www.wmxz.wang/video.php?url=">线路30</option>
                <option value="http://api.97kn.com/?url=">线路31</option>
                <option value="https://aikanapi.duapp.com/odflv105/index.php?url=">线路32</option>
                <option value="http://v.buy360.vip/wwcx/index.php?url=">线路33</option>
                <option value="http://api.lequgirl.com/?url=">线路34</option>
                <option value="https://jxapi.nepian.com/ckparse/?url=">线路35</option>
                <option value="http://91k.co/play.php?url=">线路36</option>
                <option value="http://www.52jiexi.com/yun.php?url=">线路37</option>
                <option value="http://mt2t.com/yun?url=">线路38</option>
                <option value="http://000o.cc/jx/ty.php?url=">线路39</option>
                <option value="http://yyygwz.com/index.php?url=">线路40</option>
                <option value="http://vipjiexi.com/vip.php?url=">线路41</option>
                <option value="http://www.wmxz.wang/video.php?url=">线路42</option>
                <option value="http://jx.ck921.com/?url=">线路43</option>
                <option value="http://s1y2.com/?url=">线路44</option>
                <option value="http://www.ou522.cn/t2/1.php?url=">线路45</option>
                <option value="http://jx.xuanpianwang.com/parse?url=">线路46</option>
                <option value="https://apiv.ga/magnet/">线路47</option>
                <option value="http://jiexi.92fz.cn/player/vip.php?url=">线路48</option>
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
    <div class="form-group form-group-lg input-group input-group-lg">
        buttonlist
    </div>
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
    htmlContent = htmlContent.replace("buttonlist",videolist)

    file.write(htmlContent)    
    file.close()
    os.startfile(fileName)