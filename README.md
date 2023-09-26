项目的目的时使用pgadmin4中提供的 *.sql 文件模板，根据具体参数快速生成SQL语句。
- pgadmin4 6.9

1，安装依赖
```
pip install -r requirements.txt
```
2，在项目终端执行：
```
1，创建表：python main.py --node=Table --action=create --data="{'name': 'TEST', 'schema': 'public', 'relowner': 'postgres', 'description': '121212', 'spcname':'pg_default'}"
2，修改拓展：python main.py --node=Extension --action=update --data="{'schema': 'First', 'version':'1.0'}"  --old_data="{'name':'TEST','schema': '222', 'version':'2.0'}"
```