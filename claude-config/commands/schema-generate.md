# Schema Markup Generator

Generate and implement JSON-LD schema markup for website pages.

## Instructions

### LocalBusiness Schema (Site-wide)
Generate Electrician-typed LocalBusiness schema including business details, credentials, service areas, opening hours, and membership information. See `schema/schema-localbusiness.json` for the full example.

### Service Schema
For each service page, generate Service schema referencing the LocalBusiness as provider.

### FAQ Schema
For pages with FAQ content, generate FAQPage schema matching the visible accordion content. See `schema/schema-faq-homepage.json` for the format.

### Suburb Page Schema
For location pages, add LocalBusiness with specific areaServed targeting the suburb.

## Implementation

1. Generate the appropriate schema for the specified page
2. Validate using Google's Rich Results Test format
3. Use WordPress MCP to add schema to page (via Yoast or WPCode snippet)
4. Test implementation

## Usage

Specify target page and schema types:
- `/schema-generate homepage local+faq`
- `/schema-generate industrial-page faq`
- `/schema-generate all`
