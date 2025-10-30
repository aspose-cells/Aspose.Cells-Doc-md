---
title: Personalizzazione dell XML Ribbon con Python via .NET
linktitle: Personalizzare il Menu di Excel
type: docs
weight: 1500
url: /it/python-net/customizing-the-ribbon-xml/
description: Lettura, scrittura e gestione della personalizzazione XML Ribbon di Excel usando Aspose.Cells for Python via .NET API.
---

{{% alert color="primary" %}} 

Microsoft Office ha sostituito i menu e le barre degli strumenti con una barra multifunzione nella parte superiore della finestra dell'applicazione dal 2007. La barra multifunzione è personalizzabile. 
Aspose.Cells ti permette di:

- Mantenere l'XML Ribbon senza analizzarlo
- Leggere e scrivere l'XML Ribbon senza analizzarlo
- Ottenere e impostare i dati XML Ribbon

Se si desidera modificare il Ribbon XML, è necessario analizzarlo con un analizzatore XML o altro strumento Ribbon XML.

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
