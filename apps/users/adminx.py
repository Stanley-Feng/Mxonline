import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class GlobalSettings(object):
    """xadmin 全局配置参数信息设置"""
    site_title = "遮天后台管理"
    site_footer = "stanley's admin"
    menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
    """创建admin的管理类,这里不再是继承admin，而是继承object"""
    # 配置后台我们需要显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    """创建banner的管理类"""
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 将model与admin管理器进行关联注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)
