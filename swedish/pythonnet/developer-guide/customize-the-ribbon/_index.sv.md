---
title: Anpassa Ribbon XML med Python via .NET
linktitle: Anpassa Excel meny
type: docs
weight: 1500
url: /sv/python-net/customizing-the-ribbon-xml/
description: Läs, skriv och hantera Excel Ribbon XML anpassningar med Aspose.Cells för Python via .NET API.
---

{{% alert color="primary" %}} 

Microsoft Office ersatte menyer och verktygsfält med en Band som finns högst upp i applikationsfönstret sedan Office 2007. Ribbon är anpassningsbar. 
Aspose.Cells tillåter dig att:

- Behålla Ribbon XML utan att parsa den
- Läsa och skriva Ribbon XML utan att parsa den
- Hämta och sätta Ribbon XML-data

Om du vill ändra Ribbon XML måste du analysera den med en XML-parser eller annat Ribbon XML-verktyg.

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
