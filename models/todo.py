#-*- coding: utf-8 -*-
from odoo import models ,fields,api


class TodoManagement(models.Model):
    _name = 'todo.management'
    _description = "To Do List"
    _inherit = ['mail.thread' , 'mail.activity.mixin']

    name=fields.Char(required = True)
    description =fields.Text()
    due_date = fields.Date(required = True)
    status = fields.Selection([
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ], default = 'new')
    user_id = fields.Many2one('task.person' , string='Assigned To')

    _sql_constraints = [
        ('unique_name','unique("name")','This Task does exist')
    ]
    line_ids = fields.One2many('todo.management.line', 'todo_management_id')

    def action_new(self):
        for rec in self : 
            print("inside the new action")
            rec.status = 'new'

    def action_in_progress(self):
        for rec in self : 
            print("inside the in_progress action")
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self : 
            print("inside the completed action")
            rec.status = 'completed'


class TodoMangementLine(models.Model):
    _name = 'todo.management.line'

    main =fields.Char()
    todo_management_id = fields.Many2one('todo.management')