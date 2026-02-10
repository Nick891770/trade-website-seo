"""
Suburb Page Generator for WordPress/Elementor

Generates Elementor-compatible JSON layouts for location-specific landing pages.
Each suburb page follows a consistent template with localised content for SEO.

Usage:
    python generate-suburb-pages.py

Output:
    Creates one JSON file per suburb in the output/ directory, ready for
    import into WordPress via Elementor or the WordPress REST API.
"""

import json
import os

# Use script directory as base path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'output')

suburbs = [
    {"id": 1545, "name": "Wacol", "slug": "wacol", "description": "Wacol is one of Brisbane's largest industrial areas, home to manufacturing plants, warehouses, and distribution centres.", "nearby": "Richlands, Darra, Sumner, Carole Park, Seventeen Mile Rocks, Oxley", "features": "Wacol Industrial Estate, logistics and distribution centres, manufacturing facilities, warehousing operations, food processing plants"},
    {"id": 1546, "name": "Archerfield", "slug": "archerfield", "description": "Archerfield combines aviation, manufacturing, and industrial operations in one of Brisbane's busiest commercial areas.", "nearby": "Rocklea, Salisbury, Moorooka, Coopers Plains, Acacia Ridge, Richlands", "features": "Archerfield Airport precinct, aviation maintenance facilities, manufacturing and engineering works, warehousing and logistics, automotive businesses"},
    {"id": 1547, "name": "Richlands", "slug": "richlands", "description": "Richlands sits at the heart of Brisbane's western industrial corridor, with warehouses, manufacturing plants, and logistics centres.", "nearby": "Wacol, Darra, Inala, Oxley, Seventeen Mile Rocks, Ellen Grove", "features": "Richlands industrial estate, distribution and logistics centres, manufacturing facilities, warehousing operations, trade and automotive businesses"},
    {"id": 1548, "name": "Rocklea", "slug": "rocklea", "description": "Rocklea is home to the Brisbane Markets and a thriving industrial area with food distribution and manufacturing.", "nearby": "Archerfield, Salisbury, Moorooka, Coopers Plains, Acacia Ridge, Yeerongpilly", "features": "Brisbane Markets precinct, food distribution centres, cold storage facilities, manufacturing operations, automotive and trade businesses"},
    {"id": 1549, "name": "Darra", "slug": "darra", "description": "Darra's industrial area hosts manufacturing, logistics, and trade operations along the western corridor.", "nearby": "Wacol, Richlands, Oxley, Seventeen Mile Rocks, Sumner, Jindalee", "features": "Darra industrial estate, manufacturing facilities, distribution centres, trade and automotive businesses, warehousing operations"},
    {"id": 1550, "name": "Acacia Ridge", "slug": "acacia-ridge", "description": "Acacia Ridge is a major logistics and industrial hub in Brisbane's south, with rail freight terminals and distribution centres.", "nearby": "Rocklea, Archerfield, Coopers Plains, Salisbury, Sunnybank, Willawong", "features": "Acacia Ridge industrial estate, rail freight terminals, distribution and logistics centres, manufacturing facilities, trade and automotive businesses"}
]

