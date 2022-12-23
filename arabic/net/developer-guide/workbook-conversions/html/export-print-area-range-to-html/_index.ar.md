---
title: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/net/export-print-area-range-to/
---
## **سيناريوهات الاستخدام الممكنة**

 هذا سيناريو شائع حيث نحتاج إلى تصدير منطقة الطباعة فقط ، أي نطاق الخلايا المحدد بدلاً من الورقة بأكملها إلى HTML. هذه الميزة متاحة بالفعل لتقديم PDF ، ومع ذلك ، يمكنك الآن تنفيذ هذه المهمة لـ HTML أيضًا. قم أولاً بتعيين منطقة الطباعة في كائن إعداد الصفحة لورقة العمل. في وقت لاحق ، استخدم[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) علم لتصدير النطاق المحدد فقط.

## عينة من الرموز

يؤدي نموذج التعليمات البرمجية التالي إلى تحميل مصنف ثم تصدير منطقة الطباعة إلى HTML. يمكن تنزيل نموذج ملف لاختبار هذه الميزة من الارتباط التالي:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
