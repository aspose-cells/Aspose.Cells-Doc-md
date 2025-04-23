---
title: تحديث قيم الأشكال المرتبطة
type: docs
weight: 3200
url: /ar/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

أحيانًا، لديك شكل مرتبط في ملف إكسل الخاص بك مرتبط ببعض الخلايا. في ميكروسوفت إكسل، تغيير قيمة الخلية المرتبطة يغيّر أيضًا قيمة الشكل المرتبط. يعمل هذا بشكل جيد مع Aspose.Cells for Python via .NET إذا كنت تريد حفظ دفتر العمل الخاص بك بصيغة XLS أو XLSX. ومع ذلك، إذا كنت تريد حفظ دفتر العمل بصيغة PDF أو HTML، فستحتاج إلى استدعاء طريقة [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) لتحديث قيمة الشكل المرتبط.

{{% /alert %}}

## مثال

يعرض لقطة الشاشة التالية ملف إكسل المصدر المستخدم في رمز العينة أدناه. يحتوي على صورة مرتبطة مرتبطة بالخلايا A1 إلى E4. سنغير قيمة الخلية B4 باستخدام Aspose.Cells لبايثون via .NET ثم نستدعي [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) طريقة لتحديث قيمة الصورة وحفظها بصيغة PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

يمكنك تنزيل الملف الأصلي [ملف الإكسل المصدر](95584291.xlsx) و[PDF الناتج](95584292.pdf) من الروابط المعطاة.

### كود C# لتحديث قيم الأشكال المرتبطة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
