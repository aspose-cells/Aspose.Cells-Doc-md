---
title: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/java/export-print-area-range-to-html/
---
## سيناريوهات الاستخدام الممكنة

هذا سيناريو شائع جدًا نحتاجه لتصدير منطقة الطباعة فقط ، أي نطاق الخلايا المحدد بدلاً من الورقة بأكملها إلى HTML. هذه الميزة متاحة بالفعل لتقديم PDF ، ومع ذلك ، يمكنك الآن تنفيذ هذه المهمة لـ HTML أيضًا. أولاً ، قم بتعيين منطقة الطباعة في كائن إعداد الصفحة بورقة العمل. استخدام في وقت لاحق[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)الخاصية لتصدير النطاق المحدد فقط.

## Java كود لتصدير نطاق منطقة الطباعة إلى HTML

يؤدي نموذج التعليمات البرمجية التالي إلى تحميل مصنف ثم تصدير منطقة الطباعة إلى HTML. يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الارتباط التالي:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

