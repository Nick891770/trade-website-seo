"""
FAQ Section Builder for WordPress/Elementor

Reads an existing Elementor homepage JSON layout and injects an FAQ accordion
section with structured question-and-answer content. The FAQ content is designed
to match schema markup for Google rich results.

Usage:
    python build-faq.py

Input:
    Reads homepage-fixed.json from the project data directory.

Output:
    Writes homepage-with-faq.json with the FAQ section inserted before
    the contact form.
"""

import json
import os
import random
import string

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')

def gen_id():
    """Generate a random 7-character ID for Elementor elements."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def build_faq_section():
    """
    Build an Elementor-compatible FAQ accordion section.

    Returns a container element with:
    - Section heading
    - Subheading
    - Accordion widget with 6 FAQ items covering common customer questions

    The FAQ content is written to match the corresponding FAQPage schema
    markup, so both the visible content and structured data stay in sync.
    """
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "flex_direction": "column",
            "flex_align_items": "center",
            "padding": {
                "unit": "em",
                "top": "4",
                "right": "2",
                "bottom": "4",
                "left": "2",
                "isLinked": False
            },
            "padding_mobile": {
                "unit": "em",
                "top": "3",
                "right": "1",
                "bottom": "3",
                "left": "1",
                "isLinked": False
            },
            "background_background": "classic",
            "background_color": "#F8F9FA"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "widget",
                "settings": {
                    "title": "Frequently Asked Questions",
                    "header_size": "h2",
                    "align": "center",
                    "typography_typography": "custom",
                    "typography_font_family": "Manrope",
                    "typography_font_size": {"unit": "px", "size": 36, "sizes": []},
                    "typography_font_size_mobile": {"unit": "px", "size": 28, "sizes": []},
                    "typography_font_weight": "700",
                    "__globals__": {
                        "title_color": "globals/colors?id=secondary"
                    },
                    "_margin": {
                        "unit": "px",
                        "top": "0",
                        "right": "0",
                        "bottom": "10",
                        "left": "0",
                        "isLinked": False
                    }
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": gen_id(),
                "elType": "widget",
                "settings": {
                    "title": "Common questions about our electrical services",
                    "header_size": "h3",
                    "align": "center",
                    "typography_typography": "custom",
                    "typography_font_family": "Georgia",
                    "typography_font_size": {"unit": "px", "size": 16, "sizes": []},
                    "typography_font_weight": "300",
                    "typography_text_transform": "capitalize",
                    "title_color": "#949494",
                    "_margin": {
                        "unit": "px",
                        "top": "0",
                        "right": "0",
                        "bottom": "30",
                        "left": "0",
                        "isLinked": False
                    }
                },
                "elements": [],
                "widgetType": "heading"
            },
            {
                "id": gen_id(),
                "elType": "container",
                "settings": {
                    "flex_direction": "column",
                    "content_width": "boxed",
                    "boxed_width": {"unit": "px", "size": 900, "sizes": []},
                    "width": {"unit": "%", "size": 100}
                },
                "elements": [
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "settings": {
                            "tabs": [
                                {
                                    "_id": gen_id(),
                                    "tab_title": "What areas do you service?",
                                    "tab_content": "We are based around Brisbane\u2019s western corridor. Wacol, Archerfield, Richlands, Rocklea, and Darra are our core areas. We also cover Ipswich, Springfield, Goodna, and the wider Brisbane south region. For larger jobs or maintenance contracts, we travel to the Gold Coast and Sunshine Coast as well."
                                },
                                {
                                    "_id": gen_id(),
                                    "tab_title": "How often does electrical equipment need to be tested and tagged?",
                                    "tab_content": "It depends on the environment. Under AS/NZS 3760, factories, workshops, and warehouses need testing every 6 months. Construction sites require testing every 3 months. Offices and retail spaces are tested annually. We send reminders before your next test is due so you don\u2019t have to keep track of it yourself."
                                },
                                {
                                    "_id": gen_id(),
                                    "tab_title": "What is an electrical maintenance contract?",
                                    "tab_content": "A maintenance contract means we visit your site on a regular schedule to inspect, test, and maintain your electrical systems. Rather than calling someone when things break, we catch problems early and fix them before they cause downtime. Contract clients also get priority response when breakdowns do happen."
                                },
                                {
                                    "_id": gen_id(),
                                    "tab_title": "Are you licensed and insured?",
                                    "tab_content": "Yes. We hold Queensland Electrical Contractor Licence #85763 and carry full public liability and professional indemnity insurance. We are also Master Electricians Silver Members."
                                },
                                {
                                    "_id": gen_id(),
                                    "tab_title": "Do you do residential work?",
                                    "tab_content": "We do. While industrial maintenance is our main focus, we handle domestic jobs including powerpoint installations, lighting upgrades, switchboard replacements, smoke alarm compliance, and general electrical repairs."
                                },
                                {
                                    "_id": gen_id(),
                                    "tab_title": "Do you offer emergency callouts?",
                                    "tab_content": "We operate Monday to Friday 7am to 5pm and Saturday 7am to 12pm. We don\u2019t offer 24-hour callouts, but maintenance contract clients get priority same-day response during business hours. Call us on 0402 336 372."
                                }
                            ],
                            "title_color": "#042A3C",
                            "title_background": "#FFFFFF",
                            "title_active_color": "#042A3C",
                            "tab_active_color": "#FFFFFF",
                            "content_color": "#666666",
                            "typography_typography": "custom",
                            "typography_font_family": "Open Sans",
                            "typography_font_weight": "600",
                            "typography_font_size": {"unit": "px", "size": 16, "sizes": []},
                            "content_typography_typography": "custom",
                            "content_typography_font_family": "Open Sans",
                            "content_typography_font_size": {"unit": "px", "size": 15, "sizes": []},
                            "content_typography_line_height": {"unit": "em", "size": 1.7, "sizes": []},
                            "border_color": "#E0E0E0",
                            "border_width": {
                                "unit": "px",
                                "top": "1",
                                "right": "1",
                                "bottom": "1",
                                "left": "1",
                                "isLinked": True
                            }
                        },
                        "elements": [],
                        "widgetType": "accordion"
                    }
                ],
                "isInner": True
            }
        ],
        "isInner": False
    }


if __name__ == '__main__':
    # In production, this reads an existing homepage JSON and injects the FAQ.
    # For demonstration, we just output the FAQ section structure.
    input_file = os.path.join(DATA_DIR, 'homepage-fixed.json')
    output_file = os.path.join(DATA_DIR, 'homepage-with-faq.json')

    if os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())

        faq_section = build_faq_section()

        # Insert FAQ before the quote form (last element)
        data.insert(7, faq_section)

        print(f"Total elements now: {len(data)}")
        for i, el in enumerate(data):
            print(f"  [{i}] id={el['id']}")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False))

        print(f"Saved {output_file}")
    else:
        # Demo mode: just output the FAQ section as standalone JSON
        faq = build_faq_section()
        output_file = os.path.join(SCRIPT_DIR, '..', 'output', 'faq-section-demo.json')
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(faq, f, indent=2, ensure_ascii=False)
        print(f"Demo FAQ section saved to {output_file}")
