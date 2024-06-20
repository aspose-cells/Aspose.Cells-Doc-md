---
title: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/net/export-print-area-range-to/
---

## **سيناريوهات الاستخدام المحتملة**

هذا هو سيناريو شائع حيث نحتاج إلى تصدير فقط منطقة الطباعة أي نطاق الخلايا المحددة بدلاً من الورقة بأكملها إلى HTML. هذه الميزة متاحة بالفعل لعرض PDF، ومع ذلك، يمكنك الآن القيام بهذه المهمة أيضًا لتنسيق HTML. قم أولاً بتعيين منطقة الطباعة في كائن إعداد الصفحة الخاص بورقة العمل. بعد ذلك، استخدم الرمز [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) لتصدير النطاق المحدد فقط.

## كود عينة

يقوم الكود العيني التالي بتحميل دفتر عمل ثم يصدر منطقة الطباعة إلى HTML. يمكن تنزيل ملف العينة لاختبار هذه الميزة من الرابط التالي:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
