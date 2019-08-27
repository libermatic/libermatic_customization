# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__

app_name = "libermatic_customization"
app_version = __version__
app_title = "Libermatic Customization"
app_publisher = "Libermatic"
app_description = "Customization for libermatic"
app_icon = "fa fa-cog"
app_color = "'#2196F3'"
app_email = "info@libermatic.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = \
#     "/assets/libermatic_customization/css/libermatic_customization.css"
# app_include_js = \
#     "/assets/libermatic_customization/js/libermatic_customization.js"

# include js, css files in header of web template
# web_include_css = \
#     "/assets/libermatic_customization/css/libermatic_customization.css"
# web_include_js = \
#     "/assets/libermatic_customization/js/libermatic_customization.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#    "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "libermatic_customization.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "libermatic_customization.install.before_install"
# after_install = "libermatic_customization.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = \
#     "libermatic_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#   "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {"*": {"on_submit": "libermatic_customization.doc_events"}}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "all": [
#         "libermatic_customization.tasks.all"
#     ],
#     "daily": [
#         "libermatic_customization.tasks.daily"
#     ],
#     "hourly": [
#         "libermatic_customization.tasks.hourly"
#     ],
#     "weekly": [
#         "libermatic_customization.tasks.weekly"
#     ]
#     "monthly": [
#         "libermatic_customization.tasks.monthly"
#     ]
# }

# Testing
# -------

# before_tests = "libermatic_customization.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": \
#            "libermatic_customization.event.get_events"
# }
