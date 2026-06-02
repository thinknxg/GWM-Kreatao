import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_quotation_items(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql("""
        SELECT DISTINCT qi.item_code, qi.item_name
        FROM `tabQuotation Item` qi
        WHERE qi.item_code LIKE %(txt)s
        LIMIT %(page_len)s OFFSET %(start)s
    """, {
        "txt": "%" + txt + "%",
        "page_len": page_len,
        "start": start
    })
