---
title: تصدير نفس نمط الحدود عندما لا يتم دعم نمط الحدود بواسطة متصفحات الويب
type: docs
weight: 70
url: /ar/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **سيناريوهات الاستخدام المحتملة**

يدعم Microsoft Excel بعض أنواع الحدود المتقطعة التي لا تتم دعمها بواسطة متصفحات الويب. عند تحويل ملف Excel من هذا النوع إلى HTML باستخدام Aspose.Cells، يتم إزالة هذه الحدود. ومع ذلك، يمكن لـ Aspose.Cells أيضًا دعم عرض مثل هذه الحدود باستخدام خاصية [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle). يرجى ضبط قيمتها كـ **صحيحة** وسيتم تصدير الحدود غير المدعومة أيضًا إلى ملف HTML.

## **تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب**

يحمل الكود العيني التالي [ملف Excel عيني](64716806.xlsx) الذي يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح لقطة الشاشة النتيجة الناتجة من الخاصية [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) داخل [HTML الناتج](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
{{< app/cells/assistant language="csharp" >}}
