---
title: نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة
linktitle: يحدد صيغة الجدول
type: docs
weight: 260
url: /ar/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، تريد أن تنتقل صيغة في جدولك أو كائن قائمة تلقائيًا إلى الصفوف الجديدة أثناء إدخال بيانات جديدة. هذا هو السلوك الافتراضي لبرنامج Microsoft Excel. لتحقيق نفس الشيء باستخدام Aspose.Cells for Python via .NET، يرجى استخدام خاصية [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula).

## **نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة**
الشيفرة العينية التالية تنشئ جدولًا أو كائن قائمة بحيث تنتشر الصيغة في العمود B تلقائيًا إلى الصفوف الجديدة عند إدخال بيانات جديدة. يرجى التحقق من [ملف الإكسل الناتج](5115469.xlsx) باستخدام هذه الشيفرة. إذا قمت بإدخال رقم في الخلية A3، سترى أن الصيغة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

