from flask import Flask, render_template, jsonify, request
from models.data import (db, ActivityStats, CouponStats, NewBuyerStats, \
    OrderByProvince, PagePath, RepeatPurchaseByTm, SkuCartNumTop3ByCate, \
    TradeStats, TradeStatsByCate, TradeStatsByTm, TrafficStatsByChannel, \
                         UserAction, UserChange, UserRetention, UserStats)
from sqlalchemy import text
from datetime import date


app = Flask(__name__)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'wang2003'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'DW'
app.config['SQLALCHEMY_DATABASE_URI'] \
    = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".\
    format(DIALECT,DRIVER,USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# 初始化数据库
db.init_app(app)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text('select 1'))
#         print(rs.fetchone())




@app.route('/insert_data')
def insert_data():
    # 数据插入
    records = [
        ActivityStats(dt=date(2024, 8, 29), activity_id='ACT001', activity_name='Summer Sale', start_date='2024-08-01', reduce_rate=12.50),
        ActivityStats(dt=date(2024, 8, 29), activity_id='ACT002', activity_name='Back to School', start_date='2024-08-15', reduce_rate=10.00),
        ActivityStats(dt=date(2024, 8, 29), activity_id='ACT003', activity_name='Black Friday', start_date='2024-11-25', reduce_rate=15.75),
        ActivityStats(dt=date(2024, 8, 28), activity_id='ACT004', activity_name='Christmas Sale', start_date='2024-12-20', reduce_rate=20.00),
        ActivityStats(dt=date(2024, 8, 28), activity_id='ACT005', activity_name='New Year Promotion', start_date='2024-12-31', reduce_rate=18.00),
        ActivityStats(dt=date(2024, 8, 27), activity_id='ACT006', activity_name='Flash Sale', start_date='2024-08-27', reduce_rate=5.00),
        ActivityStats(dt=date(2024, 8, 27), activity_id='ACT007', activity_name='Clearance Sale', start_date='2024-08-20', reduce_rate=30.00),
        CouponStats(dt=date(2024, 8, 29), coupon_id='CPN001', coupon_name='Summer Discount', start_date='2024-08-01', rule_name='满100元减10元', reduce_rate=12.50),
        CouponStats(dt=date(2024, 8, 29), coupon_id='CPN002', coupon_name='Back to School Special',start_date='2024-08-15', rule_name='满200元减20元', reduce_rate=10.00),
        CouponStats(dt=date(2024, 8, 29), coupon_id='CPN003', coupon_name='Black Friday Deal',start_date='2024-11-25', rule_name='满300元减50元', reduce_rate=15.75),
        CouponStats(dt=date(2024, 8, 28), coupon_id='CPN004', coupon_name='Christmas Coupon',start_date='2024-12-20', rule_name='满500元减100元', reduce_rate=20.00),
        CouponStats(dt=date(2024, 8, 28), coupon_id='CPN005', coupon_name='New Year Bonus', start_date='2024-12-31', rule_name='满100元减30元', reduce_rate=18.00),
        CouponStats(dt=date(2024, 8, 27), coupon_id='CPN006', coupon_name='Flash Discount', start_date='2024-08-27', rule_name='满50元减5元', reduce_rate=5.00),
        CouponStats(dt=date(2024, 8, 27), coupon_id='CPN007', coupon_name='Clearance Offer', start_date='2024-08-20', rule_name='满150元减25元', reduce_rate=30.00),
        NewBuyerStats(dt=date(2024, 8, 29), recent_days=1, new_order_user_count=150, new_payment_user_count=120),
        NewBuyerStats(dt=date(2024, 8, 29), recent_days=7, new_order_user_count=1050, new_payment_user_count=980),
        NewBuyerStats(dt=date(2024, 8, 29), recent_days=30, new_order_user_count=4500, new_payment_user_count=4200),
        NewBuyerStats(dt=date(2024, 8, 28), recent_days=1, new_order_user_count=140, new_payment_user_count=110),
        NewBuyerStats(dt=date(2024, 8, 28), recent_days=7, new_order_user_count=1000, new_payment_user_count=950),
        NewBuyerStats(dt=date(2024, 8, 28), recent_days=30, new_order_user_count=4300, new_payment_user_count=4000),
        NewBuyerStats(dt=date(2024, 8, 27), recent_days=1, new_order_user_count=130, new_payment_user_count=100),
        NewBuyerStats(dt=date(2024, 8, 27), recent_days=7, new_order_user_count=950, new_payment_user_count=900),
        NewBuyerStats(dt=date(2024, 8, 27), recent_days=30, new_order_user_count=4100, new_payment_user_count=3900),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=1, province_id='PROV001', province_name='北京市', area_code='110000', iso_code='CN-BJ', iso_code_3166_2='CN-11', order_count=150, order_total_amount=12500.50),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=7, province_id='PROV001', province_name='北京市', area_code='110000', iso_code='CN-BJ', iso_code_3166_2='CN-11', order_count=1050, order_total_amount=89000.75),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=30, province_id='PROV001', province_name='北京市', area_code='110000', iso_code='CN-BJ', iso_code_3166_2='CN-11', order_count=4550, order_total_amount=370000.00),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=1, province_id='PROV002', province_name='上海市', area_code='310000', iso_code='CN-SH', iso_code_3166_2='CN-31', order_count=120, order_total_amount=9600.25),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=7, province_id='PROV002', province_name='上海市', area_code='310000', iso_code='CN-SH', iso_code_3166_2='CN-31', order_count=950, order_total_amount=76000.80),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=30, province_id='PROV002', province_name='上海市', area_code='310000', iso_code='CN-SH', iso_code_3166_2='CN-31', order_count=4100, order_total_amount=315000.60),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=1, province_id='PROV003', province_name='广东省', area_code='440000', iso_code='CN-GD', iso_code_3166_2='CN-44', order_count=180, order_total_amount=14300.30),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=7, province_id='PROV003', province_name='广东省', area_code='440000', iso_code='CN-GD', iso_code_3166_2='CN-44', order_count=1350, order_total_amount=105000.50),
        OrderByProvince(dt=date(2024, 8, 29), recent_days=30, province_id='PROV003', province_name='广东省', area_code='440000', iso_code='CN-GD', iso_code_3166_2='CN-44', order_count=5300, order_total_amount=410000.00),
        OrderByProvince(dt=date(2024, 8, 28), recent_days=1, province_id='PROV004', province_name='浙江省', area_code='330000', iso_code='CN-ZJ', iso_code_3166_2='CN-33', order_count=90, order_total_amount=7500.75),
        OrderByProvince(dt=date(2024, 8, 28), recent_days=7, province_id='PROV004', province_name='浙江省', area_code='330000', iso_code='CN-ZJ', iso_code_3166_2='CN-33', order_count=720, order_total_amount=58000.60),
        OrderByProvince(dt=date(2024, 8, 28), recent_days=30, province_id='PROV004', province_name='浙江省', area_code='330000', iso_code='CN-ZJ', iso_code_3166_2='CN-33', order_count=3200, order_total_amount=256000.00),
        PagePath(dt=date(2024, 8, 29), recent_days=1, source='homepage', target='product_page', path_count=150),
        PagePath(dt=date(2024, 8, 29), recent_days=1, source='product_page', target='cart_page', path_count=120),
        PagePath(dt=date(2024, 8, 29), recent_days=1, source='cart_page', target='checkout_page', path_count=100),
        PagePath(dt=date(2024, 8, 29), recent_days=7, source='homepage', target='product_page', path_count=1050),
        PagePath(dt=date(2024, 8, 29), recent_days=7, source='product_page', target='cart_page', path_count=980),
        PagePath(dt=date(2024, 8, 29), recent_days=7, source='cart_page', target='checkout_page', path_count=870),
        PagePath(dt=date(2024, 8, 29), recent_days=30, source='homepage', target='product_page', path_count=4550),
        PagePath(dt=date(2024, 8, 29), recent_days=30, source='product_page', target='cart_page', path_count=4100),
        PagePath(dt=date(2024, 8, 29), recent_days=30, source='cart_page', target='checkout_page', path_count=3900),
        PagePath(dt=date(2024, 8, 28), recent_days=1, source='homepage', target='search_page', path_count=90),
        PagePath(dt=date(2024, 8, 28), recent_days=1, source='search_page', target='product_page', path_count=80),
        PagePath(dt=date(2024, 8, 28), recent_days=1, source='product_page', target='cart_page', path_count=70),
        PagePath(dt=date(2024, 8, 28), recent_days=7, source='homepage', target='search_page', path_count=720),
        PagePath(dt=date(2024, 8, 28), recent_days=7, source='search_page', target='product_page', path_count=680),
        PagePath(dt=date(2024, 8, 28), recent_days=7, source='product_page', target='cart_page', path_count=620),
        PagePath(dt=date(2024, 8, 28), recent_days=30, source='homepage', target='search_page', path_count=3200),
        PagePath(dt=date(2024, 8, 28), recent_days=30, source='search_page', target='product_page', path_count=2900),
        PagePath(dt=date(2024, 8, 28), recent_days=30, source='product_page', target='cart_page', path_count=2600),
        RepeatPurchaseByTm(dt=date(2024, 8, 29), recent_days=7, tm_id='TM001', tm_name='Brand A', order_repeat_rate=25.50),
        RepeatPurchaseByTm(dt=date(2024, 8, 29), recent_days=30, tm_id='TM001', tm_name='Brand A', order_repeat_rate=30.75),
        RepeatPurchaseByTm(dt=date(2024, 8, 29), recent_days=7, tm_id='TM002', tm_name='Brand B', order_repeat_rate=22.30),
        RepeatPurchaseByTm(dt=date(2024, 8, 29), recent_days=30, tm_id='TM002', tm_name='Brand B', order_repeat_rate=28.90),
        RepeatPurchaseByTm(dt=date(2024, 8, 29), recent_days=7, tm_id='TM003', tm_name='Brand C', order_repeat_rate=18.60),
        RepeatPurchaseByTm(dt=date(2024, 8, 29), recent_days=30, tm_id='TM003', tm_name='Brand C', order_repeat_rate=24.50),
        RepeatPurchaseByTm(dt=date(2024, 8, 28), recent_days=7, tm_id='TM004', tm_name='Brand D', order_repeat_rate=20.75),
        RepeatPurchaseByTm(dt=date(2024, 8, 28), recent_days=30, tm_id='TM004', tm_name='Brand D', order_repeat_rate=27.00),
        RepeatPurchaseByTm(dt=date(2024, 8, 28), recent_days=7, tm_id='TM005', tm_name='Brand E', order_repeat_rate=23.40),
        RepeatPurchaseByTm(dt=date(2024, 8, 28), recent_days=30, tm_id='TM005', tm_name='Brand E', order_repeat_rate=29.80),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='001', category1_name='电子产品', category2_id='00101', category2_name='手机', category3_id='0010101', category3_name='智能手机', sku_id='SKU0001', sku_name='iPhone 15', cart_num=120, rk=1),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='001', category1_name='电子产品', category2_id='00101', category2_name='手机', category3_id='0010102', category3_name='智能手机', sku_id='SKU0002', sku_name='Samsung Galaxy S23', cart_num=95, rk=2),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='001', category1_name='电子产品', category2_id='00102', category2_name='电脑', category3_id='0010201', category3_name='笔记本电脑', sku_id='SKU0003', sku_name='MacBook Pro', cart_num=88, rk=3),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='002', category1_name='家用电器', category2_id='00201', category2_name='洗衣机', category3_id='0020101', category3_name='滚筒洗衣机', sku_id='SKU0004', sku_name='小天鹅 XQG80-808', cart_num=130, rk=1),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='002', category1_name='家用电器', category2_id='00202', category2_name='冰箱', category3_id='0020201', category3_name='双开门冰箱', sku_id='SKU0005', sku_name='海尔 BCD-618WDP', cart_num=110, rk=2),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='003', category1_name='服装', category2_id='00301', category2_name='男装', category3_id='0030101', category3_name='T恤', sku_id='SKU0006', sku_name='Nike T恤', cart_num=150, rk=1),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='003', category1_name='服装', category2_id='00301', category2_name='男装', category3_id='0030102', category3_name='运动裤', sku_id='SKU0007', sku_name='Adidas 运动裤', cart_num=120, rk=2),
        SkuCartNumTop3ByCate(dt=date(2024, 8, 29), category1_id='003', category1_name='服装', category2_id='00302', category2_name='女装', category3_id='0030201', category3_name='连衣裙', sku_id='SKU0008', sku_name='Zara 连衣裙', cart_num=100, rk=3),
        TradeStats(dt=date(2024, 8, 29), recent_days=1, order_total_amount=15000.00, order_count=200, order_user_count=180, order_refund_count=5, order_refund_user_count=4),
        TradeStats(dt=date(2024, 8, 29), recent_days=7, order_total_amount=105000.00, order_count=1400, order_user_count=1200, order_refund_count=30, order_refund_user_count=25),
        TradeStats(dt=date(2024, 8, 29), recent_days=30, order_total_amount=450000.00, order_count=6000, order_user_count=5000, order_refund_count=150, order_refund_user_count=120),
        TradeStats(dt=date(2024, 8, 28), recent_days=1, order_total_amount=18000.00, order_count=220, order_user_count=200, order_refund_count=10, order_refund_user_count=8),
        TradeStats(dt=date(2024, 8, 28), recent_days=7, order_total_amount=120000.00, order_count=1500, order_user_count=1300, order_refund_count=25, order_refund_user_count=20),
        TradeStats(dt=date(2024, 8, 28), recent_days=30, order_total_amount=500000.00, order_count=6500, order_user_count=5200, order_refund_count=140, order_refund_user_count=110),
        TradeStatsByCate(dt=date(2024, 8, 29), recent_days=1, category1_id='001', category1_name='电子产品', category2_id='00101', category2_name='手机', category3_id='0010101', category3_name='智能手机', order_count=120, order_user_count=110, order_refund_count=3, order_refund_user_count=2),
        TradeStatsByCate(dt=date(2024, 8, 29), recent_days=1, category1_id='001', category1_name='电子产品', category2_id='00102', category2_name='电脑', category3_id='0010201', category3_name='笔记本电脑', order_count=80, order_user_count=70, order_refund_count=2, order_refund_user_count=1),
        TradeStatsByCate(dt=date(2024, 8, 29), recent_days=7, category1_id='001', category1_name='电子产品', category2_id='00101', category2_name='手机', category3_id='0010101', category3_name='智能手机', order_count=840, order_user_count=770, order_refund_count=15, order_refund_user_count=12),
        TradeStatsByCate(dt=date(2024, 8, 29), recent_days=7, category1_id='001', category1_name='电子产品', category2_id='00102', category2_name='电脑', category3_id='0010201', category3_name='笔记本电脑', order_count=560, order_user_count=490, order_refund_count=10, order_refund_user_count=7),
        TradeStatsByCate(dt=date(2024, 8, 29), recent_days=30, category1_id='002', category1_name='家用电器', category2_id='00201', category2_name='洗衣机', category3_id='0020101', category3_name='滚筒洗衣机', order_count=150, order_user_count=140, order_refund_count=5, order_refund_user_count=4),
        TradeStatsByCate(dt=date(2024, 8, 29), recent_days=30, category1_id='002', category1_name='家用电器', category2_id='00202', category2_name='冰箱', category3_id='0020201', category3_name='双开门冰箱', order_count=130, order_user_count=120, order_refund_count=7, order_refund_user_count=6),
        TradeStatsByCate(dt=date(2024, 8, 28), recent_days=1, category1_id='003', category1_name='服装', category2_id='00301', category2_name='男装', category3_id='0030101', category3_name='T恤', order_count=150, order_user_count=140, order_refund_count=5, order_refund_user_count=4),
        TradeStatsByCate(dt=date(2024, 8, 28), recent_days=1, category1_id='003', category1_name='服装', category2_id='00302', category2_name='女装', category3_id='0030201', category3_name='连衣裙', order_count=100, order_user_count=90, order_refund_count=3, order_refund_user_count=2),
        TradeStatsByCate(dt=date(2024, 8, 28), recent_days=7, category1_id='003', category1_name='服装', category2_id='00301', category2_name='男装', category3_id='0030101', category3_name='T恤', order_count=1050, order_user_count=980, order_refund_count=25, order_refund_user_count=20),
        TradeStatsByCate(dt=date(2024, 8, 28), recent_days=7, category1_id='003', category1_name='服装', category2_id='00302', category2_name='女装', category3_id='0030201', category3_name='连衣裙', order_count=700, order_user_count=650, order_refund_count=15, order_refund_user_count=12),
        TradeStatsByTm(dt=date(2024, 8, 29), recent_days=1, tm_id='T001', tm_name='Apple', order_count=100, order_user_count=90, order_refund_count=2, order_refund_user_count=1),
        TradeStatsByTm(dt=date(2024, 8, 29), recent_days=1, tm_id='T002', tm_name='Samsung', order_count=80, order_user_count=75, order_refund_count=4, order_refund_user_count=3),
        TradeStatsByTm(dt=date(2024, 8, 29), recent_days=7, tm_id='T001', tm_name='Apple', order_count=700, order_user_count=650, order_refund_count=10, order_refund_user_count=8),
        TradeStatsByTm(dt=date(2024, 8, 29), recent_days=7, tm_id='T002', tm_name='Samsung', order_count=560, order_user_count=510, order_refund_count=12, order_refund_user_count=9),
        TradeStatsByTm(dt=date(2024, 8, 29), recent_days=30, tm_id='T003', tm_name='Sony', order_count=150, order_user_count=140, order_refund_count=5, order_refund_user_count=4),
        TradeStatsByTm(dt=date(2024, 8, 29), recent_days=30, tm_id='T004', tm_name='LG', order_count=130, order_user_count=120, order_refund_count=6, order_refund_user_count=5),
        TradeStatsByTm(dt=date(2024, 8, 28), recent_days=1, tm_id='T005', tm_name='Nike', order_count=120, order_user_count=110, order_refund_count=3, order_refund_user_count=2),
        TradeStatsByTm(dt=date(2024, 8, 28), recent_days=1, tm_id='T006', tm_name='Adidas', order_count=90, order_user_count=85, order_refund_count=2, order_refund_user_count=1),
        TradeStatsByTm(dt=date(2024, 8, 28), recent_days=7, tm_id='T005', tm_name='Nike', order_count=840, order_user_count=780, order_refund_count=15, order_refund_user_count=12),
        TradeStatsByTm(dt=date(2024, 8, 28), recent_days=7, tm_id='T006', tm_name='Adidas', order_count=600, order_user_count=570, order_refund_count=10, order_refund_user_count=8),
        TrafficStatsByChannel(dt=date(2024, 8, 29), recent_days=1, channel='Organic Search', uv_count=1500, avg_duration_sec=300, avg_page_count=5, sv_count=1200, bounce_rate=35.50),
        TrafficStatsByChannel(dt=date(2024, 8, 29), recent_days=1, channel='Paid Search', uv_count=800, avg_duration_sec=250, avg_page_count=4, sv_count=600, bounce_rate=40.20),
        TrafficStatsByChannel(dt=date(2024, 8, 29), recent_days=1, channel='Social Media', uv_count=1200, avg_duration_sec=270, avg_page_count=6, sv_count=1000, bounce_rate=30.75),
        TrafficStatsByChannel(dt=date(2024, 8, 29), recent_days=7, channel='Organic Search', uv_count=10500, avg_duration_sec=320, avg_page_count=5.5, sv_count=8500, bounce_rate=33.00),
        TrafficStatsByChannel(dt=date(2024, 8, 29), recent_days=7, channel='Paid Search', uv_count=5600, avg_duration_sec=260, avg_page_count=4.2, sv_count=4500, bounce_rate=38.10),
        TrafficStatsByChannel(dt=date(2024, 8, 29), recent_days=7, channel='Social Media', uv_count=8400, avg_duration_sec=280, avg_page_count=6.2, sv_count=7000, bounce_rate=32.00),
        TrafficStatsByChannel(dt=date(2024, 8, 28), recent_days=30, channel='Organic Search', uv_count=46000, avg_duration_sec=310, avg_page_count=5.4, sv_count=35000, bounce_rate=34.50),
        TrafficStatsByChannel(dt=date(2024, 8, 28), recent_days=30, channel='Paid Search', uv_count=25000, avg_duration_sec=270, avg_page_count=4.5, sv_count=20000, bounce_rate=37.80),
        TrafficStatsByChannel(dt=date(2024, 8, 28), recent_days=30, channel='Social Media', uv_count=35000, avg_duration_sec=290, avg_page_count=6.0, sv_count=30000, bounce_rate=31.00),
        UserAction(dt=date(2024, 8, 29), recent_days=1, home_count=3000, good_detail_count=1200, cart_count=800, order_count=500, payment_count=450),
        UserAction(dt=date(2024, 8, 29), recent_days=7, home_count=21000, good_detail_count=8400, cart_count=5600, order_count=3500, payment_count=3100),
        UserAction(dt=date(2024, 8, 29), recent_days=30, home_count=90000, good_detail_count=36000, cart_count=24000, order_count=15000, payment_count=13000),
        UserAction(dt=date(2024, 8, 28), recent_days=1, home_count=2800, good_detail_count=1150, cart_count=750, order_count=490, payment_count=440),
        UserAction(dt=date(2024, 8, 28), recent_days=7, home_count=20000, good_detail_count=8200, cart_count=5500, order_count=3400, payment_count=3000),
        UserAction(dt=date(2024, 8, 28), recent_days=30, home_count=88000, good_detail_count=35000, cart_count=23000, order_count=14800, payment_count=12500),
        UserChange(dt='2024-08-29', user_churn_count='150', user_back_count='80'),
        UserChange(dt='2024-08-28', user_churn_count='200', user_back_count='95'),
        UserChange(dt='2024-08-27', user_churn_count='180', user_back_count='70'),
        UserChange(dt='2024-08-26', user_churn_count='160', user_back_count='85'),
        UserChange(dt='2024-08-25', user_churn_count='170', user_back_count='90'),
        UserRetention(dt=date(2024, 8, 29), create_date='2024-08-01', retention_day=1, retention_count=1200, new_user_count=1500, retention_rate=80.00),
        UserRetention(dt=date(2024, 8, 29), create_date='2024-08-01', retention_day=7, retention_count=800, new_user_count=1500, retention_rate=53.33),
        UserRetention(dt=date(2024, 8, 29), create_date='2024-08-01', retention_day=30, retention_count=400, new_user_count=1500, retention_rate=26.67),
        UserRetention(dt=date(2024, 8, 29), create_date='2024-08-15', retention_day=1, retention_count=1300, new_user_count=1600, retention_rate=81.25),
        UserRetention(dt=date(2024, 8, 29), create_date='2024-08-15', retention_day=7, retention_count=850, new_user_count=1600, retention_rate=53.13),
        UserRetention(dt=date(2024, 8, 29), create_date='2024-08-15', retention_day=30, retention_count=420, new_user_count=1600, retention_rate=26.25),
        UserRetention(dt=date(2024, 8, 28), create_date='2024-08-05', retention_day=1, retention_count=1100, new_user_count=1400, retention_rate=78.57),
        UserRetention(dt=date(2024, 8, 28), create_date='2024-08-05', retention_day=7, retention_count=750, new_user_count=1400, retention_rate=53.57),
        UserRetention(dt=date(2024, 8, 28), create_date='2024-08-05', retention_day=30, retention_count=380, new_user_count=1400, retention_rate=27.14),
        UserRetention(dt=date(2024, 8, 28), create_date='2024-08-10', retention_day=1, retention_count=1150, new_user_count=1450, retention_rate=79.31),
        UserRetention(dt=date(2024, 8, 28), create_date='2024-08-10', retention_day=7, retention_count=780, new_user_count=1450, retention_rate=53.79),
        UserRetention(dt=date(2024, 8, 28), create_date='2024-08-10', retention_day=30, retention_count=400, new_user_count=1450, retention_rate=27.59),
        UserStats(dt=date(2024, 8, 29), recent_days=1, new_user_count=500, active_user_count=400),
        UserStats(dt=date(2024, 8, 29), recent_days=7, new_user_count=3500, active_user_count=3000),
        UserStats(dt=date(2024, 8, 29), recent_days=30, new_user_count=15000, active_user_count=12000),
        UserStats(dt=date(2024, 8, 28), recent_days=1, new_user_count=480, active_user_count=390),
        UserStats(dt=date(2024, 8, 28), recent_days=7, new_user_count=3400, active_user_count=2900),
        UserStats(dt=date(2024, 8, 28), recent_days=30, new_user_count=14800, active_user_count=11800),
        UserStats(dt=date(2024, 8, 27), recent_days=1, new_user_count=520, active_user_count=410),
        UserStats(dt=date(2024, 8, 27), recent_days=7, new_user_count=3600, active_user_count=3100),
        UserStats(dt=date(2024, 8, 27), recent_days=30, new_user_count=15500, active_user_count=12200),
    ]

    db.session.bulk_save_objects(records)  # 批量插入数据
    db.session.commit()  # 提交更改

    return "Data inserted successfully!"

