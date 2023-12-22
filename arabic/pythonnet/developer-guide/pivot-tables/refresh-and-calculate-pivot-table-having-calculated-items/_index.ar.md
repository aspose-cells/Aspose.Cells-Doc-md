---
title: تحديث وحساب الجدول المحوري الذي يحتوي على العناصر المحسوبة
type: docs
weight: 40
url: /ar/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: توضح هذه المقالة كيفية تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة باستخدام Aspose.Cells for Python via .NET.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET يدعم الآن تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة. الرجاء استخدام[**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) و[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) كالعادة لأداء هذه الوظيفة.

{{% /alert %}}

##  **تحديث وحساب الجدول المحوري الذي يحتوي على العناصر المحسوبة**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[ملف اكسيل المصدر](5115238.xlsx)والذي يحتوي على جدول محوري يحتوي على ثلاثة عناصر محسوبة مثل "add" و"div" و"div2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم نقوم بتحديث وحساب الجدول المحوري باستخدام Aspose.Cells for Python via .NET APIs وحفظ المصنف بتنسيق PDF. النتائج في[الإخراج PDF](5115229.pdf) يظهر أن Aspose.Cells for Python via .NET قام بتحديث وحساب الجدول المحوري بعد حساب العناصر بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel عن طريق وضع القيمة 20 يدويًا في الخلية D2 ثم تحديث الجدول المحوري عبر مفتاح الاختصار Alt + F5 أو النقر فوق زر تحديث الجدول المحوري.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
