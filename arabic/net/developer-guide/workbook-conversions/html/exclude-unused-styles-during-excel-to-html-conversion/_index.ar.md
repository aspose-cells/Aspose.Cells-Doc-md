---
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML
type: docs
weight: 30
url: /ar/net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **سيناريوهات الاستخدام المحتملة**

 يمكن أن يحتوي ملف Microsoft Excel على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى تنسيق HTML، يتم تصدير هذه الأنماط غير المستخدمة أيضًا. يمكن زيادة حجم HTML بسبب ذلك. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملف Excel إلى HTML باستخدام الخاصية [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles). عندما تقوم بتعيينها بالقيمة true، يتم استبعاد جميع الأنماط غير المستخدمة من مخرجات HTML. يعرض اللقطة الشاشة التالية عينةً من الأنمطة غير المستخدمة داخل مخرجات HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**

الشيفرة النموذجية التالية تنشئ دفتر عمل وتنشئ أيضًا نمط اسم لم يستخدم. نظرًا لتعيين [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) إلى true، فلن يتم تصدير هذا النمط الاسمي الغير مستخدم إلى [HTML الناتج](61767778.zip). ولكن إذا قمت بتعيينها إلى false، فسيكون هذا النمط الغير المستخدم موجودًا داخل الـHTML الناتج الذي يمكنك رؤيته في العلامة HTML كما هو مبين في اللقطة الشاشة أعلاه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
