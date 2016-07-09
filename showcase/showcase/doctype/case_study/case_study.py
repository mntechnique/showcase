# -*- coding: utf-8 -*-
# Copyright (c) 2015, MN Technique and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class CaseStudy(WebsiteGenerator):
	website = frappe._dict(
		condition_field = "published",
		page_title_field = "case_name",
		template = "templates/generators/case_study.html",
		no_cache = 1
	)
	def before_insert(self):
		if not self.page_name:
			page_name = self.case_name.lower()
			self.page_name = page_name.replace(" ", "-")

	def autoname(self):
		self.name = self.page_name
