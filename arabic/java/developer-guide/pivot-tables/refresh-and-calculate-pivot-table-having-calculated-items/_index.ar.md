---
title: تحديث وحساب جدول البيانات المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 130
url: /ar/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

تدعم Aspose.Cells الآن تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة. يرجى استخدام [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) و [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) كالعادة لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة**

الكود النموذجي التالي يحمل [ملف الإكسل المصدر](5473428.xlsx) الذي يحتوي على جدول دوري يحتوي على ثلاثة عناصر محسوبة مثل "إضافة"، "قسمة"، "قسمة2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم نقوم بتحديث الجدول الدوري باستخدام واجهات Aspose.Cells وحفظ المصنوعة بتنسيق PDF. النتائج في [ملف PDF الإخراجي](5473431.pdf) تظهر أن Aspose.Cells قام بتحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة بنجاح. يمكنك التحقق من ذلك باستخدام برنامج Microsoft Excel عن طريق وضع القيمة 20 في الخلية D2 يدوياً ومن ثم تحديث الجدول الدوري عبر مفتاح الاختصار Alt+F5 أو النقر فوق زر تحديث الجدول الدوري.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
