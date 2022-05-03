# 初始化flask app变量
export FLASK_APP=$PWD/manage.py
# 初始项目根目录到环境变量中
# 确保部分相对引用可用
export  PYTHONPATH=${PYTHONPATH}:$PWD
# 关闭mysql默认的ONLY_FULL_GROUP_BY sql_mode
#mysql -h 主机地址 -u用户名 -p密码 -e "set @@GLOBAL.sql_mode='';"""
mysql -h localhost -uroot -proot -e "set @@GLOBAL.sql_mode='';"""
