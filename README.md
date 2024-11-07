# Change Log S1.3 (11/7/24, 9:26 AM)
- Added the content and initial structure for contactUs.py, faqs.py, ourStory.py, meetTheRescues.py
- Update home.py with initial image
---
# Change Log S1.2 (11/6/24)
## index.py
- Restored the one important code (`html.Div(id='page_content')`), this was why the pages didn't load lol
## ourStory.py
- Added content in Our Story but only HTML
---
# Change Log S1.1 (11/6/24)
## index.py
- More or less copypaste from the IE 172 Repo
- index.py's app.layout contains the functions `create_header()` and `create_footer()` that are self-explanatory. The `html.Div()` after `dcc.Location()`
- In `displaypage(pathname)`, path names are added for the navbar elements (Adopt, Meet the Rescues, Contact Us, etc.)
- the home.layout and other pages do not appear for some reason
