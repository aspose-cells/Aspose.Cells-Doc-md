---
title: Anpassen des Ribbon XML mit Python via .NET
linktitle: Excel Menü anpassen
type: docs
weight: 1500
url: /de/python-net/customizing-the-ribbon-xml/
description: Lesen, Schreiben und Verwalten der Excel Ribbon XML Anpassung mit Aspose.Cells für Python via .NET API.
---

{{% alert color="primary" %}} 

Microsoft Office hat Menüleisten und Symbolleisten seit Office 2007 durch das Ribbon ersetzt, das oben im Anwendungsfenster erscheint. Das Ribbon ist anpassbar. 
Aspose.Cells ermöglicht es Ihnen, zu:

- Ribbon XML ohne Parsing beibehalten
- Ribbon XML ohne Parsing lesen und schreiben
- Ribbon XML-Daten abrufen und festlegen

Wenn Sie das Ribbon-XML ändern möchten, müssen Sie es mit einem XML-Parser oder einem anderen Ribbon-XML-Tool analysieren.

{{% /alert %}}

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

wb = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
xml_path = os.path.join(data_dir, "CustomUI.xml")

with open(xml_path, 'r') as sr:
    wb.ribbon_xml = sr.read()
```
{{< app/cells/assistant language="python-net" >}}
