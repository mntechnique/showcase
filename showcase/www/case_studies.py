import frappe

def get_context(context):
	context.case_studies = frappe.get_all("Case Study",
		fields=["name", "case_name", "problem_description", "page_name"],
		filters={"published":1},
		order_by="name desc")