table_dict = {
    'UserStats': UserStats, 'TradeStatsByTm': TradeStatsByTm, 'ActivityStats': ActivityStats, 'CouponStats': CouponStats,
    'NewBuyerStats': NewBuyerStats, 'OrderByProvince': OrderByProvince, 'PagePath': PagePath,
    'RepeatPurchaseByTm': RepeatPurchaseByTm, 'SkuCartNumTop3ByCate': SkuCartNumTop3ByCate, 'TradeStats': TradeStats,
    'TradeStatsByCate': TradeStatsByCate, 'TrafficStatsByChannel': TrafficStatsByChannel,
    'UserAction': UserAction, 'UserChange': UserChange, 'UserRetention': UserRetention
}


@app.route('/api/mysql/query/activity_stats', methods=['POST'])
def submit_data1():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_activity_id = data.get('activity_id')
    model_class = table_dict.get('ActivityStats')
    middle_data = model_class.query.filter_by(dt=data_dt, activity_id=data_activity_id).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "reduce_rate": result_data.reduce_rate}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/coupon_stats', methods=['POST'])
def submit_data2():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_coupon_id = data.get('coupon_id')
    model_class = table_dict.get('CouponStats')
    middle_data = model_class.query.filter_by(dt=data_dt, coupon_id=data_coupon_id).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "reduce_rate": result_data.reduce_rate}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/new_buyer_stats', methods=['POST'])
