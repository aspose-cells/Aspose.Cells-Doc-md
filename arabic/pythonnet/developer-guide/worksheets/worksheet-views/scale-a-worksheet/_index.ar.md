---
title: كيفية تكبير ورقة عمل باستخدام Python.NET
linktitle: كيفية تكبير ورقة عمل
type: docs
weight: 130
url: /ar/python-net/how-to-scale-a-worksheet/
description: توضح هذه المقالة كيفية تكبير ورقة العمل باستخدام Aspose.Cells for Python.NET.
keywords: تكبير ورقة العمل باستخدام بايثون، تكبير ورقة العمل بواسطة Python.NET، الملاءمة للطباعة في بايثون، نسبة تكبير ورقة العمل في بايثون، تكبير ورقة العمل باستخدام Aspose.Cells في بايثون.
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون تكبير ورقة العمل مفيدًا لأسباب متعددة، اعتمادًا على السياق الذي تعمل فيه. إليك بعض الأسباب الشائعة لتكبير ورقة العمل:
1. **الملاءمة للصفحة**: لضمان أن جميع المحتوى يناسب صفحة واحدة أو عدد محدد من الصفحات عند الطباعة.
1. **العرض**: لإنشاء أوراق عمل منظمة وذات مظهر احترافي للمشاركة.
1. **سهولة القراءة**: لضبط حجم النص والعناصر لتحسين الوصول البصري.
1. **إدارة المساحة**: لتحسين تخطيط ورقة العمل وتقليل الفراغ الأبيض غير الضروري.
1. **تصور البيانات**: لضبط حجم الرسوم البيانية والمخططات بشكل مناسب ضمن المساحة المتاحة.
1. **الاتساق**: للحفاظ على مظهر موحد عبر عدة أوراق عمل أو مستندات.

## **كيفية تكبير ورقة عمل في Excel**
يساعد تكبير ورقة عمل في إكسل على ملاءمة المحتوى على الصفحات المحددة عند الطباعة. اتبع هذه الخطوات:

1. افتح ورقة العمل في إكسل
1. انتقل إلى **تخطيط الصفحة** > مجموعة **التحجيم ليناسب**
1. قم بضبط **العرض** و **الارتفاع** لتلبية متطلبات عدد الصفحات
1. حدد نسبة تحجيم مخصصة إذا لزم الأمر
<br>
<img src="1.png" width=60% />

## **كيفية تكبير ورقة عمل باستخدام Python.NET**
توفر Aspose.Cells for Python.NET قدرات تكبير ورقة العمل بشكل شامل. استخدم هذه الطرق لتحجيم أوراق العمل برمجياً:

### **مثال على ملائمة للصفحة**
ضبط إعدادات الطباعة لتناسب المحتوى على الصفحات المحددة:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **مثال على التحجيم بنسبة مئوية**
تطبيق نسبة مقياس مخصصة لمحتويات ورقة العمل:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**مراجع API الرئيسية:**
- فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
- فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)
- تكوين [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)
