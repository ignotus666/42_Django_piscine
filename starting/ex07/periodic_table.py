from pathlib import Path


def parse_elements():
    elements = {}
    file_path = Path(__file__).with_name("periodic_table.txt")
    
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            name, props = line.split(" = ")
            props_dict = {}
            
            for prop in props.split(", "):
                key, value = prop.split(":")
                props_dict[key.strip()] = value.strip()
            
            elements[int(props_dict["number"])] = {
                "name": name,
                "position": int(props_dict["position"]),
                "symbol": props_dict["small"],
                "molar": props_dict["molar"],
                "electron": props_dict["electron"],
            }
    
    return elements


def get_period(atomic_number):
    if 1 <= atomic_number <= 2:
        return 1
    elif 3 <= atomic_number <= 10:
        return 2
    elif 11 <= atomic_number <= 18:
        return 3
    elif 19 <= atomic_number <= 36:
        return 4
    elif 37 <= atomic_number <= 54:
        return 5
    elif 55 <= atomic_number <= 86:
        return 6
    elif 87 <= atomic_number <= 118:
        return 7
    return None


def is_lanthanide(atomic_number):
    return 57 <= atomic_number <= 71


def is_actinide(atomic_number):
    return 89 <= atomic_number <= 103


def get_lanthanide_index(atomic_number):
    return atomic_number - 57 if is_lanthanide(atomic_number) else None


def get_actinide_index(atomic_number):
    return atomic_number - 89 if is_actinide(atomic_number) else None


def generate_cell(element, atomic_number=None):
    if element is None:
        return '<td style="border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9;"></td>'
    
    return f'''<td style="border: 1px solid black; padding: 10px; background-color: #e8f4f8;">
<h4 style="margin: 0 0 10px 0; text-align: center;">{element['name']}</h4>
<ul style="margin: 0; padding-left: 20px;">
<li>No {atomic_number}</li>
<li>{element['symbol']}</li>
<li>{element['molar']}</li>
<li>{element['electron']} electrons</li>
</ul>
</td>'''


def generate_html(elements):
    html_lines = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<title>Periodic Table of Elements</title>',
        '<style>',
        'body { font-family: Arial, sans-serif; margin: 20px; }',
        'h1 { text-align: center; }',
        'table { border-collapse: collapse; margin: 20px 0; }',
        'td { width: 120px; height: 120px; vertical-align: top; }',
        'h4 { margin: 5px; font-size: 14px; }',
        'ul { font-size: 12px; margin: 5px; }',
        '</style>',
        '</head>',
        '<body>',
        '<h1>Periodic Table of the Elements</h1>',
        '<table>',
    ]
    
    # Main table (periods 1-7, excluding lanthanides and actinides separate rows)
    for period in range(1, 8):
        html_lines.append('<tr>')
        
        for col in range(18):
            found = False
            for num, elem in elements.items():
                if get_period(num) == period and elem['position'] == col:
                    if not is_lanthanide(num) and not is_actinide(num):
                        html_lines.append(generate_cell(elem, num))
                        found = True
                        break
            
            if not found:
                html_lines.append(generate_cell(None))
        
        html_lines.append('</tr>')
        
        # Add lanthanides row after period 6
        if period == 6:
            html_lines.append('<tr>')
            html_lines.append('<td colspan="3"></td>')
            for i in range(15):
                for num, elem in elements.items():
                    if get_lanthanide_index(num) == i:
                        html_lines.append(generate_cell(elem, num))
                        break
            html_lines.append('</tr>')
        
        # Add actinides row after period 7
        if period == 7:
            html_lines.append('<tr>')
            html_lines.append('<td colspan="3"></td>')
            for i in range(15):
                for num, elem in elements.items():
                    if get_actinide_index(num) == i:
                        html_lines.append(generate_cell(elem, num))
                        break
            html_lines.append('</tr>')
    
    html_lines.extend([
        '</table>',
        '</body>',
        '</html>',
    ])
    
    return '\n'.join(html_lines)


def main():
    elements = parse_elements()
    html_content = generate_html(elements)
    
    output_file = Path(__file__).with_name("periodic_table.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML file generated: {output_file}")


if __name__ == '__main__':
    main()
