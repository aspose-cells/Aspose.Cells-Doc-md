---
title: نشر الصيغة في جدول أو قائمة كائن تلقائيًا أثناء إدخال البيانات في صفوف جديدة
type: docs
weight: 980
url: /ar/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **سيناريوهات الاستخدام الممكنة**
 في بعض الأحيان ، تريد أن تنتشر صيغة في الجدول أو كائن القائمة تلقائيًا إلى صفوف جديدة أثناء إدخال بيانات جديدة. هذا هو السلوك الافتراضي لـ Microsoft Excel. من أجل تحقيق نفس الشيء مع Aspose.Cells ، يرجى استخدام[ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)خاصية.
## **نشر الصيغة في جدول أو قائمة كائن تلقائيًا أثناء إدخال البيانات في صفوف جديدة**
يقوم نموذج التعليمات البرمجية التالي بإنشاء جدول أو قائمة كائن بطريقة تنتشر الصيغة الموجودة في العمود B تلقائيًا إلى صفوف جديدة عندما تقوم بإدخال بيانات جديدة. رجاء تاكد من[ملف اكسل الناتج](5472519.xlsx) ولدت مع هذا الرمز. إذا أدخلت أي رقم في الخلية A3 ، فسترى أن الصيغة الموجودة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
