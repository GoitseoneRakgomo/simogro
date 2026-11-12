# Simogro Corp website

The site is a Flask application that renders the corporate home page and
standalone privacy, terms, and cookie-settings pages from Jinja templates. It
serves styles and media from Flask's static-file directory.

The visual design uses Cormorant SC for headings and Quicksand for body copy.
Page content and cards reveal as they enter the viewport; reduced-motion
preferences are respected.

The introductory loading screen clears when the page loads (with a five-second
fallback). The cookie-consent banner remembers accept/reject choices in
browser local storage, and preferences can be changed on the cookie-settings
page. No analytics or advertising cookies are currently configured.

## Requirements

- Python 3.10 or newer
- pip

## Run locally

From the project directory, create and activate a virtual environment, then
install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the development server:

```powershell
flask --app app run --debug
```

Open <http://127.0.0.1:5000/> in a browser. The Flask development server is for
local development; use a production WSGI server for deployment.

## Project layout

```text
app.py                  Flask application and routes
templates/
  _footer.html          Shared footer and policy navigation
  base.html             Shared HTML document layout
  index.html            Main page template
  policy.html           Shared template for policy pages
static/
  style.css             Site styles
  assets/               Images and favicon
requirements.txt        Python dependencies
```

## Publication notes

- Verify the legal company name, jurisdiction, registered office, and any
  registration details required before publication.
- Confirm historical activity descriptions and that the site does not imply
  unapproved financial or regulated services.
- Confirm `hello@simogro.com` is monitored.
- The included crest image is a local visual fallback, not an official Canva
  master export. Replace it with an approved brand asset before publication.
- The privacy and terms text is preliminary and should be reviewed by legal
  counsel.

## Content references

- The Wayback listing supplied for the original site could not be fetched in the available web client; no claim is made that a Wayback snapshot was directly reviewed.
- 2022 source material: [Simogro Corp Website Content PDF](https://drive.google.com/file/d/1hywVV3oU2AKQr2jDFOYbmWlj_nr_ZZCw/view)
- 2026 editorial direction: [Simogro website content (June 2026)](https://docs.google.com/document/d/1RzNGFiaOkqAeP_q-q6LePZ52lnA7x6476lX0Nc_CifU/edit)
- [Additional historical material](https://docs.google.com/document/d/11KtXWDHVaBXFgdQnkNhX9z77ok4VDp3juSpySWJGzEA/edit) and [additional background](https://docs.google.com/document/d/1-eLvjJsOC5sIVIu852VNOA_tmXUVdeEtZR-81zd0B5A/edit)
- [Canva brand kit and official logo design](https://www.canva.com/design/DAGu2ClDDvM/view) and [font pairing options](https://www.canva.com/design/DAGvtUBjNeg/view)

The brand kit did not expose a permanent high-resolution logo export or exact
font and color tokens. The included crest is a local visual fallback matching
the previously approved screenshot, not an official Canva master export. The
CSS font and color choices reflect the approved image and original project;
exact brand-token verification remains pending.
