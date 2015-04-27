from openerp.osv import fields, osv
from openerp.tools.translate import _

class sopo(osv.Model):
    _inherit = 'sale.order'
    _columns = {
        'project': fields.char('Project',size=64),
        'contract_no': fields.char('Contract No',size=64),
        'sale_order_in': fields.one2many('purchase.order', 'related_sale_order', string='Related Purchase Order'),
        'sales_commission': fields.one2many('sales.commission', 'orders_id', string="Sales Commission"),
    }


class commission_tab(osv.Model):
    _name = 'sales.commission'

    def _get_total(self, cr, uid, ids,fields,args, context=None):
        obj = {}
        for record in self.browse(cr,uid,ids,context=context):
            obj[record.id] = self.pool.get('sale.order').browse(cr,uid, record.orders_id.id).amount_total
        return obj

    def _get_commission(self, cr, uid, ids,fields,args, context=None):
        obj = {}
        for record in self.browse(cr,uid,ids,context=context):
            obj[record.id] = (record.sales_value * record.percentage)/100
        return obj

    _columns = {
        'orders_id': fields.many2one('sale.order'),
        'user': fields.many2one('res.users', 'User'),
        'sales_value': fields.function(_get_total, type='char', string='Total', size=64),
        'percentage': fields.float('Percentage'),
        'commission': fields.function(_get_commission,type='char',string='Commission', size=64),
    }




class poso(osv.Model):
    _inherit = 'purchase.order'

    def change_cn(self, cr, uid, ids, related_sale_order, context=None):
        res = {}
        if related_sale_order:
            obj = self.pool.get('sale.order').browse(cr, uid, related_sale_order)
            res['contract_no'] = obj.contract_no
        return {'value': res}

    _columns = {
        'contract_no': fields.char('Contract NO', size=64),
        'related_sale_order': fields.many2one('sale.order', 'Related Sale Order', required=True),
    }



sopo()
poso()
commission_tab()
