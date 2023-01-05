---
title: قم بتصدير نمط حدود مشابه عندما لا تدعم متصفحات الويب نمط الحدود
type: docs
weight: 70
url: /ar/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **سيناريوهات الاستخدام الممكنة**

Microsoft يدعم Excel نوعًا من الحدود المتقطعة التي لا تدعمها مستعرضات الويب. عند تحويل ملف Excel إلى HTML باستخدام Aspose.Cells ، تتم إزالة هذه الحدود. ومع ذلك ، يمكن أن يدعم Aspose.Cells أيضًا عرض حدود مماثلة بـ[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)خاصية. يرجى تعيين قيمته كـ**حقيقي**وسيتم أيضًا تصدير الحدود غير المدعومة إلى ملف HTML.

## **قم بتصدير نمط حدود مشابه عندما لا تدعم متصفحات الويب نمط الحدود**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716832.xlsx)يحتوي على بعض الحدود غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح لقطة الشاشة تأثير[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)الممتلكات داخل[الإخراج HTML](64716831.zip).

![ما يجب القيام به: image_بديل_نص](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
