import frappe

def get_context(context):
	if frappe.form_dict.get("page"):
		page = int(frappe.form_dict.get("page"))
		if page <= 0:
			page = 1
	else:
		page = 1

	case_studies = frappe.get_all("Case Study",
		fields=["name", "case_name", "case_description", "page_name", "source_code", "route"],
		filters={"published":1},
		order_by="case_name asc",
		page_length=6,
		start=(page-1)*6)
	if len (case_studies) != 0:
		context.case_studies = case_studies
	all_cases = frappe.get_all("Case Study", filters={"published":1})
	pages = len(chunks(all_cases,6))
	context.pages = pages

def chunks(seq, size):
	l = [seq[i:i+size] for i  in range(0, len(seq), size)]
	return l
