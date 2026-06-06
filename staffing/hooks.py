from . import __version__ as app_version

app_name = "staffing"
app_title = "Staffing"
app_publisher = "jan"
app_description = "Staffing"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "janlloydangeles@gmail.com"
app_license = "MIT"

add_to_apps_screen = [
    {
        "name": "staffing",
        "logo": "/assets/staffing/images/staffing-logo.png",
        "title": "Staffing",
        "route": "/app/staffing/staffing",
    }
]

doctype_js = {
        "Sales Invoice" : "public/js/sales_invoice.js",
        "Purchase Invoice" : "public/js/purchase_invoice.js",
        "Project" : "public/js/project.js",
        "Timesy": "staffing/doctype/timesy/timesy.js",
}

user_data_fields = [
        {
                "doctype": "{doctype_1}",
                "filter_by": "{filter_by}",
                "redact_fields": ["{field_1}", "{field_2}"],
                "partial": 1,
        },
        {
                "doctype": "{doctype_2}",
                "filter_by": "{filter_by}",
                "partial": 1,
        },
        {
                "doctype": "{doctype_3}",
                "strict": False,
        },
        {
                "doctype": "{doctype_4}"
        }
]

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Purchase Invoice-timesy",
                    "Purchase Invoice-timesy_reference",
                    "Sales Invoice-timesy",
                    "Sales Invoice-timesy_reference",
                    "Additional Salary-timesy_list",
                    "Additional Salary-timesy_reference",
                    "Purchase Invoice-grand_costing_rate",
                    "Sales Invoice-grand_costing_rate",
                    "Address-report",
                    "Sales Order-custom_is_proforma_invoice",
                ]
            ]
        ]
    },
    {
        "dt": "Custom Field",
        "filters": [["dt", "in", ["Timesy", "Timesy Details"]]]
    },
    {
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Invoice Item-rate-label",
                    "Purchase Invoice Item-rate-label",
                ]
            ]
        ]
    },
    {
        "dt": "Property Setter",
        "filters": [["doc_type", "in", ["Timesy", "Timesy Details"]]]
    },
    {
        "dt": "Custom Field",
        "filters": [["dt", "in", ["Project Milestone", "Project"]]]
    },
    {
        "dt": "DocType",
        "filters": [["custom", "=", 1]]
    },
    {
        "dt": "Client Script",
        "filters": [["name", "in", [
            "Project Milestone Calculations",
            "Project Milestone Item Fetch",
            "Price List Bulk Editor"
        ]]]
    },
    {
        "dt": "Server Script",
        "filters": [["name", "in", [
            "Project Milestone Auto Invoice",
            "Project Milestone Validations"
        ]]]
    },
]