def create_template(name, slug, description, nearby, features):
    """
    Generate an Elementor-compatible JSON layout for a suburb landing page.

    The template includes:
    - Hero section with suburb name and CTA buttons
    - Introduction with localised business description
    - Services section with internal links to service pages
    - "Why Local Matters" section for local SEO signals
    - Service area section with nearby suburb links
    - CTA section with contact details and licence info
    """
    return [
        {
            "id": "hero001",
            "elType": "section",
            "settings": {
                "background_background": "classic",
                "background_color": "#042A3C",
                "padding": {"unit": "em", "top": "6", "right": "2", "bottom": "6", "left": "2", "isLinked": False},
                "padding_mobile": {"unit": "em", "top": "4", "right": "1", "bottom": "4", "left": "1", "isLinked": False}
            },
            "elements": [
                {
                    "id": "herocol1",
                    "elType": "column",
                    "settings": {"_column_size": 100, "_inline_size": None},
                    "elements": [
                        {
                            "id": "herotitle",
                            "elType": "widget",
                            "settings": {
                                "title": f"Electrician {name}",
                                "align": "center",
                                "title_color": "#FFFFFF",
                                "typography_typography": "custom",
                                "typography_font_family": "Manrope",
                                "typography_font_size": {"unit": "px", "size": 48, "sizes": []},
                                "typography_font_size_mobile": {"unit": "px", "size": 32, "sizes": []},
                                "typography_font_weight": "700"
                            },
                            "elements": [],
                            "widgetType": "heading"
                        },
                        {
                            "id": "herosubtitle",
                            "elType": "widget",
                            "settings": {
                                "title": "Industrial and Commercial Electrical Services",
                                "align": "center",
                                "header_size": "h2",
                                "title_color": "#F5A623",
                                "typography_typography": "custom",
                                "typography_font_family": "Open Sans",
                                "typography_font_size": {"unit": "px", "size": 20, "sizes": []},
                                "typography_font_size_mobile": {"unit": "px", "size": 16, "sizes": []},
                                "typography_font_weight": "400"
                            },
                            "elements": [],
                            "widgetType": "heading"
                        },
                        {
                            "id": "herodesc",
                            "elType": "widget",
                            "settings": {
                                "editor": f"<p>Local electrician servicing {name}'s industrial area. Maintenance contracts, compliance testing, and breakdown repairs.</p>",
                                "align": "center",
                                "text_color": "#FFFFFF",
                                "_padding": {"unit": "%", "top": "0", "right": "15", "bottom": "0", "left": "15", "isLinked": False}
                            },
                            "elements": [],
                            "widgetType": "text-editor"
                        },
                        {
                            "id": "herobtncontainer",
                            "elType": "container",
                            "settings": {
                                "flex_direction": "row",
                                "flex_justify_content": "center",
                                "flex_gap": {"column": "20", "row": "20", "isLinked": True, "unit": "px", "size": 20},
                                "padding": {"unit": "em", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
                            },
                            "elements": [
                                {
                                    "id": "herobtn1",
                                    "elType": "widget",
                                    "settings": {
                                        "text": "Get a Quote",
                                        "link": {"url": "https://lawselecservices.com/#quote", "is_external": "", "nofollow": "", "custom_attributes": ""},
                                        "background_color": "#F5A623",
                                        "button_text_color": "#042A3C",
                                        "border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4", "isLinked": True}
                                    },
                                    "elements": [],
                                    "widgetType": "button"
                                },
                                {
                                    "id": "herobtn2",
                                    "elType": "widget",
                                    "settings": {
                                        "text": "0402 336 372",
                                        "link": {"url": "tel:0402336372", "is_external": "", "nofollow": "", "custom_attributes": ""},
                                        "button_text_color": "#FFFFFF",
                                        "background_color": "transparent",
                                        "border_border": "solid",
                                        "border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
                                        "border_color": "#F5A623",
                                        "border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4", "isLinked": True}
                                    },
                                    "elements": [],
                                    "widgetType": "button"
                                }
                            ],
                            "isInner": True
                        }
                    ],
                    "isInner": False
                }
            ],
            "isInner": False
        },
        {
            "id": "content001",
            "elType": "section",
            "settings": {
                "background_background": "classic",
                "background_color": "#FFFFFF",
                "padding": {"unit": "em", "top": "4", "right": "2", "bottom": "4", "left": "2", "isLinked": False},
                "content_width": {"unit": "px", "size": 1100, "sizes": []}
            },
            "elements": [
                {
                    "id": "contentcol1",
                    "elType": "column",
                    "settings": {"_column_size": 100, "_inline_size": None},
                    "elements": [
                        {
                            "id": "intro001",
                            "elType": "widget",
                            "settings": {
                                "title": f"{name}'s Local Industrial Electrician",
                                "align": "left",
                                "title_color": "#042A3C",
                                "typography_typography": "custom",
                                "typography_font_family": "Manrope",
                                "typography_font_size": {"unit": "px", "size": 32, "sizes": []},
                                "typography_font_weight": "700"
                            },
                            "elements": [],
                            "widgetType": "heading"
                        },
                        {
                            "id": "intro002",
                            "elType": "widget",
                            "settings": {
                                "editor": f"<p>{description} Laws Electrical Services provides ongoing electrical maintenance and repair services to businesses throughout {name}.</p><p>We understand the demands of industrial operations\u2014production schedules, equipment reliability, and compliance requirements. Our maintenance contracts keep your electrical systems running while you focus on your business.</p>",
                                "text_color": "#333333"
                            },
                            "elements": [],
                            "widgetType": "text-editor"
                        },
                        {
                            "id": "divider001",
                            "elType": "widget",
                            "settings": {"color": "#E0E0E0", "gap": {"unit": "px", "size": 30, "sizes": []}},
                            "elements": [],
                            "widgetType": "divider"
                        },
                        {
                            "id": "section001",
                            "elType": "widget",
                            "settings": {
                                "title": f"Our {name} Services",
                                "align": "left",
                                "title_color": "#042A3C",
                                "typography_typography": "custom",
                                "typography_font_family": "Manrope",
                                "typography_font_size": {"unit": "px", "size": 28, "sizes": []},
                                "typography_font_weight": "700"
                            },
                            "elements": [],
                            "widgetType": "heading"
                        },
                        {
                            "id": "section001text",
                            "elType": "widget",
                            "settings": {
                                "editor": "<p><strong>Industrial Maintenance:</strong> Scheduled maintenance contracts, machine breakdown repairs, switchboard upgrades and repairs, three-phase installations, motor and control system repairs.</p><p><strong>Compliance Testing:</strong> <a href=\"/electrical-compliance-testing-brisbane/\">Test and tag</a> (AS/NZS 3760), RCD and safety switch testing, emergency lighting inspections (AS 2293).</p><p><strong>Commercial Electrical:</strong> Office and warehouse lighting, data cabling, safety system installations.</p>",
                                "text_color": "#333333"
                            },
                            "elements": [],
                            "widgetType": "text-editor"
                        },
                        {
                            "id": "divider002",
                            "elType": "widget",
                            "settings": {"color": "#E0E0E0", "gap": {"unit": "px", "size": 30, "sizes": []}},
                            "elements": [],
                            "widgetType": "divider"
                        },
                        {
                            "id": "section002",
                            "elType": "widget",
                            "settings": {
                                "title": "Why Local Matters",
                                "align": "left",
                                "title_color": "#042A3C",
                                "typography_typography": "custom",
                                "typography_font_family": "Manrope",
                                "typography_font_size": {"unit": "px", "size": 28, "sizes": []},
                                "typography_font_weight": "700"
                            },
                            "elements": [],
                            "widgetType": "heading"
                        },
                        {
                            "id": "section002text",
                            "elType": "widget",
                            "settings": {
                                "editor": f"<p>We're based in Brisbane's western corridor and service {name} regularly. This means:</p><ul><li>Fast response times for urgent work</li><li>Knowledge of local industrial operations</li><li>Established relationships with {name} businesses</li><li>No excessive travel charges</li></ul>",
                                "text_color": "#333333"
                            },
                            "elements": [],
                            "widgetType": "text-editor"
                        },
                        {
                            "id": "divider003",
                            "elType": "widget",
                            "settings": {"color": "#E0E0E0", "gap": {"unit": "px", "size": 30, "sizes": []}},
                            "elements": [],
                            "widgetType": "divider"
                        },
                        {
                            "id": "section003",
                            "elType": "widget",
                            "settings": {
                                "title": f"{name} Areas We Service",
                                "align": "left",
                                "title_color": "#042A3C",
                                "typography_typography": "custom",
                                "typography_font_family": "Manrope",
                                "typography_font_size": {"unit": "px", "size": 28, "sizes": []},
                                "typography_font_weight": "700"
                            },
                            "elements": [],
                            "widgetType": "heading"
                        },
                        {
                            "id": "section003text",
                            "elType": "widget",
                            "settings": {
                                "editor": f"<p>We work throughout {name} including: {features}.</p><p><strong>Nearby Areas:</strong> {nearby}</p><p>See our <a href=\"/industrial-electrician-brisbane/\">industrial electrician services</a> for more details on what we offer.</p>",
                                "text_color": "#333333"
                            },
                            "elements": [],
                            "widgetType": "text-editor"
                        }
                    ],
                    "isInner": False
                }
            ],
            "isInner": False
        },
        {
            "id": "cta001",
            "elType": "section",
            "settings": {
                "background_background": "classic",
                "background_color": "#042A3C",
                "padding": {"unit": "em", "top": "4", "right": "2", "bottom": "4", "left": "2", "isLinked": False}
            },
            "elements": [
                {
                    "id": "ctacol1",
                    "elType": "column",
                    "settings": {"_column_size": 100, "_inline_size": None},
                    "elements": [
                        {
                            "id": "ctatitle",
                            "elType": "widget",
                            "settings": {
                                "title": f"Get a Quote for Your {name} Business",
                                "align": "center",
                                "title_color": "#FFFFFF",
                                "typography_typography": "custom",
                                "typography_font_family": "Manrope",
                                "typography_font_size": {"unit": "px", "size": 32, "sizes": []},
                                "typography_font_weight": "700"
                            },
                            "elements": [],
                            "widgetType": "heading"
                        },
                        {
                            "id": "ctatext",
                            "elType": "widget",
                            "settings": {
                                "editor": "<p>Whether you need a one-off repair or an ongoing maintenance contract, we're here to help.</p><p><strong>Laws Electrical Services Pty Ltd</strong><br>Electrical Contractor Licence #85763 | ABN 65 628 378 272</p><p>Mon\u2013Fri: 7am\u20135pm | Sat: 7am\u201312pm</p>",
                                "align": "center",
                                "text_color": "#FFFFFF"
                            },
                            "elements": [],
                            "widgetType": "text-editor"
                        },
                        {
                            "id": "ctabtncontainer",
                            "elType": "container",
                            "settings": {
                                "flex_direction": "row",
                                "flex_justify_content": "center",
                                "flex_gap": {"column": "20", "row": "20", "isLinked": True, "unit": "px", "size": 20},
                                "padding": {"unit": "em", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
                            },
                            "elements": [
                                {
                                    "id": "ctabtn1",
                                    "elType": "widget",
                                    "settings": {
                                        "text": "Request a Quote",
                                        "link": {"url": "https://lawselecservices.com/#quote", "is_external": "", "nofollow": "", "custom_attributes": ""},
                                        "background_color": "#F5A623",
                                        "button_text_color": "#042A3C",
                                        "border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4", "isLinked": True}
                                    },
                                    "elements": [],
                                    "widgetType": "button"
                                },
                                {
                                    "id": "ctabtn2",
                                    "elType": "widget",
                                    "settings": {
                                        "text": "Call 0402 336 372",
                                        "link": {"url": "tel:0402336372", "is_external": "", "nofollow": "", "custom_attributes": ""},
                                        "button_text_color": "#FFFFFF",
                                        "background_color": "transparent",
                                        "border_border": "solid",
                                        "border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
                                        "border_color": "#F5A623",
                                        "border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4", "isLinked": True}
                                    },
                                    "elements": [],
                                    "widgetType": "button"
                                }
                            ],
                            "isInner": True
                        }
                    ],
                    "isInner": False
                }
            ],
            "isInner": False
        }
    ]

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for suburb in suburbs:
        data = create_template(suburb["name"], suburb["slug"], suburb["description"], suburb["nearby"], suburb["features"])
        filename = os.path.join(OUTPUT_DIR, f"elementor-{suburb['slug']}.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'))
        print(f"Created: {suburb['name']} ({suburb['id']})")

    print(f"\nAll suburb pages created in {OUTPUT_DIR}")
