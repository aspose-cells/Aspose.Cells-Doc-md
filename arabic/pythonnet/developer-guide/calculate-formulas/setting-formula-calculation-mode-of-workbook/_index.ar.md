---
title: ضبط وضع حساب الصيغ للمستندات باستخدام Python.NET
linktitle: ضبط وضع حساب الصيغ لسجل العمل
type: docs
weight: 110
url: /ar/python-net/setting-formula-calculation-mode-of-workbook/
description: تعلم كيفية تعيين وضع حساب الصيغ (تلقائي، يدوي) في ملفات إكسل باستخدام Aspose.Cells لبايثون via .NET مع دليل خطوة بخطوة وأمثلة على الكود.
keywords: بايثون، Aspose.Cells، إكسل، ملف العمل، وضع حساب الصيغة، تلقائي، يدوي، الإعدادات
---

## ** تعيين وضع حساب الصيغة في ملف العمل**

{{% alert color="primary" %}}

 يوفر ميكروسوفت إكسل ثلاثة أوضاع لحساب الصيغ:
- **تلقائي**: يعيد حساب الصيغ عند كل تغيير وفتح الملف
- **تلقائي باستثناء جداول البيانات**: يعيد حساب الصيغ باستثناء جداول البيانات عند التغييرات
- **يدوي**: يعيد الحساب فقط عندما يطلب المستخدم (F9/CTRL+ALT+F9) أو أثناء الحفظ

{{% /alert %}}

### **تعيين وضع الحساب باستخدام Aspose.Cells**

 يوفر Aspose.Cells لبايثون via .NET إعداد [**formula_settings**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/) من خلال الخاصية [**Workbook.settings**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/settings/). استخدم السمة [**calculation_mode**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/calculation_mode/) للتحكم في سلوك الحساب.

 الأوضاع المتاحة عبر enum [**CalcModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/calcmodetype/):
- `تلقائي`
- `استثناء_جدول_تلقائي`
- `يدوي`

**خطوات التنفيذ:**
1. تحميل دفتر العمل الموجود أو إنشاء نسخة جديدة
الوصول إلى إعدادات دفتر العمل
تعيين وضع الحساب باستخدام `formula_settings.calculation_mode`
حفظ دفتر العمل المعدل

```python
from aspose.cells import Workbook, CalcModeType

# Load source workbook
workbook = Workbook("source.xlsx")

# Configure manual calculation mode
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CalcModeType, SaveFormat

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create a workbook
workbook = Workbook()

# Set the Formula Calculation Mode to Manual
workbook.settings.formula_settings.calculation_mode = CalcModeType.MANUAL

# Save the workbook
output_path = os.path.join(data_dir, "output_out.xlsx")
workbook.save(output_path, SaveFormat.XLSX)
```
