from odoo import fields, models


class AccountAnalyticPlan(models.Model):
    _inherit = 'account.analytic.plan'
    _check_company_auto = True

    _sql_constraints = [
        ('account_analytic_plan_constraints', 'unique(name, company_id)', 'The plan name must be unique per company!')
    ]

    company_id = fields.Many2one(
        'res.company',
        string='Company',  default
        =lambda self: self.env.company,
    )

    def _get_all_plans(self):
        plan_id, other_ids = super(AccountAnalyticPlan, self.sudo())._get_all_plans()
        return plan_id, other_ids.filtered(lambda r: r.company_id.id in [self.env.company.id, False] + self.env.context.get('allowed_company_ids', []))
