---
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML
type: docs
weight: 30
url: /ar/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **سيناريوهات الاستخدام المحتملة**

ملف Microsoft Excel قد يحتوي على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى تنسيق HTML، يتم تصدير هذه الأنماط غير المستخدمة أيضًا. يمكن أن يزيد ذلك من حجم HTML. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملف Excel إلى HTML باستخدام الخاصية [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles). عندما يتم تعيينها **true**، يتم استبعاد جميع الأنماط غير المستخدمة من مخرج HTML. يعرض اللقطة الشاشة التالية نموذجًا لنمط غير مستخدم داخل مخرج HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**

ينشئ الكود النموذجي التالي دفتر عمل وينشئ أيضًا نمطًا بالاسم غير المستخدم. نظرًا لتعيين [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) على **true**، فإن هذا النمط بالاسم غير المستخدم لن يتم تصديره إلى [مخرج HTML](61767781.zip). ولكن إذا قمت بتعيينها **false**، فسيكون هذا النمط غير المستخدم موجودًا داخل مخرج HTML ويمكنك رؤيته ثمار سوق HTML كما هو موضح في اللقطة الشاشة أعلاه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
