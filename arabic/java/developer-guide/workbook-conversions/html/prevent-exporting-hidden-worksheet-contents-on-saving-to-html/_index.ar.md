---
title: منع تصدير محتويات ورقة عمل مخفية عند الحفظ إلى HTML
type: docs
weight: 90
url: /ar/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

يمكنك حفظ سجلات العمل في Excel إلى HTML. ومع ذلك، إذا كانت سجلات العمل تحتوي على أوراق عمل مخفية، فإن Aspose.Cells بشكل افتراضي يصدر محتويات ورقة العمل المخفية إلى دليل الإخراج الخاص ب HTML (_files) الذي يحتوي على ملفات مثل أوراق العمل، الصور، tabstrip.htm، stylesheet.css إلخ. في بعض الأحيان، سيصدر محتوى أوراق العمل المخفية بهذه الطريقة ليس مناسبًا. على سبيل المثال، إذا كانت ورقة العمل المخفية تحتوي على صور يجب عدم تصديرها إلى دليل _files.

{{% /alert %}}

توفر Aspose.Cells خاصية [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet). بشكل افتراضي، يتم تعيين خاصية [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) على **true**. إذا قمت بتعيينها على **false**، فلن يقوم Aspose.Cells بتصدير محتويات ورقة العمل المخفية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

بجانب التحكم في ما إذا كان سيتم تصدير الأوراق العمل المخفية أم لا، يمكنك أيضًا تكوين إعدادات إضافية لتصدير مصنف العمل إلى HTML. توضح المقالات التالية الميزات الأخرى المدعومة من قبل Aspose.Cells لتصدير مصنفات العمل إلى HTML.

- [تحويل Excel إلى HTML مع عناوين](/cells/ar/java/convert-excel-to-html-with-headings/)
- [استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML](/cells/ar/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [تصدير التعليقات أثناء حفظ ملف Excel إلى HTML](/cells/ar/java/export-comments-while-saving-excel-file-to-html/)
- [إخفاء المحتوى المتداخل باستخدام CrossHideRight أثناء الحفظ إلى HTML](/cells/ar/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب](/cells/ar/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
