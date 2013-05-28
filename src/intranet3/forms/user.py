# -*- coding: utf-8 -*-
"""
Forms for user edit
"""
import wtforms as wtf
from wtforms import validators
from pyramid.i18n import TranslationStringFactory

from intranet3.models.user import levels, User

_ = TranslationStringFactory('intranet3')

class UserEditForm(wtf.Form):
    """ Admin edits freelancer's profile """
    
    def process(self, formdata=None, obj=None, **kwargs):
        if isinstance(obj, User):
            kwargs['level'] = obj.levels_list
        super(UserEditForm,self).process(formdata,obj,**kwargs)
    
    is_active = wtf.BooleanField(_(u"Is active"), validators=[])
    is_programmer = wtf.BooleanField(_(u"Is programmer"), validators=[])
    is_frontend_developer = wtf.BooleanField(_(u"Is frontend developer"), validators=[])
    is_graphic_designer = wtf.BooleanField(_(u"Is graphic designer"), validators=[])

    avatar = wtf.HiddenField()
    level = wtf.SelectMultipleField(_(u'Role'), validators=[], choices=levels)
    
    start_work  = wtf.DateField(_(u"Start work"), format='%d/%m/%Y', validators=[])
    start_full_time_work  = wtf.DateField(_(u"Start full time work"), format='%d/%m/%Y', validators=[validators.Optional()])
    description = wtf.TextField(_(u"Description"), validators=[validators.Optional()])
    location = wtf.SelectField(
        _(u"Office location"),
        choices=[('', u'--None--')] + [(k, v[0]) for k, v in User.LOCATIONS.items()]
    )

    availability_link = wtf.TextField(_(u"Availability calendar link"), validators=[validators.Optional(), validators.URL()])
    tasks_link = wtf.TextField(_(u"Tasks calendar link"), validators=[validators.Optional(), validators.URL()])
    skype = wtf.TextField(_(u"Skype"), validators=[validators.Optional()])
    phone = wtf.TextField(_(u"Phone"), validators=[validators.Optional()])
    phone_on_desk = wtf.TextField(_(u"Deskphone"), validators=[validators.Optional()])
    irc = wtf.TextField(_(u"IRC"), validators=[validators.Optional()])

    groups = wtf.SelectMultipleField(_(u'Groups'), validators=[], choices=(('freelancer','freelancer'),('user','user'),('admin','admin'), ('scrum', 'scrum')))

