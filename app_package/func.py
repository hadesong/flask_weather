#coding:utf-8
import urllib , urllib2 , json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def api_func(url , cityname):
    apikey = 'c06bb5cfaf3090c62f70c52450998ec7'
    cn = cityname
    u = url
    req = urllib2.Request(url)
    req.add_header("apikey" , apikey)
    resp = urllib2.urlopen(req)
    #content = resp.read().decode('unicode_escape')
    content = resp.read()
    if(content):
        return content
    else:
        re = '''{"errNum":-1}'''
        return re



null ='None'
def seven_data(content):
    global null
    dict_content = eval(content)
    if dict_content['errMsg'] != "success":
        html = '''
<div class="alert alert-warning alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>哎呦  !</strong> 这个城市名称好像不对呀....
</div>
        '''
        return html
    else:
        info = {
        "city": dict_content['retData']['city'].decode('unicode_escape'),
        "data": dict_content['retData']['today']['date'].decode('unicode_escape'),
        "week": dict_content['retData']['today']['week'].decode('unicode_escape'),
        "curTemp": dict_content['retData']['today']['curTemp'].decode('unicode_escape'),
        "aqi":dict_content['retData']['today']['aqi'].decode('unicode_escape'),
        "fengxiang": dict_content['retData']['today']['fengxiang'].decode('unicode_escape'),
        "fengli": dict_content['retData']['today']['fengli'].decode('unicode_escape'),
        "hightemp": dict_content['retData']['today']['hightemp'].decode('unicode_escape'),
        "lowtemp": dict_content['retData']['today']['lowtemp'].decode('unicode_escape'),
        "type": dict_content['retData']['today']['type'].decode('unicode_escape'),

        "gm_info": dict_content['retData']['today']['index'][0]['details'].decode('unicode_escape'),
        "fs_info": dict_content['retData']['today']['index'][1]['details'].decode('unicode_escape'),
        "cy_info": dict_content['retData']['today']['index'][2]['details'].decode('unicode_escape'),
        "yd_info": dict_content['retData']['today']['index'][3]['details'].decode('unicode_escape'),
        "xc_info": dict_content['retData']['today']['index'][4]['details'].decode('unicode_escape'),
        "ls_info": dict_content['retData']['today']['index'][5]['details'].decode('unicode_escape'),

        "for_0": dict_content['retData']['forecast'][0]['date'].decode('unicode_escape'),
        "for_0_high": dict_content['retData']['forecast'][0]['hightemp'].decode('unicode_escape'),
        "for_0_low": dict_content['retData']['forecast'][0]['lowtemp'].decode('unicode_escape'),

        "for_1": dict_content['retData']['forecast'][1]['date'].decode('unicode_escape'),
        "for_1_high": dict_content['retData']['forecast'][1]['hightemp'].decode('unicode_escape'),
        "for_1_low": dict_content['retData']['forecast'][1]['lowtemp'].decode('unicode_escape'),

        "for_2": dict_content['retData']['forecast'][2]['date'].decode('unicode_escape'),
        "for_2_high": dict_content['retData']['forecast'][2]['hightemp'].decode('unicode_escape'),
        "for_2_low": dict_content['retData']['forecast'][2]['lowtemp'].decode('unicode_escape'),

        "for_3": dict_content['retData']['forecast'][3]['date'].decode('unicode_escape'),
        "for_3_high": dict_content['retData']['forecast'][3]['hightemp'].decode('unicode_escape'),
        "for_3_low": dict_content['retData']['forecast'][3]['lowtemp'].decode('unicode_escape'),
        }
        html = '''
<ul class="list-group" >
  <li class="list-group-item active"><h2>%s</h2>&nbsp;&nbsp;%s&nbsp;&nbsp;%s</li>
  <li class="list-group-item"><b>当前温度 : </b><h1 style="font-color:blue">%s</h1>风向 : %s&nbsp;&nbsp;风力 : %s&nbsp;&nbsp;PM值 : %s</li>
  <li class="list-group-item"><b>感冒提示 : </b>%s</li>
  <li class="list-group-item"><b>防晒提示 : </b>%s</li>
  <li class="list-group-item"><b>穿衣信息 : </b>%s</li>
  <li class="list-group-item"><b>运动信息 : </b>%s</li>
  <li class="list-group-item"><b>洗车信息 : </b>%s</li>
  <li class="list-group-item"><b>晾晒信息 : </b>%s</li>
  <li class="list-group-item active"></li>
</ul>
        '''%(info['city'],info['data'] , info['week'] , info['curTemp'] , info['fengxiang'] , info['fengli'] , info['aqi'] ,
            info['gm_info'] , info['fs_info'] , info['cy_info'] , info['yd_info'] , info['xc_info'] , 
            info['ls_info'])

        part1= '''
    <div id="main" style="width:80%;height:400px ;margin:0 auto" ></div>
    <script type="text/javascript">
        var myChart = echarts.init(document.getElementById('main'));
        var option = {
    title: {'''

        part11='''text: '%s未来四天天气预报'
        '''%info['city']
        part12='''
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:[ '最高温度','最低温度']
    },
    grid: {
        left: '3%',
        right: '7%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap :true,
            '''
        part2='''data:['%s','%s','%s','%s']'''%(info['for_0'],info['for_1'],info['for_2'],info['for_3'],)
        part3='''
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        
      
        {
            name:'最高温度',
            type:'line',
            label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
            '''
        part4='''data:[%s , %s , %s , %s]'''%(info['for_0_high'][:-1],info['for_1_high'][:-1],info['for_2_high'][:-1],info['for_3_high'][:-1],)
        part5='''
        },
        {
            name:'最低温度',
            type:'line',
            label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
            '''
        part6='''data:[%s , %s , %s , %s]'''%(info['for_0_low'][:-1],info['for_1_low'][:-1],info['for_2_low'][:-1],info['for_3_low'][:-1],)
        part7 = '''
        }
    ]
};

        myChart.setOption(option);
    </script>
'''
        chart = part1+ part11+ part12+part2+part3+part4+part5+part6+part7
        div = '''
        <div style="margin:0 auto">
%s
%s
</div>
        '''%(chart , html)
        return div


## 使用ajax 返回一段js+html代码  但是i不执行 .....
        charts =''' 
    <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <!-- 引入 echarts.js -->
</head>
<body>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="main" style="width:50%;height:400px;"></div>
    <script type="text/javascript">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));
        // 指定图表的配置项和数据
        var option = {
    title: {
        text: '未来四天天气预报'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:[ '最高温度','最低温度']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : true,
            data : ['1','2','3','4' ]
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        
      
        {
            name:'直接访问',
            type:'line',
            stack: '总量',
            data:[1 , 2, 3 , 4]
        },
        {
            name:'搜索引擎',
            type:'line',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
            data:[3 , 5 , 1 , 7]
        }
    ]
};

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
</body>
</html>
'''
