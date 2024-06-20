---
title: نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة
linktitle: يحدد صيغة الجدول
type: docs
weight: 260
url: /ar/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، تريد وجود صيغة في جدول أو كائن قائمة ينتشر تلقائيًا إلى الصفوف الجديدة أثناء إدخال بيانات جديدة. وهذا هو السلوك الافتراضي في Microsoft Excel. من أجل تحقيق نفس الشيء باستخدام Aspose.Cells، يرجى استخدام خاصية [ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula).
## **نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة**
الشيفرة العينية التالية تنشئ جدولًا أو كائن قائمة بحيث تنتشر الصيغة في العمود B تلقائيًا إلى الصفوف الجديدة عند إدخال بيانات جديدة. يرجى التحقق من [ملف الإكسل الناتج](5115469.xlsx) باستخدام هذه الشيفرة. إذا قمت بإدخال رقم في الخلية A3، سترى أن الصيغة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
