from job_web.app import create_app
from flask_admin import Admin as FAdmin
from flask_admin.contrib.sqla import ModelView
from job_web.models import Company,Job,User, Advertisement,db

app = create_app('development')

class CompanyView(ModelView):
    column_list = ['name','is_enable' ]

if __name__ == '__main__':
    admin = FAdmin(app, name='后台管理系统', template_mode='bootstrap3')
    admin.add_view(CompanyView(Company, db.session,endpoint='m_company',name='公司管理'))

    admin.add_view(ModelView(Advertisement, db.session,endpoint='m_advertisement',name='广告管理'))
    admin.add_view(ModelView(User, db.session,endpoint='m_user',name='求职者管理'))
    admin.add_view(ModelView(Job, db.session,endpoint='m_job',name='岗位管理'))
    app.run()
