---
title: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/java/export-print-area-range-to-html/
---

## سيناريوات الاستخدام المحتملة

هذا هو سيناريو شائع جدًا نحتاج فيه إلى تصدير منطقة الطباعة فقط أي نطاق الخلايا المحدد بدلاً من الورقة بأكملها إلى تحويل HTML. يتوفر هذا الميزة بالفعل لتقديم PDF، ومع ذلك، يمكنك الآن أيضًا القيام بذلك للتنسيق HTML أيضًا. اضبط أولاً منطقة الطباعة في كائن إعداد الصفحة لورقة البيانات. بعد ذلك استخدم الخاصية [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) لتصدير النطاق المحدد فقط.

## كود جافا لتصدير نطاق منطقة الطباعة إلى HTML

الكود العينة التالي يحمل دفتر عمل ثم يقوم بتصدير منطقة الطباعة إلى الـ HTML. يمكن تنزيل ملف الاختبار لهذه الميزة من الرابط التالي:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

{{< app/cells/assistant language="java" >}}
