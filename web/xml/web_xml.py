import xml.etree.ElementTree as ET

"""
<root>
    <humans>
        <human>
            <name>Mike</name>
            <age>25</age>
            <sex>M</sex>        
        </human>
        <human>
            <name>Jane</name>
            <age>22</age>
            <sex>F</sex>        
        </human>
    <humans>
</root>
"""

# xmlの作成
# まず、xmlの階層をコードに書かない。
# テンプレートを作って動的に値を埋め込むのが一般
# listの中にクラスを格納し、listを渡すと xmlへ変換するラッパーを使うのより良い方法
root = ET.Element('root')
tree = ET.ElementTree(element=root)

humans = ET.SubElement(root, 'humans')

mike = ET.SubElement(humans, 'human')
mike_name = ET.SubElement(mike, 'name')
mike_age = ET.SubElement(mike, 'age')
mike_sex = ET.SubElement(mike, 'sex')
mike_name.text = 'Mike'
mike_age.text = '25'
mike_sex.text = 'M'

jane = ET.SubElement(humans, 'human')
jane_name = ET.SubElement(jane, 'name')
jane_age = ET.SubElement(jane, 'age')
jane_sex = ET.SubElement(jane, 'sex')
jane_name.text = 'Jane'
jane_age.text = '22'
jane_sex.text = 'F'

tree.write('humans.xml', encoding="utf-8", xml_declaration=True)

# xmlの解析
parse_tree = ET.ElementTree(file='humans.xml')
parse_root = parse_tree.getroot()

for humans in parse_root:
    for human in humans:
        for element in human:
            print(element.tag, element.text)

# 特定の要素の値だけ取得
for name in parse_root.iter('name'):
    print(f"### name = {name.text}")
