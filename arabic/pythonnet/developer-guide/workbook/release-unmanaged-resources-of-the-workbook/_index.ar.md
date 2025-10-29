---
title: تحرير الموارد غير المدارة للكتاب باستخدام بايثون via .NET
linktitle: تحرير الموارد غير المدارة
type: docs
weight: 310
url: /ar/python-net/release-unmanaged-resources-of-the-workbook/
description: تعلم كيفية تحرير الموارد غير المدارة بشكل صحيح عند العمل مع ملفات Excel باستخدام Aspose.Cells لبايثون via .NET.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells الطريقة [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) لتحرير الموارد غير المدارة لكائن [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). يُعد هذا النمط حاسمًا للتعامل مع الموارد غير المدارة مثل مقابض الملفات، التدفقات، أو تخصيصات الذاكرة التي لا يديرها جامع القمامة تلقائيًا في بايثون.

{{% /alert %}}

تطبق فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) بروتوكول مدير السياق الخاص ببايثون لإدارة الموارد. يمكنك إما استدعاء الطريقة [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) بشكل صريح أو استخدام عبارة `with` في بايثون لضمان التنظيف الصحيح.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
{{< app/cells/assistant language="python-net" >}}
