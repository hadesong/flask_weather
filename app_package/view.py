#coding:utf-8
from app_package import app , func
from flask import render_template ,request


@app.route('/')
@app.route('/index')
def index():
    a = app.config['TEST']
    return render_template('index.html')


'''
@app.route('/search_city' , methods =['POST' ])   
def search_city():
    cityname = request.form.get('cityname').encode('utf-8')
    url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=%s'%cityname
    s = func.api_func(url , cityname)
    return func.city_data(s)
'''
#暂时用不到 的路由....
@app.route('/search_weather' , methods =['POST' ])   
def search_weather():
    cityname = request.form.get('cityname').encode('utf-8')
    url = 'http://apis.baidu.com/apistore/weatherservice/cityname?cityname=%s'%cityname
    s = func.api_func(url , cityname)
    return s



@app.route('/search_seven' , methods =['POST' ])   
def search_seven():
    cityname = request.form.get('cityname').encode('utf-8')
    url = 'http://apis.baidu.com/apistore/weatherservice/recentweathers?cityname=%s'%cityname
    s = func.api_func(url , cityname)
    return func.seven_data(s)



