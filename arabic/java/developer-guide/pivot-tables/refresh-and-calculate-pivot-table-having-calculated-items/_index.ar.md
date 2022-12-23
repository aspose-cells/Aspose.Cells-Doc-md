---
title: تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 130
url: /ar/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 يدعم Aspose.Cells الآن تحديث وحساب الجدول المحوري باستخدام العناصر المحسوبة. الرجاء استخدام[**PivotTable.refreshData ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) و[**PivotTable.caclulateData ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) كالمعتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[ملف اكسل المصدر](5473428.xlsx)الذي يحتوي على جدول محوري يحتوي على ثلاثة عناصر محسوبة مثل "إضافة" و "div" و "div2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم تحديث الجدول المحوري وحسابه باستخدام واجهات برمجة تطبيقات Aspose.Cells وحفظ المصنف بتنسيق PDF. النتائج في[الإخراج PDF](5473431.pdf) يوضح أن Aspose.Cells قام بتحديث وحساب الجدول المحوري بعد أن تم حساب العناصر بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel عن طريق وضع القيمة 20 يدويًا في الخلية D2 ثم تحديث الجدول المحوري عبر مفتاح الاختصار Alt + F5 أو النقر فوق الزر "تحديث الجدول المحوري".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
