---
title: منع تصدير محتويات ورقة العمل المخفية عند الحفظ إلى HTML
type: docs
weight: 90
url: /ar/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

يمكنك حفظ مصنفات Excel في HTML. ومع ذلك ، إذا كان المصنف يحتوي على أوراق عمل مخفية ، فإن Aspose.Cells يقوم افتراضيًا بتصدير محتويات ورقة العمل المخفية إلى إخراج HTML (_ files) الذي يحتوي على ملفات مثل أوراق العمل والصور و tabstrip.htm و stylesheet.css وما إلى ذلك. في بعض الأحيان ، لا يكون تصدير محتوى أوراق العمل المخفية بهذه الطريقة مناسبًا. على سبيل المثال ، إذا كانت ورقة العمل المخفية تحتوي على صور لا ينبغي تصديرها إلى ملف_دليل الملفات.

{{% /alert %}}

يوفر Aspose.Cells ملف[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) خاصية. بشكل افتراضي ، فإن ملف[**تصدير ورقة العمل المخفية**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) تم تعيين الخاصية على**حقيقي**. إذا قمت بتعيينه على**خاطئة**، فلن يقوم Aspose.Cells بتصدير محتويات ورقة العمل المخفية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

بخلاف التحكم في تصدير أوراق العمل المخفية أم لا ، يمكنك أيضًا تكوين إعدادات إضافية لتصدير المصنف إلى HTML. توضح المقالات التالية الميزات الأخرى التي يدعمها Aspose.Cells لتصدير المصنفات إلى HTML.

- [تحويل Excel إلى HTML بالعناوين](/cells/ar/java/convert-excel-to-html-with-headings/)
- [استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML](/cells/ar/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [تصدير التعليقات أثناء حفظ ملف Excel في HTML](/cells/ar/java/export-comments-while-saving-excel-file-to-html/)
- [إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML](/cells/ar/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [قم بتصدير نمط حدود مشابه عندما لا تدعم متصفحات الويب نمط الحدود](/cells/ar/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
