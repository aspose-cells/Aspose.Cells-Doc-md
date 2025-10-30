---
title: Python ile Özelleştirilmiş Ribın XML i via .NET
linktitle: Excel Menüsünü Özelleştirme
type: docs
weight: 1500
url: /tr/python-net/customizing-the-ribbon-xml/
description: Aspose.Cells for Python via .NET API sini kullanarak Excel Ribın XML özelleştirmesini okuyun, yazın ve yönetin.
---

{{% alert color="primary" %}} 

Microsoft Office, Office 2007'den itibaren menüleri ve araç çubuklarını üstteki Ribın ile değiştirdi. RIBIN özelleştirilebilir. 
Aspose.Cells size şu imkanları sağlar:

- Ribın XML'ini parse etmeden tutmak
- Ribın XML'ini parse etmeden okuyup yazmak
- Ribın XML verilerini almak ve ayarlamak

Eğer açılış XML’ni değiştirmek istiyorsanız, XML veri işaretleme aracıları ya da başka bir açılış XML aracı kullanarak, onu işaretleşmelisiniz.

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
