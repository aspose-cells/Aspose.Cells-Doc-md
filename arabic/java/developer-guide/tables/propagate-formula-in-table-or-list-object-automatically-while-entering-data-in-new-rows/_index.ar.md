---
title: نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة
type: docs
weight: 980
url: /ar/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، ترغب في أن تنتشر الصيغة في الجدول أو كائن القائمة تلقائيًا إلى صفوف جديدة أثناء إدخال بيانات جديدة. هذا هو السلوك الافتراضي في Microsoft Excel. من أجل تحقيق نفس الشيء باستخدام Aspose.Cells، يرجى استخدام [ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula) كخاصية.
## **نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة**
الكود النموذجي التالي ينشئ جدولًا أو كائن قائمة بحيث تنتشر الصيغة في العمود B تلقائيًا إلى الصفوف الجديدة عند إدخال بيانات جديدة. يُرجى مراجعة [ملف الإكسل الناتج](5472519.xlsx) الذي تم إنشاؤه باستخدام هذا الكود. إذا قمت بإدخال أي رقم في الخلية A3، سترى أن الصيغة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
