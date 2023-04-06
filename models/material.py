from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = "material.material"
    _description = "Materials for sell"

    name = fields.Char(string='Material Name')
    code = fields.Char(string='Material Code')
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], default='cotton', required=True)
    buy_price = fields.Float(string='Price', required=True)
    partner_id = fields.Many2one('res.partner', string='Supplier', 
        required=True, 
        change_default=True, 
        tracking=True, 
        help="You can find a vendor by its Name, TIN, Email or Internal Reference.")

    _sql_constraints = [
        ('code', 'unique(code)', "A Code must be unique"),
        ('buy_price', 'buy_price < 100', "Buy price must be rather than 100")
    ]

    @api.model
    def create(self, value):
        if 'buy_price' in value and value['buy_price'] < 100:
            raise ValidationError("Buy Price must be rather than 100")
        
        return super(Material, self).create(value)