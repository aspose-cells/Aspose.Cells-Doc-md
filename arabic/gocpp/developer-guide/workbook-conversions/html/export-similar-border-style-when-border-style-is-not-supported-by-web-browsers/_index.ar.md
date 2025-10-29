---
title: تصدير نمط حدود مماثل عندما لا يدعم مستعرض الويب نمط الحدود باستخدام جولانغ عبر C++
linktitle: تصدير نفس نمط الحدود عندما لا يتم دعم نمط الحدود بواسطة متصفحات الويب
type: docs
weight: 70
url: /ar/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: تعلم كيفية تصدير أنماط حدود مماثلة عند عدم دعمها بواسطة مستعرضات الويب باستخدام Aspose.Cells مع جولانغ عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

يدعم Microsoft Excel بعض أنواع الحدود المتقطعة التي لا يدعمها متصفحات الويب. عند تحويل ملف إكسل من نوع HTML باستخدام Aspose.Cells، تتم إزالة هذه الحدود. ومع ذلك، يدعم Aspose.Cells أيضًا عرض هذه الحدود مع الخاصية [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/). الرجاء تعيين قيمتها إلى **صحيح** وسيتم تصدير هذه الحدود غير المدعومة أيضًا إلى ملف HTML.

## **تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب**

يحمِّل رمز النموذج التالي ملف إكسل النموذجي (64716806.xlsx) الذي يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة أدناه. توضح لقطة الشاشة أيضًا تأثير الخاصية [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/) داخل ملف HTML الإخراجي (64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
