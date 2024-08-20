#-*- coding: utf-8 -*-
{
    'name' : 'To Do',
    'author' : 'Ahmed Tawfik',
    'version' : '17.0.0.1.0',
    'license': 'LGPL-3',
    'depends' : ['base','mail'],
    'data' :[
        'view/base_menu.xml',
        'view/todo_mangement_view.xml',
        'view/person_view.xml',
        'security/ir.model.access.csv',
    ],
    'application':True,
    'installable': True,
}