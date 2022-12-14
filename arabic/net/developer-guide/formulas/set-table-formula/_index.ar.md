---
title: نشر الصيغة في جدول أو قائمة كائن تلقائيًا أثناء إدخال البيانات في صفوف جديدة
linktitle: يعين صيغة الجدول
type: docs
weight: 260
url: /ar/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **سيناريوهات الاستخدام الممكنة**
 في بعض الأحيان ، تريد أن تنتشر صيغة في الجدول أو كائن القائمة تلقائيًا إلى صفوف جديدة أثناء إدخال بيانات جديدة. هذا هو السلوك الافتراضي لـ Microsoft Excel. من أجل تحقيق نفس الشيء مع Aspose.Cells ، يرجى استخدام[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)منشأه.
## **نشر الصيغة في جدول أو قائمة كائن تلقائيًا أثناء إدخال البيانات في صفوف جديدة**
يقوم نموذج التعليمات البرمجية التالي بإنشاء جدول أو قائمة كائن بطريقة تنتشر الصيغة الموجودة في العمود B تلقائيًا إلى صفوف جديدة عندما تقوم بإدخال بيانات جديدة. رجاء تاكد من[ملف اكسل الناتج](5115469.xlsx) ولدت مع هذا الرمز. إذا أدخلت أي رقم في الخلية A3 ، فسترى أن الصيغة الموجودة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
