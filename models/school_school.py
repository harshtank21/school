from  odoo import models,fields

class school_Management(models.Model):
    _name = "school.school"
    _description = "School Management"

    names=fields.Char(string="school name")
    email=fields.Char(string="email name")
    div=fields.Char(string="div name")
    student=fields.Char(string="student name")
    teacher=fields.Char(string="teacher name")