def submit_data3():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    model_class = table_dict.get('NewBuyerStats')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "new_order_user_count": result_data.new_order_user_count,
                  "new_payment_user_count": result_data.new_payment_user_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/order_by_province', methods=['POST'])
def submit_data4():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    data_province_id = data.get('province_id')
    model_class = table_dict.get('OrderByProvince')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days, province_id=data_province_id).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "order_count": result_data.order_count,
                  "order_total_amount": result_data.order_total_amount}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/page_path', methods=['POST'])
def submit_data5():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    data_source = data.get('source')
    data_target = data.get('target')
    model_class = table_dict.get('PagePath')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days
                                              , source=data_source, target=data_target).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "path_count": result_data.path_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/repeat_purchase_by_tm', methods=['POST'])
def submit_data6():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    data_tm_id = data.get('tm_id')
    model_class = table_dict.get('RepeatPurchaseByTm')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days
                                              , tm_id=data_tm_id).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "order_repeat_rate": result_data.order_repeat_rate}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/sku_cart_num_top3_by_cate', methods=['POST'])
def submit_data7():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_category1_id = data.get('category1_id')
    data_category2_id = data.get('category2_id')
    data_category3_id = data.get('category3_id')
    data_sku_id = data.get('sku_id')
    model_class = table_dict.get('SkuCartNumTop3ByCate')
    middle_data = model_class.query.filter_by(dt=data_dt, category1_id=data_category1_id, category2_id=data_category2_id
                                              , category3_id=data_category3_id, sku_id=data_sku_id).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "cart_num": result_data.cart_num, "rk": result_data.rk}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/trade_stats', methods=['POST'])
