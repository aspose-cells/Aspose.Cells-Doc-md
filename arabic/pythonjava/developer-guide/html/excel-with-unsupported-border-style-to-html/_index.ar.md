---
title: Excel ذو نمط جانبي غير مدعوم إلى HTML
type: docs
weight: 80
url: /ar/python-java/excel-with-unsupported-border-style-to/
---

## **Excel ذو نمط جانبي غير مدعوم إلى HTML**
يدعم Microsoft Excel بعض أنواع الحدود المتقطعة التي لا تدعمها متصفحات الويب. عند تحويل ملفات من هذا النوع إلى HTML باستخدام Aspose.Cells، يتم إزالة تلك الحدود. ومع ذلك، يدعم Aspose.Cells for Python via Java عرض حدود مماثلة مع خاصية [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle). يمكنك تعيين قيمة [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) إلى **True** لتصدير الحدود غير المدعومة.

يقوم الكود النموذجي التالي بتحميل ملف اكسل عينة (sampleExportSimilarBorderStyle.xlsx) الذي يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح اللقطة أيضًا تأثير خاصية ExportSimilarBorderStyle (https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) داخل الHTML الناتج (outputExportSimilarBorderStyle.zip).

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
