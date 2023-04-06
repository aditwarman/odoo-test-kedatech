from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import ValidationError
from odoo.exceptions import AccessError

import random

@tagged('standard', 'unit')
class TestMaterial(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestMaterial, self).setUp(*args, **kwargs)
        self.model = self.env['material.material']

        # self.type = ['jeans', 'cotton', 'fabric']
        self.type = 'jeans'
        self.supplier = self.env['res.partner'].create({'name': 'Wood Corner'})

    def test_create_record(self):
        # Create a new record
        record = self.model.create({
            'name': 'Test Record',
            'code': '102901',
            'material_type': self.type,
            # 'material_type': random.choice(self.type),
            'buy_price': 102,
            'res_partner': self.supplier.id
        })

        # Check that the record was created successfully
        self.assertTrue(record.id)
        self.assertEqual(record.name, 'Test Record')
        self.assertEqual(record.code, '102901')
        self.assertEqual(record.material_type, 'jeans')
        self.assertEqual(record.buy_price, '102')

    def test_create_record_with_negative_value(self):
        # Attempt to create a record with a negative value
        with self.assertRaises(ValidationError):
            self.model.create({
                'name': 'Test Record',
                'code': '102901',
                'material_type': self.type,
                'buy_price': 20,
                'res_partner': self.supplier.id
            })

    def test_delete_record(self):
        record = self.model.create({
            'name': 'Test Record',
            'code': '102901',
            'material_type': self.type,
            # 'material_type': random.choice(self.type),
            'buy_price': 102,
            'res_partner': self.supplier.id
        })

        # Check that the record was created successfully
        self.assertTrue(record.id)

        # Delete the record
        record.unlink()

        # Check that the record was deleted successfully
        with self.assertRaises(AccessError):
            self.model.browse(record.id)