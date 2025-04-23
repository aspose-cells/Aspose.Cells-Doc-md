---
title: Personalizando el XML de la Cinta con Python via .NET
linktitle: Personalizar el menú de Excel
type: docs
weight: 1500
url: /es/python-net/customizing-the-ribbon-xml/
description: Leer, escribir y gestionar la personalización del XML de la Cinta de Excel usando la API Aspose.Cells para Python via .NET.
---

{{% alert color="primary" %}} 

Microsoft Office reemplazó menús y barras de herramientas con una Cinta en la parte superior de la ventana de la aplicación desde Office 2007. La Cinta es personalizable. 
Aspose.Cells te permite:

- Mantener el XML de la Cinta sin analizarlo
- Leer y escribir el XML de la Cinta sin analizarlo
- Obtener y establecer datos XML de la Cinta

Si desea cambiar el XML de la cinta, debe analizarlo con un analizador XML u otra herramienta XML de la cinta.

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
