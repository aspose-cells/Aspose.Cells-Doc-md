---
title: تحديث وحساب جدول البيانات المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 40
url: /ar/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

تدعم Aspose.Cells الآن تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة. يرجى استخدام [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) و [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) كالمعتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة**

تحميل كود العينة التالي [ملف إكسيل المصدر](5115238.xlsx) الذي يحتوي على جدول محوري يحتوي على ثلاث عناصر محسوبة مثل "إضافة", "قسمة", "قسمة2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم نقوم بتحديث وحساب جدول الجدول المحوري باستخدام واجهات برمجة تطبيقات Aspose.Cells وحفظ المصنف في تنسيق PDF. تظهر النتائج في [ملف PDF الناتج](5115229.pdf) أن Aspose.Cells قام بتحديث وحساب جدول الجدول المحوري الذي يحتوي على العناصر المحسوبة بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel عن طريق وضع القيمة 20 يدوياً في الخلية D2 ومن ثم تحديث جدول الجدول المحوري عبر مفتاح الاختصار Alt+F5 أو النقر فوق زر تحديث جدول الجدول المحوري.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
