"""
Page Content Updater for WordPress/Elementor

Batch updates multiple Elementor page layouts:
- Expands FAQ sections on service pages (Industrial, Compliance)
- Adds new content sections to suburb pages (Wacol)
- Generates matching FAQPage schema JSON for each page

This script demonstrates how to programmatically update WordPress/Elementor
content by manipulating the JSON layout structure.

Usage:
    python update-pages.py

Input:
    Reads *-current.json page layouts from the data directory.

Output:
    - Updated page JSONs (*-updated.json) with expanded content
    - Schema JSON files for FAQ markup (schema-faq-*.json)
"""

import json
import os
import random
import string

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')
SCHEMA_DIR = os.path.join(SCRIPT_DIR, '..', 'schema')

def gen_id():
    """Generate a random 7-character ID for Elementor elements."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def load_page(filename):
    """Load and parse an Elementor page JSON, handling double-encoded strings."""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    data = json.loads(raw)
    if isinstance(data, str):
        data = json.loads(data)
    return data

def save_page(data, filename):
    """Save an Elementor page JSON layout."""
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))

def make_accordion_faq(tabs):
    """Create an Elementor accordion widget with FAQ items."""
    return {
        "id": gen_id(),
        "elType": "widget",
        "settings": {
            "tabs": tabs,
            "title_color": "#042A3C",
            "title_background": "#F8F9FA",
            "title_active_color": "#042A3C",
            "content_color": "#666666",
            "typography_typography": "custom",
            "typography_font_family": "Open Sans",
            "typography_font_weight": "600",
            "typography_font_size": {"unit": "px", "size": 16, "sizes": []},
            "content_typography_typography": "custom",
            "content_typography_font_family": "Open Sans",
            "content_typography_font_size": {"unit": "px", "size": 15, "sizes": []},
            "content_typography_line_height": {"unit": "em", "size": 1.7, "sizes": []},
            "border_color": "#E0E0E0"
        },
        "elements": [],
        "widgetType": "accordion"
    }

def make_heading(title, size=28):
    """Create an Elementor heading widget."""
    return {
        "id": gen_id(),
        "elType": "widget",
        "settings": {
            "title": title,
            "align": "left",
            "title_color": "#042A3C",
            "typography_typography": "custom",
            "typography_font_family": "Manrope",
            "typography_font_size": {"unit": "px", "size": size, "sizes": []},
            "typography_font_weight": "700"
        },
        "elements": [],
        "widgetType": "heading"
    }

def make_divider():
    """Create an Elementor divider widget."""
    return {
        "id": gen_id(),
        "elType": "widget",
        "settings": {"color": "#E0E0E0", "gap": {"unit": "px", "size": 30, "sizes": []}},
        "elements": [],
        "widgetType": "divider"
    }

def generate_faq_schema(faq_tabs):
    """
    Generate a FAQPage schema from accordion tab data.

    Converts Elementor accordion tabs into schema.org FAQPage JSON-LD,
    stripping any HTML from answers for clean structured data.
    """
    import re
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": t["tab_title"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": re.sub(r'<[^>]+>', '', t.get("tab_content", ""))
                }
            }
            for t in faq_tabs
        ]
    }


# ============================================================
# FAQ DATA
# ============================================================

INDUSTRIAL_FAQ_TABS = [
    {
        "_id": gen_id(),
        "tab_title": "What is included in an industrial maintenance contract?",
        "tab_content": "We tailor every contract to the site. A typical contract includes scheduled electrical inspections of switchboards, distribution boards, and equipment at agreed intervals (monthly, quarterly, or six-monthly). It also covers compliance testing including test and tag to AS/NZS 3760, RCD testing, and emergency lighting inspections to AS 2293. Contract clients also get priority response for breakdowns during business hours."
    },
    {
        "_id": gen_id(),
        "tab_title": "How often should industrial electrical equipment be tested and tagged?",
        "tab_content": "Under AS/NZS 3760:2022, the testing frequency depends on your environment. Factories, workshops, and warehouses require testing every 6 months. Construction and demolition sites need testing every 3 months. Offices and retail environments are tested every 12 months. We schedule all testing as part of your maintenance contract so nothing falls overdue."
    },
    {
        "_id": gen_id(),
        "tab_title": "Do you offer emergency breakdown response?",
        "tab_content": "We operate Monday to Friday 7am to 5pm and Saturday 7am to 12pm. We don't offer 24-hour callouts, but maintenance contract clients get priority same-day response during business hours. When you call, your job goes to the front of the queue."
    },
    {
        "_id": gen_id(),
        "tab_title": "What industrial equipment can you repair?",
        "tab_content": "We work on lathes, milling machines, drill presses, bandsaws, CNC machines and controllers, production line equipment, conveyor systems, compressors, pumps, welding equipment, and packaging machinery. Common repairs include motor replacements, control panel repairs, sensor and limit switch replacement, VSD and soft starter installation, and electrical fault finding."
    },
    {
        "_id": gen_id(),
        "tab_title": "Can you work on older industrial machinery?",
        "tab_content": "Yes. We have 15 years of experience with older industrial equipment and understand legacy systems. We can source replacement parts or find alternative solutions when original components are no longer available. We have worked on equipment ranging from brand new to decades old."
    },
    {
        "_id": gen_id(),
        "tab_title": "What areas do you cover for industrial electrical work?",
        "tab_content": "Our core area is Brisbane's western corridor including Wacol, Archerfield, Richlands, Rocklea, Darra, and Acacia Ridge. We also cover Ipswich, Springfield, Goodna, Coopers Plains, Salisbury, and the wider Brisbane region. For larger contracts we service the Gold Coast and Sunshine Coast as well."
    },
    {
        "_id": gen_id(),
        "tab_title": "Are you licensed for three-phase work?",
        "tab_content": "Yes. We hold Queensland Electrical Contractor Licence #85763 which covers all electrical work including three-phase installations, new supply applications, equipment connections and commissioning, and load balancing. We are fully insured and Master Electricians Silver Members."
    },
    {
        "_id": gen_id(),
        "tab_title": "How do RCDs protect workers in industrial settings?",
        "tab_content": "Residual Current Devices (RCDs), also called safety switches, monitor the current flowing through a circuit. If current leaks to earth, which happens when someone touches a live part, the RCD trips within 300 milliseconds to prevent electrocution. Australian workplace safety regulations require RCD protection on all socket outlets. We test RCDs as part of every maintenance contract to make sure they trip correctly."
    }
]

COMPLIANCE_FAQ_TABS = [
    {
        "_id": gen_id(),
        "tab_title": "Can you do all compliance testing in one visit?",
        "tab_content": "Yes. We schedule test and tag, RCD testing, and emergency lighting inspections together so you only have one disruption to your operations. For larger sites we may spread the work across two visits, but we coordinate everything so your compliance stays current."
    },
    {
        "_id": gen_id(),
        "tab_title": "How often should we have compliance testing done?",
        "tab_content": "It depends on your environment. Under AS/NZS 3760:2022, factories and warehouses need test and tag every 6 months. Construction sites every 3 months. Offices annually. RCDs should be push-button tested every 3 months and electrically tested annually. Emergency lighting needs monthly function tests, six-monthly duration tests (90 minutes), and annual full inspections under AS 2293. We set up a schedule that covers everything."
    },
    {
        "_id": gen_id(),
        "tab_title": "What records do you provide after testing?",
        "tab_content": "You get digital compliance reports for all testing carried out, including individual test results for every item. Emergency lighting gets logbook entries as required by AS 2293. All records are easy to store and retrieve for workplace audits, insurance purposes, or safety inspections."
    },
    {
        "_id": gen_id(),
        "tab_title": "What happens if equipment fails testing?",
        "tab_content": "Failed equipment is tagged out of service immediately with a red fail tag. As licensed electricians, we can often repair or replace faulty items on the spot rather than just tagging them and leaving. If a repair requires parts, we will quote the work and get it sorted as quickly as possible."
    },
    {
        "_id": gen_id(),
        "tab_title": "What is the difference between test and tag and RCD testing?",
        "tab_content": "Test and tag covers portable electrical equipment such as power tools, extension leads, and appliances. Each item is visually inspected and electrically tested, then tagged with the test date and next due date. RCD testing is specifically for the safety switches in your switchboard. RCDs are tested to make sure they trip within 300 milliseconds at the correct current. Both are separate requirements under Australian standards."
    },
    {
        "_id": gen_id(),
        "tab_title": "Do you offer ongoing compliance contracts?",
        "tab_content": "Yes. We set up scheduled visits at the correct intervals for your environment, track all due dates, and send reminders before testing expires. This is the easiest way to stay compliant without having to manage it yourself."
    },
    {
        "_id": gen_id(),
        "tab_title": "What does emergency lighting testing involve?",
        "tab_content": "Emergency lighting testing under AS 2293 involves three levels: a monthly function test where each light is briefly activated to confirm it works, a six-monthly duration test where lights run on battery for 90 minutes to verify battery capacity, and an annual full inspection covering all components, mounting, signage, and obstruction of exit paths. We document everything in a logbook."
    },
    {
        "_id": gen_id(),
        "tab_title": "Do you service areas outside Brisbane?",
        "tab_content": "Yes. Our core area is Brisbane's western corridor but we provide compliance testing throughout greater Brisbane, Ipswich, Springfield, Logan, and the Gold Coast. For sites with a large number of items to test, we are happy to travel further. Call us on 0402 336 372 to discuss your location."
    }
]


if __name__ == '__main__':
    os.makedirs(SCHEMA_DIR, exist_ok=True)

    # Generate schema files (these work standalone without page data)
    print("=== Generating Schema JSON ===")

    industrial_schema = generate_faq_schema(INDUSTRIAL_FAQ_TABS)
    compliance_schema = generate_faq_schema(COMPLIANCE_FAQ_TABS)

    schemas = {
        "schema-faq-industrial.json": industrial_schema,
        "schema-faq-compliance.json": compliance_schema,
    }

    for fname, schema in schemas.items():
        filepath = os.path.join(SCHEMA_DIR, fname)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        print(f"  Saved {fname}")

    # Page updates require existing page data files
    # In production, these would be exported from WordPress first
    print("\n=== Page Updates ===")
    print("  (Page updates require *-current.json files exported from WordPress)")
    print("  Run with WordPress MCP to export page data first.")
    print("\nSchema generation complete!")
