"""
 @Author: DFL
 @Email: xxx@xxx.com
 @FileName: Extension.py
 @DateTime: 2023/9/26 10:59
 @SoftWare: PyCharm
"""

import os
from jinja2 import Environment, FileSystemLoader

from utils.handle_quote import qtIdent

######################################### 模板解析基础配置 #########################################
# 项目根目录
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼接模板文件目录
template_path = os.path.join(root_path, 'Extension')

# 创建一个Environment对象，并指定模板文件的目录
env = Environment(loader=FileSystemLoader(template_path))

# env.filters 注册过滤器
# env.filters['qtIdent'] = qtIdent

# 注册自定义函数
env.globals['qtIdent'] = qtIdent


def custom_function(value):
    return value + ' in custom_function'


env.globals['custom_function'] = custom_function


def create(params=None):
    if params:
        # 加载模板文件
        template = env.get_template('create.sql')
        # 渲染模板并传入参数
        sql = template.render(data=params)

        # 用\n替换两个及以上个数的连续的\n
        sql = sql.replace('\n\n', '\n')

        # 打印生成的SQL字符串
        print(sql)
    else:
        print('params is None')


def update(params=None, old_params=None):
    if params:
        # 加载模板文件
        template = env.get_template('update.sql')
        # 渲染模板并传入参数
        sql = template.render(data=params, o_data=old_params)

        # 用\n替换两个及以上个数的连续的\n
        sql = sql.replace('\n\n', '\n')

        # 打印生成的SQL字符串
        print(sql)
    else:
        print('params is None')
