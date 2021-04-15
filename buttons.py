import markdown

md_text = """
```python hl_lines="1 3"
# some Python code
hi = 'Hello'
print(hi)
```
"""
html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])
print(html)
