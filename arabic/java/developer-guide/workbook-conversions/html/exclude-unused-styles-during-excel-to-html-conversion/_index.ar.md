---
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML
type: docs
weight: 30
url: /ar/java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **سيناريوهات الاستخدام الممكنة**

Microsoft قد يحتوي ملف Excel على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى تنسيق HTML ، يتم أيضًا تصدير هذه الأنماط غير المستخدمة. يمكن أن يؤدي ذلك إلى زيادة حجم HTML. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملف Excel إلى HTML باستخدام[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)خاصية. عندما تقوم بتعيينه**حقيقي**، يتم استبعاد جميع الأنماط غير المستخدمة من الإخراج HTML. تعرض لقطة الشاشة التالية عينة من النمط غير المستخدم داخل الإخراج HTML.

![ما يجب القيام به: image_بديل_نص](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**

يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف كما يقوم أيضًا بإنشاء نمط مسمى غير مستخدم. منذ[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)تم تعيينه على**حقيقي**، لذلك لن يتم تصدير هذا النمط المسمى غير المستخدم إلى[الإخراج HTML](61767781.zip). ولكن إذا قمت بتعيينه**خاطئة**، فسيكون هذا النمط غير المستخدم موجودًا داخل الإخراج HTML والذي يمكنك رؤيته بعد ذلك في ترميز HTML كما هو موضح في لقطة الشاشة أعلاه.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
