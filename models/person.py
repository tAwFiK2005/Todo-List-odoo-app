from odoo import models ,fields,api


class TaskPerson(models.Model):
    _name ='task.person'
    _description = 'Person'

    name = fields.Char(required = 1 , default = "New" , size = 12)
    tasks = fields.Integer(compute = '_compute_no', store =True)
    task_ids = fields.One2many('todo.management' , 'user_id' , store = True)

    @api.depends('task_ids')
    def _compute_no(self):
        for rec in self :
            print("inside the _compute_no")
            rec.tasks = len(rec.task_ids)
