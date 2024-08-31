from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

# 1）各活动补贴率
class ActivityStats(db.Model):
    __tablename__ = 'activity_stats'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    activity_id = db.Column(db.String(16), primary_key=True, comment='活动ID')
    activity_name = db.Column(db.String(64), nullable=True, comment='活动名称')
    start_date = db.Column(db.String(16), nullable=True, comment='活动开始日期')
    reduce_rate = db.Column(db.DECIMAL(16, 2), nullable=True, comment='补贴率')

# 2）各优惠券补贴率
class CouponStats(db.Model):
    __tablename__ = 'coupon_stats'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    coupon_id = db.Column(db.String(16), primary_key=True, comment='优惠券ID')
    coupon_name = db.Column(db.String(64), nullable=True, comment='优惠券名称')
    start_date = db.Column(db.String(16), nullable=True, comment='发布日期')
    rule_name = db.Column(db.String(64), nullable=True, comment='优惠规则，例如满100元减10元')
    reduce_rate = db.Column(db.DECIMAL(16, 2), nullable=True, comment='补贴率')

# 3）新增交易用户统计
class NewBuyerStats(db.Model):
    __tablename__ = 'new_buyer_stats'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1天,7:最近7天,30:最近30天')
    new_order_user_count = db.Column(db.BigInteger, nullable=True, comment='新增下单人数')
    new_payment_user_count = db.Column(db.BigInteger, nullable=True, comment='新增支付人数')

# 4）各省份订单统计
class OrderByProvince(db.Model):
    __tablename__ = 'order_by_province'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1天,7:最近7天,30:最近30天')
    province_id = db.Column(db.String(16), primary_key=True, comment='省份ID')
    province_name = db.Column(db.String(16), nullable=True, comment='省份名称')
    area_code = db.Column(db.String(16), nullable=True, comment='地区编码')
    iso_code = db.Column(db.String(16), nullable=True, comment='国际标准地区编码')
    iso_code_3166_2 = db.Column(db.String(16), nullable=True, comment='国际标准地区编码')
    order_count = db.Column(db.BigInteger, nullable=True, comment='订单数')
    order_total_amount = db.Column(db.DECIMAL(16, 2), nullable=True, comment='订单金额')

# 5）用户路径分析
class PagePath(db.Model):
    __tablename__ = 'page_path'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1天,7:最近7天,30:最近30天')
    source = db.Column(db.String(64), primary_key=True, comment='跳转起始页面ID')
    target = db.Column(db.String(64), primary_key=True, comment='跳转终到页面ID')
    path_count = db.Column(db.BigInteger, nullable=True, comment='跳转次数')

# 6）各品牌复购率
class RepeatPurchaseByTm(db.Model):
    __tablename__ = 'repeat_purchase_by_tm'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,7:最近7天,30:最近30天')
    tm_id = db.Column(db.String(16), primary_key=True, comment='品牌ID')
    tm_name = db.Column(db.String(32), nullable=True, comment='品牌名称')
    order_repeat_rate = db.Column(db.DECIMAL(16, 2), nullable=True, comment='复购率')

# 7）各品类商品购物车存量topN
class SkuCartNumTop3ByCate(db.Model):
    __tablename__ = 'sku_cart_num_top3_by_cate'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    category1_id = db.Column(db.String(16), primary_key=True, comment='一级分类ID')
    category1_name = db.Column(db.String(64), nullable=True, comment='一级分类名称')
    category2_id = db.Column(db.String(16), primary_key=True, comment='二级分类ID')
    category2_name = db.Column(db.String(64), nullable=True, comment='二级分类名称')
    category3_id = db.Column(db.String(16), primary_key=True, comment='三级分类ID')
    category3_name = db.Column(db.String(64), nullable=True, comment='三级分类名称')
    sku_id = db.Column(db.String(16), primary_key=True, comment='商品ID')
    sku_name = db.Column(db.String(128), nullable=True, comment='商品名称')
    cart_num = db.Column(db.BigInteger, nullable=True, comment='购物车中商品数量')
    rk = db.Column(db.BigInteger, nullable=True, comment='排名')

# 8）交易综合统计
class TradeStats(db.Model):
    __tablename__ = 'trade_stats'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1日,7:最近7天,30:最近30天')
    order_total_amount = db.Column(db.DECIMAL(16, 2), nullable=True, comment='订单总额,GMV')
    order_count = db.Column(db.BigInteger, nullable=True, comment='订单数')
    order_user_count = db.Column(db.BigInteger, nullable=True, comment='下单人数')
    order_refund_count = db.Column(db.BigInteger, nullable=True, comment='退单数')
    order_refund_user_count = db.Column(db.BigInteger, nullable=True, comment='退单人数')

