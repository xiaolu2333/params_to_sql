项目的目的是使用pgadmin4中提供的 *.sql 文件模板，根据具体参数快速生成SQL语句。
- pgadmin4 6.9

1，安装依赖
```
pip install -r requirements.txt
```
2，在项目终端执行：
```
1，创建表：python main.py --node=Table --action=create --data="{'name': 'test2', 'is_sys_obj': False, 'encoding': 'UTF8','datconnlimit': -1, 'variables': [], 'privileges': [],'securities': [], 'datacl': [], 'deftblacl': [], 'deffuncacl': [],'defseqacl': [], 'is_template': False, 'deftypeacl': [],'schema': 'public', 'relowner': 'postgres', 'description': '1234'}"
2，修改拓展：python main.py --node=Extension --action=update --data="{'schema': 'First', 'version':'1.0'}"  --old_data="{'name':'TEST','schema': '222', 'version':'2.0'}"
```
