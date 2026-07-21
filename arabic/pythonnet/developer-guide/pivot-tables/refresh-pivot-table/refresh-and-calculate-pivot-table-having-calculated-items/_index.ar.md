---
title: تحديث وحساب جدول البيانات المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 40
url: /ar/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: يظهر هذا المقال كيفية تحديث وحساب جدول الدوران الذي يحتوي على عناصر محسوبة باستخدام Aspose.Cells لـ Python via .NET.
keywords: Aspose.Cells لـ Python Excel، مكتبة Excel Python، تحديث وحساب جدول الدوران مع العناصر المحسوبة
---

{{% alert color="primary" %}}

تدعم الآن Aspose.Cells لـ Python via .NET تحديث وحساب جدول الدوران الذي يحتوي على عناصر محسوبة. يرجى استخدام [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) و [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) كالمعتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة**

يقوم الكود العيني التالي بتحميل [ملف جدول الدوران المصدر](5115238.xlsx) الذي يحتوي على جدول دوران يحتوي على ثلاثة عناصر محسوبة مثل "إضافة"، "تقسيم"، "تقسيم2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم بتحديث وحساب جدول الدوران باستخدام Aspose.Cells لمكتبة Python Excel via .NET APIs وحفظ المصنف بتنسيق PDF. تظهر النتائج في [ملف PDF الناتج](5115229.pdf) أن Aspose.Cells لـ Python via .NET قد قامت بتحديث وحساب جدول الدوران الذي يحتوي على عناصر محسوبة بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel عن طريق وضع القيمة 20 في الخلية D2 يدويا ثم تحديث جدول الدوران عبر مفتاح الاختصار Alt+F5 أو النقر فوق زر تحديث جدول الدوران.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