# 9）各品类商品交易统计
class TradeStatsByCate(db.Model):
    __tablename__ = 'trade_stats_by_cate'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1天,7:最近7天,30:最近30天')
    category1_id = db.Column(db.String(16), primary_key=True, comment='一级分类id')
    category1_name = db.Column(db.String(64), nullable=True, comment='一级分类名称')
    category2_id = db.Column(db.String(16), primary_key=True, comment='二级分类id')
    category2_name = db.Column(db.String(64), nullable=True, comment='二级分类名称')
    category3_id = db.Column(db.String(16), primary_key=True, comment='三级分类id')
    category3_name = db.Column(db.String(64), nullable=True, comment='三级分类名称')
    order_count = db.Column(db.BigInteger, nullable=True, comment='订单数')
    order_user_count = db.Column(db.BigInteger, nullable=True, comment='订单人数')
    order_refund_count = db.Column(db.BigInteger, nullable=True, comment='退单数')
    order_refund_user_count = db.Column(db.BigInteger, nullable=True, comment='退单人数')

# 10）各品牌商品交易统计
class TradeStatsByTm(db.Model):
    __tablename__ = 'trade_stats_by_tm'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1天,7:最近7天,30:最近30天')
    tm_id = db.Column(db.String(16), primary_key=True, comment='品牌ID')
    tm_name = db.Column(db.String(32), nullable=True, comment='品牌名称')
    order_count = db.Column(db.BigInteger, nullable=True, comment='订单数')
    order_user_count = db.Column(db.BigInteger, nullable=True, comment='订单人数')
    order_refund_count = db.Column(db.BigInteger, nullable=True, comment='退单数')
    order_refund_user_count = db.Column(db.BigInteger, nullable=True, comment='退单人数')

# 11）各渠道流量统计
class TrafficStatsByChannel(db.Model):
    __tablename__ = 'traffic_stats_by_channel'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1天,7:最近7天,30:最近30天')
    channel = db.Column(db.String(16), primary_key=True, comment='渠道')
    uv_count = db.Column(db.BigInteger, nullable=True, comment='访客人数')
    avg_duration_sec = db.Column(db.BigInteger, nullable=True, comment='会话平均停留时长，单位为秒')
    avg_page_count = db.Column(db.BigInteger, nullable=True, comment='会话平均浏览页面数')
    sv_count = db.Column(db.BigInteger, nullable=True, comment='会话数')
    bounce_rate = db.Column(db.DECIMAL(16, 2), nullable=True, comment='跳出率')

# 12）用户行为漏斗分析
class UserAction(db.Model):
    __tablename__ = 'user_action'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近天数,1:最近1天,7:最近7天,30:最近30天')
    home_count = db.Column(db.BigInteger, nullable=True, comment='浏览首页人数')
    good_detail_count = db.Column(db.BigInteger, nullable=True, comment='浏览商品详情页人数')
    cart_count = db.Column(db.BigInteger, nullable=True, comment='加入购物车人数')
    order_count = db.Column(db.BigInteger, nullable=True, comment='下单人数')
    payment_count = db.Column(db.BigInteger, nullable=True, comment='支付人数')

# 13）用户变动统计
class UserChange(db.Model):
    __tablename__ = 'user_change'
    dt = db.Column(db.String(16), primary_key=True, comment='统计日期')
    user_churn_count = db.Column(db.String(16), nullable=True, comment='流失用户数')
    user_back_count = db.Column(db.String(16), nullable=True, comment='回流用户数')

# 14）用户留存率
class UserRetention(db.Model):
    __tablename__ = 'user_retention'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    create_date = db.Column(db.String(16), primary_key=True, comment='用户新增日期')
    retention_day = db.Column(db.Integer, primary_key=True, comment='截至当前日期留存天数')
    retention_count = db.Column(db.BigInteger, nullable=True, comment='留存用户数量')
    new_user_count = db.Column(db.BigInteger, nullable=True, comment='新增用户数量')
    retention_rate = db.Column(db.DECIMAL(16, 2), nullable=True, comment='留存率')

# 15）用户新增活跃统计
class UserStats(db.Model):
    __tablename__ = 'user_stats'
    dt = db.Column(db.Date, primary_key=True, comment='统计日期')
    recent_days = db.Column(db.BigInteger, primary_key=True, comment='最近n日,1:最近1日,7:最近7日,30:最近30日')
    new_user_count = db.Column(db.BigInteger, nullable=True, comment='新增用户数')
    active_user_count = db.Column(db.BigInteger, nullable=True, comment='活跃用户数')





