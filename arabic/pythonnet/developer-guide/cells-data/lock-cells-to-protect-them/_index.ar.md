---
title: قفل الخلايا لحمايتها باستخدام Python.NET
linktitle: قفل الخلايا لحمايتها
type: docs
weight: 130
url: /ar/python-net/how-to-lock-cells-to-protect-them/
description: تعلم كيفية قفل خلايا معينة وحماية أوراق العمل في ملفات Excel باستخدام Aspose.Cells لبايثون via .NET.
keywords: قفل الخلايا في بايثون، حماية أوراق العمل، حماية الخلايا في Excel باستخدام بايثون، دروس Aspose.Cells لبايثون
---

## **سيناريوهات الاستخدام المحتملة**
قفل الخلايا لحمايتها هو ممارسة شائعة في تطبيقات الجداول، مثل مايكروسوفت إكسل أو جوجل شيتس، للأسباب المهمة التالية:

1. منع التغييرات العرضية: يمكن لقفل الخلايا منع المستخدمين من تعديل البيانات أو الصيغ المهمة عن غير قصد.
2. الحفاظ على سلامة البيانات: التأكد من أن البيانات الحرجة تظل متسقة ودقيقة.
3. الوصولControlled: إدارة أذونات التحرير في البيئات التعاونية.
4. حماية الصيغ: حماية الحسابات الحاسوبية الهامة من التغيير.
5. فرض قواعد العمل: الامتثال لمتطلبات حماية البيانات.
6. توجيه المستخدمين: توفير مناطق تحرير واضحة في جداول البيانات المعقدة.

## **كيفية قفل الخلايا لحمايتها في إكسل**
إليك كيفية قفل الخلايا في Microsoft Excel:

1. اختيار الخلايا لقفلها: اختيار خلايا أو تخطي لقفل الورقة بالكامل.
1. فتح مربع حوار تنسيق الخلايا: النقر بزر الماوس الأيمن > "تنسيق الخلايا" أو Ctrl+1.
<br>
<img src="1.png" width=60% />
1. قفل الخلايا: انتقل إلى علامة التبويب "الحماية" > تحقق من "مقفل" > اضغط على "موافق".
1. حماية ورقة العمل: علامة التبويب "مراجعة" > "حماية ورقة" > تعيين كلمة مرور/أذونات > اضغط على "موافق".
<br>
<img src="2.png" width=60% />

## **كيفية قفل الخلايا لحمايتها باستخدام بايثون**

تمكين حماية الخلايا برمجياً باستخدام Aspose.Cells لبايثون via .NET. اتبع هذه الخطوات:
1. تحميل [ملف العينات](sample.xlsx)
2. فتح جميع الخلايا (لا يتم فرض الحالة المغلقة الافتراضية حتى الحماية)
3. قفل خلايا معينة
4. حماية ورقة العمل لفرض القفل

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **نتيجة الإخراج**
تقوم هذه التنفيذات بقفل الخلايا المحددة (A1 و B2) مع إبقاء الآخرين قابلة للتحرير. حماية ورقة العمل تفرض هذه الإعدادات.

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```
{{< app/cells/assistant language="python-net" >}}
