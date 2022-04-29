# 初始化flask app变量
export FLASK_APP=manage.py
# 初始项目根目录到环境变量中
# 确保部分相对引用可用
export  PYTHONPATH=${PYTHONPATH}:$PWD
