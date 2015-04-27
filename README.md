# Sopo
3.3 LINK SALES ORDER AND PURCHASE ORDER

3.3.1 Add SO field in PO

In the top page of the SO form view, create two char fields, named “Project” and “Contract

NO.” Show these two fields also in the SO list view.

Create a char field in the PO form view named “Contract NO.”.

In the form view of PO, add a many2one field named “Related Sales Order”, which

contains the sale.order object. Make this field a required field, show this field also in the

list view of the PO. When choosing the “Related Sales Order” in PO, automatically pass

the “Contract NO.” from SO to PO.

3.3.2 Create “Related Purchase Orders” Tab in the Sales Order

Create this tab to the right of “Other Information” tab.

In the tab, show a tree structure of all the POs that are related to the SO by the

many2one “Sales Order” field in the PO.

Create Salesmen Commission Table

In the form view of the sales order, add a "Salesmen Commission" tab.

Create a Group named "Commission", only users in this group have access to the "Salesmen

Commission" tab.

Create a tree view in this tab, the layout follows the table below:

User

Jhon

Sales Value

Percent

100

Commission

10

10

The content of the table columns are as follows:

The “User” column is the many2one of the Users object.

The “Sales Value” column is a function field which copies the value of “Total” field of order.

The “Percent” column is a float to be filled in manually

The “Commission” column is a function field equals (Sales Value*Percent)/100.

Sales Order Workflow Customization

Draft->To Check->Checked->Approved->Sale Order->Done

Add ‘To Check’ workflow after Draft

Add ‘To Check’ button to change from Draft to ‘To Check’

Add ‘Checked’ workflow after ‘To Check’

Add ‘Checked’ button to change from ‘To Check’ to ‘Checked’

Add ‘Approved’ workflow after ‘Checked’

Add ‘Approve’ button to change from ‘Checked’ to ‘Approved’

Show the “Confirm Order” button in “Approved” workflow only

When clicked on "Confirm Order”, sale order should be confirmed
