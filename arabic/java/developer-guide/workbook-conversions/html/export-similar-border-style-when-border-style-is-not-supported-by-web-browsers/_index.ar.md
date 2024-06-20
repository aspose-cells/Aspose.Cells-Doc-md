---
title: تصدير نفس نمط الحدود عندما لا يتم دعم نمط الحدود بواسطة متصفحات الويب
type: docs
weight: 70
url: /ar/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **سيناريوهات الاستخدام المحتملة**

يدعم Microsoft Excel بعض أنواع الحدود المنقطة التي لا يتم دعهما بواسطة متصفحات الويب. عند تحويل ملف إكسل من هذا النوع إلى HTML باستخدام Aspose.Cells، يتم إزالة مثل هذه الحدود. ومع ذلك، يمكن لـ Aspose.Cells أيضًا دعم عرض حدود مماثلة بخاصية [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle). يُرجى ضبط قيمتها على **true** وسيتم تصدير الحدود غير المدعومة أيضًا إلى ملف HTML.

## **تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب**

يقوم الرمز البريدي التالي بتحميل [ملف Excel عينة](64716832.xlsx) الذي يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح اللقطة الشاشة تأثير خاصية [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) داخل [HTML الناتج](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
