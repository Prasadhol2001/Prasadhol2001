import os
import sys
import html

def generate_banner_svg(output_svg="terminal-banner.svg", username="Prasadhol2001"):
    width = 860
    height = 110
    
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    
    lines.append('<defs>')
    lines.append('  <style>')
    lines.append('    .banner-bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    lines.append('    .header-dot { rx: 50%; ry: 50%; }')
    lines.append('    .prompt-user { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 13px; fill: #58a6ff; font-weight: bold; }')
    lines.append('    .prompt-host { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 13px; fill: #bc8cff; font-weight: bold; }')
    lines.append('    .cmd-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 14px; fill: #e6edf3; font-weight: 600; }')
    lines.append('    .subtitle-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 14px; fill: #7ee787; font-weight: bold; }')
    lines.append('    .cursor { fill: #58a6ff; }')
    lines.append('  </style>')
    
    # Clip path for typewriter animation
    lines.append('  <clipPath id="type-clip">')
    lines.append(f'    <rect x="0" y="0" width="0" height="{height}">')
    lines.append(f'      <animate attributeName="width" from="0" to="{width}" begin="0.2s" dur="2.8s" fill="freeze" />')
    lines.append('    </rect>')
    lines.append('  </clipPath>')
    lines.append('</defs>')
    
    # Background
    lines.append(f'<rect class="banner-bg" width="{width}" height="{height}" />')
    
    # Window Header
    lines.append('<circle class="header-dot" cx="20" cy="18" r="5" fill="#ff5f56" />')
    lines.append('<circle class="header-dot" cx="35" cy="18" r="5" fill="#ffbd2e" />')
    lines.append('<circle class="header-dot" cx="50" cy="18" r="5" fill="#27c93f" />')
    lines.append(f'<line x1="0" y1="32" x2="{width}" y2="32" stroke="#21262d" stroke-width="1" />')
    
    # Command Line 1
    lines.append('<text class="cmd-text" x="20" y="58">')
    lines.append(f'  <tspan class="prompt-user">{html.escape(username)}</tspan><tspan fill="#8b949e">@</tspan><tspan class="prompt-host">github</tspan><tspan fill="#8b949e"> ~ $ </tspan>')
    lines.append(f'  <tspan fill="#d2a8ff">echo</tspan> <tspan fill="#a5d6ff">"Hi, I&#39;m Prasad Hol! 👋"</tspan>')
    lines.append('</text>')
    
    # Animated Typewriter Subtitle Line 2
    subtitle_text = "> Flutter &amp; Mobile App Developer | Firebase &amp; API Specialist 🚀"
    lines.append('<g clip-path="url(#type-clip)">')
    lines.append(f'  <text class="subtitle-text" x="20" y="90">{subtitle_text}</text>')
    lines.append('</g>')
    
    # Blinking Cursor Block
    lines.append('<rect class="cursor" x="600" y="76" width="10" height="16" rx="1">')
    lines.append('  <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />')
    lines.append('</rect>')
    
    lines.append('</svg>')
    
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Generated Terminal Banner SVG '{output_svg}'.")

if __name__ == "__main__":
    out_file = sys.argv[1] if len(sys.argv) > 1 else "terminal-banner.svg"
    user = sys.argv[2] if len(sys.argv) > 2 else "Prasadhol2001"
    generate_banner_svg(out_file, user)
