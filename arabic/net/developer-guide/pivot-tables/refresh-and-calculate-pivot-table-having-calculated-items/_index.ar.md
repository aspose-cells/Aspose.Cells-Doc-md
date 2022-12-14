---
title: تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 40
url: /ar/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 يدعم Aspose.Cells الآن تحديث وحساب الجدول المحوري باستخدام العناصر المحسوبة. الرجاء استخدام[**PivotTable.RefreshData ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) و[**PivotTable.CaclulateData ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) كالمعتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[ملف اكسل المصدر](5115238.xlsx)الذي يحتوي على جدول محوري يحتوي على ثلاثة عناصر محسوبة مثل "إضافة" و "div" و "div2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم تحديث الجدول المحوري وحسابه باستخدام واجهات برمجة تطبيقات Aspose.Cells وحفظ المصنف بتنسيق PDF. النتائج في[إخراج PDF](5115229.pdf) يوضح أن Aspose.Cells قام بتحديث وحساب الجدول المحوري بعد أن تم حساب العناصر بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel عن طريق وضع القيمة 20 يدويًا في الخلية D2 ثم تحديث الجدول المحوري عبر مفتاح الاختصار Alt + F5 أو النقر فوق الزر "تحديث الجدول المحوري".

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
