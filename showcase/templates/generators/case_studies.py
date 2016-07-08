import frappe

def get_context(context):
	context.case_studies = frappe.get_all("Case Study",
		fields=["name", "case_name", "problem_description", "page_name"],
		order_by="name desc")
