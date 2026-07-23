import os
import sys
import json
import html

def render_activity_svg(input_json="data/activity.json", output_svg="recent-activity.svg"):
    if not os.path.exists(input_json):
        raise FileNotFoundError(f"'{input_json}' not found. Run fetch_activity.py first.")
        
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    username = data.get("username", "Prasadhol2001")
    events = data.get("events", [])
    
    width = 860
    height = 210
    
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    
    lines.append('<defs>')
    lines.append('  <style>')
    lines.append('    .card-bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    lines.append('    .header-dot { rx: 50%; ry: 50%; }')
    lines.append('    .title-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #8b949e; font-weight: 600; }')
    lines.append('    .activity-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 12px; fill: #c9d1d9; }')
    lines.append('    .date-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #7d8590; }')
    lines.append('    .icon-text { font-size: 13px; }')
    lines.append('  </style>')
    
    # Clip paths for row wipe animations
    for r in range(len(events)):
        begin_t = 0.05 + (r * 0.08)
        lines.append(f'  <clipPath id="act-clip-{r}">')
        lines.append(f'    <rect x="0" y="0" width="0" height="{height}">')
        lines.append(f'      <animate attributeName="width" from="0" to="{width}" begin="{begin_t:.2f}s" dur="0.25s" fill="freeze" />')
        lines.append('    </rect>')
        lines.append('  </clipPath>')
        
    lines.append('</defs>')
    
    # Background
    lines.append(f'<rect class="card-bg" width="{width}" height="{height}" />')
    
    # Header Bar
    lines.append('<circle class="header-dot" cx="20" cy="18" r="5" fill="#ff5f56" />')
    lines.append('<circle class="header-dot" cx="35" cy="18" r="5" fill="#ffbd2e" />')
    lines.append('<circle class="header-dot" cx="50" cy="18" r="5" fill="#27c93f" />')
    lines.append(f'<text class="title-text" x="{width // 2}" y="22" text-anchor="middle">{html.escape(username)}@github ~ $ ./recent_activity.sh</text>')
    lines.append(f'<line x1="0" y1="32" x2="{width}" y2="32" stroke="#21262d" stroke-width="1" />')
    
    start_x = 24
    start_y = 62
    row_height = 28
    
    for i, ev in enumerate(events):
        y_pos = start_y + (i * row_height)
        icon = ev.get("icon", "⚡")
        desc = html.escape(ev.get("description", ""))
        date_str = html.escape(ev.get("date", ""))
        
        lines.append(f'<g clip-path="url(#act-clip-{i})">')
        lines.append(f'  <text class="icon-text" x="{start_x}" y="{y_pos}">{icon}</text>')
        lines.append(f'  <text class="activity-text" x="{start_x + 28}" y="{y_pos}">{desc}</text>')
        lines.append(f'  <text class="date-text" x="{width - 24}" y="{y_pos}" text-anchor="end">{date_str}</text>')
        lines.append('</g>')
        
    lines.append('</svg>')
    
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Rendered Activity SVG '{output_svg}'.")

if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "data/activity.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "recent-activity.svg"
    render_activity_svg(inp, out)
