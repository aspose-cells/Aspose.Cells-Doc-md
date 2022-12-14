---
title: Excel بنمط حدود غير مدعوم لـ HTML
type: docs
weight: 80
url: /ar/python-java/excel-with-unsupported-border-style-to/
---
## **Excel بنمط حدود غير مدعوم لـ HTML**
Microsoft يدعم Excel نوعًا من الحدود المتقطعة التي لا تدعمها مستعرضات الويب. عندما يتم تحويل هذه الملفات إلى HTML باستخدام Aspose.Cells ، يتم إزالة هذه الحدود. ومع ذلك ، يدعم Aspose.Cells لـ Python عبر Java عرض حدود مماثلة باستخدام[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)منشأه. يمكنك تعيين قيمة[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) الملكية ل**حقيقي**لتصدير حدود غير مدعومة.

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](sampleExportSimilarBorderStyle.xlsx)يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح لقطة الشاشة تأثير[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)الممتلكات داخل[إخراج HTML](outputExportSimilarBorderStyle.zip).

![ما يجب القيام به: image_بديل_نص](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
