from odoo import fields, models

class InheritAccountAnalyticPlan(models.Model):
    _inherit = 'account.analytic.plan'

    _sql_constraints = [
        ('account_analytic_plan_constraints', 'unique(name, company_id)', 'The plan name must be unique per company!')
    ]

    company_id = fields.Many2one('res.company', string='Company',  default=lambda self: self.env.company,)