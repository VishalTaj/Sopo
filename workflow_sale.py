<?xml version="1.0" encoding="utf-8"?>
<openerp>
    <data>
         <record id="my_quotation_form" model="ir.ui.view">
            <field name="name">sale.order.form</field>
            <field name="model">sale.order</field>
            <field name="inherit_id" ref="sale.view_order_form"/>
            <field name="arch" type="xml">

                    <button name="action_quotation_send" position="before">
                        <button name="approve_quotation" string="To Check" states="draft" type="workflow" class="oe_highlight" groups="base.group_user"/>
                        <button name="approve_quotation_second" string="Checked" states="quotation_approved" type="workflow" class="oe_highlight" groups="base.group_user"/>
                        <button name="approve_quotation_validate" string="Approved" states="quotation_second" type="workflow" class="oe_highlight" groups="base.group_user"/>
                    </button>
                    <button name="action_quotation_send" position="attributes">
                        <attribute name="states">quotation_approved,quotation_second,quotation_validate,sent,progress,manual</attribute>
                    </button>
                    <button name="print_quotation" position="attributes">
                        <attribute name="states">quotation_approved,sent,progress,manual</attribute>
                    </button>

                     <button name="action_button_confirm" position="attributes">
                        <attribute name="states">quotation_approved,quotation_second,quotation_validate,sent,progress,manual</attribute>
                    </button>


                    <field name="state" position="attributes">
                        <attribute name="statusbar_visible">draft,quotation_approved,quotation_second,quotation_validate,sent,progress,done</attribute>
                    </field>
            </field>
        </record>
        <record id="my_action_quotations" model="ir.actions.act_window">
            <field name="name">My Quotations</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">sale.order</field>
            <field name="view_type">tree</field>
            <field name="view_id" ref="sale.view_quotation_tree"/>
            <field name="view_mode">tree,form,calendar,graph</field>
            <field name="context">{'search_default_my_sale_orders_filter': 1}</field>
            <field name="domain">[('state','in',('draft','quotation_approved','quotation_second','quotation_validate' 'sent','cancel'))]</field>
            <field name="search_view_id" ref="sale.view_sales_order_filter"/>
            <field name="help" type="html">
              <p class="oe_view_nocontent_create">
                You Can See Here all the Approval Types Here
              </p><p>
                Odoo will help you handle efficiently the complete sale flow:
                from the quotation to the sales order, the
                delivery, the invoicing and the payment collection.
              </p><p>
                The social feature helps you organize discussions on each sales
                order, and allow your customers to keep track of the evolution
                of the sales order.
              </p>
            </field>
        </record>

        <menuitem action="my_action_quotations"
            name="Approval Details"
            id="menu_my_quotation"
            parent="base.menu_sales"
            sequence="99"/>
        <record id="act_quotation_approved" model="workflow.activity">
            <field name="wkf_id" ref="sale.wkf_sale"/>
            <field name="name">To check</field>
            <field name="kind">function</field>
            <field name="action">action_quotation_approve</field>
        </record>
        <record id="trans_quotation_draft_to_approved" model="workflow.transition">
            <field name="act_from" ref="sale.act_draft"/>
            <field name="act_to" ref="act_quotation_approved"/>
            <field name="signal">approve_quotation</field>
        </record>
        <record id="act_quotation_approved_second" model="workflow.activity">
            <field name="wkf_id" ref="sale.wkf_sale"/>
            <field name="name">Checked</field>
            <field name="kind">function</field>
            <field name="action">action_quotation_approve_second()</field>
        </record>
        <record id="trans_quotation_tocheck_to_checked_second" model="workflow.transition">
            <field name="act_from" ref="act_quotation_approved"/>
            <field name="act_to" ref="act_quotation_approved_second"/>
            <field name="signal">approve_quotation_second</field>
        </record>
        <record id="act_quotation_approve_approved" model="workflow.activity">
            <field name="wkf_id" ref="sale.wkf_sale"/>
            <field name="name">Approved</field>
            <field name="kind">function</field>
            <field name="action">action_quotation_approve_validate()</field>
        </record>
        <record id="trans_quotation_checked_to_approve" model="workflow.transition">
            <field name="act_from" ref="act_quotation_approved_second"/>
            <field name="act_to" ref="act_quotation_approve_approved"/>
            <field name="signal">approve_quotation_validate</field>
        </record>
    </data>
</openerp>
