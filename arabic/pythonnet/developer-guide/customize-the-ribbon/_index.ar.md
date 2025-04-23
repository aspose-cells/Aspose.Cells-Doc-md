---
title: تخصيص XML الشريط باستخدام بايثون via .NET
linktitle: تخصيص قائمة Excel
type: docs
weight: 1500
url: /ar/python-net/customizing-the-ribbon-xml/
description: قراءة وكتابة وإدارة تخصيص XML الشريط في إكسل باستخدام Aspose.Cells لواجهة برمجة التطبيقات بايثون via .NET.
---

{{% alert color="primary" %}} 

استبدلت Microsoft Office القوائم وأشرطة الأدوات بشريط في أعلى نافذة التطبيق منذ Office 2007. يمكن تخصيص الشريط. 
تتيح لك Aspose.Cells:

- الاحتفاظ بـ XML الشريط بدون تحليله
- قراءة وكتابة XML الشريط بدون تحليله
- الحصول على وتعيين بيانات XML الشريط

إذا كنت ترغب في تغيير رمز الشريط XML، عليك تحليله باستخدام محلل XML أو أداة أخرى لرمز الشريط XML.

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
