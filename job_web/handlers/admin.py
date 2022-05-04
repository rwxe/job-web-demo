#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, \
    current_app, redirect, url_for, flash, request
from flask_login import current_user,login_user

from job_web.forms import RegisterAdminForm
from ..models import User, Job, Company
from ..decorators import admin_required

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('front.index'))
    form = RegisterAdminForm()
    if form.validate_on_submit():
        form.create_admin()
        flash('注册成功，请登录', 'success')
        return redirect(url_for('front.login'))
    return render_template('admin/register.html', form=form, active='admin_register')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/user')
@admin_required
def user():
    page = request.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config['LIST_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/user.html', pagination=pagination)


@admin.route('/company')
@admin_required
def company():
    page = request.args.get('page', default=1, type=int)
    pagination = Company.query.paginate(
        page=page,
        per_page=current_app.config['LIST_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/company.html', pagination=pagination)


@admin.route('/job')
@admin_required
def job():
    page = request.args.get('page', default=1, type=int)
    pagination = Job.query.paginate(
        page=page,
        per_page=current_app.config['LIST_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/job.html', pagination=pagination)


# @admin.route('/resume')
# @admin_required
# def resume():
#     page = request.args.get('page', default=1, type=int)
#     content = User.query.paginate(
#         page=page,
#         per_page=current_app.config['LIST_PER_PAGE'],
#         error_out=False
#     )
#     return render_template('admin/resumes.html', content=content)
