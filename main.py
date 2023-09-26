import importlib
import argparse
import ast

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--node', type=str)
    parser.add_argument('--action', type=str)
    parser.add_argument('--data', type=ast.literal_eval)
    parser.add_argument('--old_data', type=ast.literal_eval)

    args = parser.parse_args()

    # 将args.params转为字典
    data_dict = dict(args.data)
    old_data_dict = {}
    if args.action == 'update':
        old_data_dict = dict(args.old_data)

    # 动态导入模块
    module = importlib.import_module(args.node)

    # 从模块中导入模块同名文件
    file = importlib.import_module(module.__name__ + '.' + module.__name__)

    # 从文件中导入函数 create 和 update
    create = getattr(file, 'create')
    update = getattr(file, 'update')

    if args.action == 'create':
        create(data_dict)

    if args.action == 'update':
        update(data_dict, old_data_dict)
