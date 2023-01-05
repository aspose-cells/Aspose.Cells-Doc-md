---
title: Excel بنمط حد غير مدعوم حتى HTML
type: docs
weight: 80
url: /ar/python-java/excel-with-unsupported-border-style-to/
---
## **Excel بنمط حد غير مدعوم حتى HTML**
Microsoft يدعم Excel نوعًا من الحدود المتقطعة التي لا تدعمها مستعرضات الويب. عند تحويل هذه الملفات إلى HTML باستخدام Aspose.Cells ، يتم إزالة تلك الحدود. ومع ذلك ، يدعم Aspose.Cells for Python via Java عرض حدود مماثلة بـ[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)خاصية. يمكنك تعيين قيمة[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) ملكية ل**حقيقي** لتصدير حدود غير مدعومة.

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](sampleExportSimilarBorderStyle.xlsx)يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح لقطة الشاشة تأثير[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle)الممتلكات داخل[الإخراج HTML](outputExportSimilarBorderStyle.zip).

![ما يجب القيام به: image_بديل_نص](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
