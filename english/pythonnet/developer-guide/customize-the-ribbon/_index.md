---
title: Customizing the Ribbon XML with Python via .NET
linktitle: Customize Excel Menu
type: docs
weight: 1500
url: /python-net/customizing-the-ribbon-xml/
description: Read, write, and manage Excel Ribbon XML customization using Aspose.Cells for Python via .NET API.
---

{{% alert color="primary" %}} 

Microsoft Office replaced menus and toolbars with a Ribbon at the top of the application window since Office 2007. The Ribbon is customizable. 
Aspose.Cells allows you to:

- Keep Ribbon XML without parsing it
- Read and write Ribbon XML without parsing it
- Get and set Ribbon XML data

If you want to change the Ribbon XML, you have to parse it with an XML parser or other Ribbon XML tool.

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