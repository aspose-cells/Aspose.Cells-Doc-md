---
title: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/python-net/export-print-area-range-to/
---

## **سيناريوهات الاستخدام المحتملة**

هذا هو سيناريو شائع حيث نحتاج إلى تصدير فقط منطقة الطباعة أي نطاق الخلايا المحددة بدلاً من الورقة بأكملها إلى HTML. هذه الميزة متاحة بالفعل لعرض PDF، ومع ذلك، يمكنك الآن القيام بهذه المهمة أيضًا لتنسيق HTML. قم أولاً بتعيين منطقة الطباعة في كائن إعداد الصفحة الخاص بورقة العمل. بعد ذلك، استخدم الرمز [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only) لتصدير النطاق المحدد فقط.

## كود عينة

يقوم الكود العيني التالي بتحميل دفتر عمل ثم يصدر منطقة الطباعة إلى HTML. يمكن تنزيل ملف العينة لاختبار هذه الميزة من الرابط التالي:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