def submit_data8():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    model_class = table_dict.get('TradeStats')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "order_total_amount": result_data.order_total_amount, "order_count": result_data.order_count,
                  "order_user_count": result_data.order_user_count, "order_refund_count": result_data.order_refund_count
                  , "order_refund_user_count": result_data.order_refund_user_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/trade_stats_by_cate', methods=['POST'])
def submit_data9():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    data_category1_id = data.get('category1_id')
    data_category2_id = data.get('category2_id')
    data_category3_id = data.get('category3_id')
    model_class = table_dict.get('TradeStatsByCate')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days, category1_id=data_category1_id, category2_id=data_category2_id
                                              , category3_id=data_category3_id).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "order_count": result_data.order_count, "order_user_count": result_data.order_user_count,
                  "order_refund_count": result_data.order_refund_count, "order_refund_user_count": result_data.order_refund_user_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/trade_stats_by_tm', methods=['POST'])
def submit_data10():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    data_tm_id = data.get('tm_id')
    model_class = table_dict.get('TradeStatsByTm')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days, tm_id=data_tm_id).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "order_count": result_data.order_count, "order_user_count": result_data.order_user_count
            , "order_refund_count": result_data.order_refund_count, "order_refund_user_count": result_data.order_refund_user_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/traffic_stats_by_channel', methods=['POST'])
