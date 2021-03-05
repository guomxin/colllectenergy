import uiautomator2 as u2
import time
import random
#d = u2.connect()  # 有线连接，手机需要插电脑上 
d = u2.connect("192.168.0.27") # 通过无线连接，电脑和手机需要在同一个局域网内，并且需要先用有线的方式做过初始化

print("打开支付宝")
d.app_start("com.eg.android.AlipayGphone")
time.sleep(2) # 根据具体手机情况，休眠2s等待支付宝完全启动

print("打开蚂蚁森林，等待5s……")
d(text="蚂蚁森林").click()
time.sleep(3) # 根据具体手机情况，看完全进入蚂蚁森林的时间   

def collectEnergy(cnt):
    print("开始第%d次收能量..." % cnt)

    # 开始扫描点击有能量出现的区域  
    for x in range(150,1000,150):
        for y in range(600,900,150):
            d.long_click(x + random.randint(10,20), y + random.randint(10,20), 0.1)
            time.sleep(0.01)

cnt = 1
while True:
    collectEnergy(cnt)
    a = d.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds 
    d.click(1000, a[3]-80) # "找能量"按钮的坐标 

    # 如果出现“返回我的森林”说明已经没有能量可收，结束
    if d.xpath('//*[@text="返回我的森林"]').click_exists(timeout=2.0):
        break
    cnt += 1
print("###结束###")