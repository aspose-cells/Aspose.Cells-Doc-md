---
title: تصدير نفس نمط الحدود عندما لا يتم دعم نمط الحدود بواسطة متصفحات الويب
type: docs
weight: 70
url: /ar/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **سيناريوهات الاستخدام المحتملة**

يدعم Microsoft Excel بعض أنواع الحدود المنقطة التي لا يدعمها متصفحو الويب. عند تحويل مثل هذا الملف Excel إلى HTML باستخدام Aspose.Cells لـ Python via .NET، يتم إزالة هذه الحدود. ومع ذلك، يمكن أيضًا دعم Aspose.Cells لـ Python via .NET لعرض هذه الحدود باستخدام خاصية [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style). يرجى ضبط قيمتها على **true** وسيتم أيضًا تصدير الحدود غير المدعومة إلى ملف HTML.

## **تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب**

يحمل الكود العيني التالي [ملف Excel عيني](64716806.xlsx) الذي يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح لقطة الشاشة النتيجة الناتجة من الخاصية [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) داخل [HTML الناتج](64716804.zip).

![todo:image_alt_text](1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
