# Trade Business Website SEO Toolkit

A collection of Python scripts and Claude Code configurations that automate SEO for a WordPress/Elementor trade business website. Built for [Laws Electrical Services](https://lawselecservices.com), an electrical contracting business in Brisbane, Australia.

## The Problem

Small trade businesses often have websites that rank poorly because they lack structured data, location-specific content, and consistent SEO practices. Hiring an SEO agency is expensive and often results in generic content that sounds like it was written by a marketing robot rather than someone who actually does the work.

## The Solution

This toolkit automates the repetitive parts of local SEO for a service-area business. Instead of manually creating dozens of location pages, writing FAQ schema by hand, or trying to keep structured data in sync with page content, these scripts handle it programmatically.

The approach combines Python automation for content generation with Claude Code agent configurations that enforce consistent, human-sounding writing across all SEO work.

### What's Included

- **Suburb page generator** -- creates location-specific landing pages at scale with Elementor-compatible JSON layouts, localised content, internal linking, and consistent structure across 18+ suburbs
- **FAQ schema builder** -- injects accordion FAQ sections into Elementor page layouts and generates matching FAQPage schema JSON-LD so visible content and structured data stay in sync
- **Page content updater** -- batch updates multiple pages with expanded FAQ sections, new content blocks, and compliance information, then generates corresponding schema files
- **Structured data examples** -- LocalBusiness (Electrician type) and FAQPage schema JSON-LD ready for implementation via WPCode or Yoast
- **Service page templates** -- content templates following E-E-A-T principles with proper heading hierarchy, keyword targeting, and internal linking strategy
- **Claude Code agent setup** -- CLAUDE.md configuration, custom slash commands, and specialist agents for ongoing SEO work with consistent style enforcement

## Key Features

- **Automated suburb landing page generation** -- define suburb data once, generate consistent Elementor layouts with localised content, CTAs, and internal links
- **FAQ schema markup** -- accordion FAQ sections that match their corresponding FAQPage schema, keeping visible content and structured data in sync
- **LocalBusiness structured data** -- full Electrician-typed schema with credentials, service areas, opening hours, and membership info
- **Service page templates** -- proper heading hierarchy (H1 > H2 > H3), keyword placement, meta descriptions, and internal linking
- **Claude Code agent configuration** -- custom commands (`/seo-audit`, `/suburb-page`, `/schema-generate`, `/content-write`) and a writing style guide that bans AI-sounding language

## Project Structure

```
trade-website-seo/
├── scripts/
│   ├── generate-suburb-pages.py   # Creates location landing pages
│   ├── build-faq.py               # Builds FAQ sections + schema
│   └── update-pages.py            # Batch page updates + schema generation
├── schema/
│   ├── schema-localbusiness.json  # LocalBusiness/Electrician structured data
│   └── schema-faq-homepage.json   # FAQPage schema example
├── content/
│   ├── service-pages/
│   │   └── industrial-electrician-brisbane.md  # Service page template
│   └── suburb-pages/
│       └── electrician-wacol-template.md       # Suburb page template
├── redesign/
│   └── index.html                 # Homepage redesign concept (static HTML/CSS)
├── claude-config/                 # Claude Code configuration (copy to .claude/)
│   ├── CLAUDE.md                  # Agent context + writing style guide
│   ├── settings.json              # Project settings + business context
│   ├── commands/
│   │   ├── seo-audit.md           # /seo-audit command
│   │   ├── suburb-page.md         # /suburb-page command
│   │   ├── schema-generate.md     # /schema-generate command
│   │   └── content-write.md       # /content-write command
│   └── agents/
│       └── seo-specialist.md      # SEO specialist agent definition
├── .gitignore
└── README.md
```

## How It Works

### 1. Suburb Page Generation

Define suburb data (name, description, nearby areas, industrial features) and the script generates Elementor-compatible JSON layouts with:

- Hero section with suburb name and CTA buttons
- Localised introduction mentioning specific industrial areas
- Services section with internal links to main service pages
- "Why Local Matters" section for local SEO signals
- Nearby areas with cross-links to other suburb pages
- CTA section with business details and credentials

```python
python scripts/generate-suburb-pages.py
# Output: one Elementor JSON layout per suburb in output/
```

### 2. FAQ Schema Generation

The FAQ builder creates accordion sections that match their structured data:

```python
python scripts/build-faq.py
# Injects FAQ accordion into Elementor page layout
# FAQ content matches schema-faq-homepage.json exactly
```

### 3. Batch Content Updates

Expand FAQ sections, add new content blocks, and generate matching schema:

```python
python scripts/update-pages.py
# Updates Industrial and Compliance pages with expanded FAQs
# Generates schema-faq-industrial.json and schema-faq-compliance.json
```

### 4. Claude Code SEO Workflow

Copy `claude-config/` contents to `.claude/` in your project, then use custom commands:

```
/seo-audit              # Full technical + content + local SEO audit
/suburb-page Sumner     # Generate a new suburb landing page
/schema-generate homepage local+faq  # Generate schema for a page
/content-write service "test and tag brisbane"  # Write optimised content
```

## Results

Over 4 weeks of implementation on the Laws Electrical website:

- **Pages indexed**: 2 to 23 (homepage, 2 service pages, 18 suburb pages, about us, privacy policy)
- **Schema markup**: LocalBusiness + FAQPage on homepage, FAQPage on 3 service pages
- **Suburb coverage**: 18 location-specific landing pages covering Brisbane western corridor and Ipswich region
- **Content**: 3 service pages with 1000+ words each, FAQ sections on all major pages
- **Technical**: Meta descriptions on all pages, proper heading hierarchy, internal linking network

## Built With

- **Python** -- content generation and Elementor JSON manipulation
- **WordPress/Elementor** -- website platform and page builder
- **Claude Code** -- AI agent for ongoing SEO work with custom commands and style enforcement
- **JSON-LD** -- structured data for Google rich results
- **Yoast SEO** -- meta descriptions and SEO titles
- **WPCode** -- schema markup injection via code snippets

## Context

Built for Laws Electrical Services, an electrical contracting business in Brisbane. Demonstrates how AI tools can automate local SEO for trade businesses -- the kind of work that SEO agencies charge thousands for but often deliver with generic, cookie-cutter content.

The writing style guide in `claude-config/CLAUDE.md` is worth reading on its own. It includes a banned words list, before/after examples, and a simple test: "Would the business owner actually say this to a client?" If the answer is no, the content gets rewritten.

## Adapting for Your Business

To use this toolkit for a different trade business:

1. Update `claude-config/settings.json` with your business details
2. Update `claude-config/CLAUDE.md` with your writing style and banned words
3. Modify `scripts/generate-suburb-pages.py` with your service areas and suburb data
4. Update schema files with your business information
5. Adjust service page templates for your industry

The approach works for any service-area business: plumbers, HVAC, pest control, landscaping, or any trade that serves multiple suburbs.

## Licence

MIT
