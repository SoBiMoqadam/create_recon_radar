"""HTML reporting using a very small Jinja2 template"""
from jinja2 import Template
from typing import Dict, List

TEMPLATE = """        <html>
<head>
  <meta charset="utf-8" />
  <title>ReconRadar Report - {{ domain }}</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ddd; padding: 8px; }
    th { background: #222; color: white; }
  </style>
</head>
<body>
  <h1>ReconRadar Report — {{ domain }}</h1>
  <h2>Subdomains ({{ subdomains|length }})</h2>
  <ul>
  {% for s in subdomains %}
    <li>{{ s }}</li>
  {% endfor %}
  </ul>

  <h2>Port Scan Results</h2>
  <table>
    <tr><th>Host</th><th>Open Ports</th></tr>
    {% for host, ports in results.items() %}
    <tr>
      <td>{{ host }}</td>
      <td>{{ ports | join(', ') }}</td>
    </tr>
    {% endfor %}
  </table>

</body>
</html>
"""

def render_html_report(domain: str, subdomains: List[str], results: Dict[str, List[int]], out_path: str):
    tpl = Template(TEMPLATE)
    html = tpl.render(domain=domain, subdomains=subdomains, results=results)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
