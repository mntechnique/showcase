import frappe

def get_context(context):
	context.case_studies = frappe.get_all("Case Study",
		fields=["name", "case_name", "case_description", "page_name", "source_code", "route"],
		filters={"published":1},
		order_by="case_name asc")
	context.parents = [{'route': 'jobs', 'title': _('All Jobs') }]