def submit_data11():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    data_channel = data.get('channel')
    model_class = table_dict.get('TrafficStatsByChannel')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days, channel=data_channel).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "uv_count": result_data.uv_count, "avg_duration_sec=": result_data.avg_duration_sec
            , "avg_page_count": result_data.avg_page_count, "sv_count": result_data.sv_count, "bounce_rate": result_data.bounce_rate}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/user_action', methods=['POST'])
def submit_data12():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    model_class = table_dict.get('UserAction')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "home_count": result_data.home_count, "good_detail_count": result_data.good_detail_count,
                  "cart_count": result_data.cart_count, "order_count": result_data.order_count, "payment_count": result_data.payment_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/user_change', methods=['POST'])
def submit_data13():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    model_class = table_dict.get('UserChange')
    middle_data = model_class.query.filter_by(dt=data_dt).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "user_churn_count": result_data.user_churn_count, "user_back_count": result_data.user_back_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/user_retention', methods=['POST'])
def submit_data14():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_create_date = data.get('create_date')
    model_class = table_dict.get('UserRetention')
    middle_data = model_class.query.filter_by(dt=data_dt, create_date=data_create_date).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "retention_count": result_data.retention_count, "new_user_count": result_data.new_user_count,
                  "retention_rate": result_data.retention_rate}
        result_data_list.append(content)
    return jsonify(result_data_list)

@app.route('/api/mysql/query/user_stats', methods=['POST'])
def submit_data15():
    # 获取POST请求中的数据
    data = request.form  # 如果数据是表单格式
    data_dt = data.get('dt')
    data_recent_days = data.get('recent_days')
    model_class = table_dict.get('UserStats')
    middle_data = model_class.query.filter_by(dt=data_dt, recent_days=data_recent_days).all()
    # json返回
    result_data_list = []
    for result_data in middle_data:
        content ={"msg": "success", "new_user_count": result_data.new_user_count, "active_user_count": result_data.active_user_count}
        result_data_list.append(content)
    return jsonify(result_data_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 确保表格在第一次运行时被创建
    app.run(debug=True)

