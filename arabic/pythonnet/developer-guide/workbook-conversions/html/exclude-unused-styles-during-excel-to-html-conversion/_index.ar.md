---
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML
type: docs
weight: 30
url: /ar/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **سيناريوهات الاستخدام المحتملة**

 يمكن أن يحتوي ملف Microsoft Excel على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى تنسيق HTML، يتم تصدير هذه الأنماط غير المستخدمة أيضًا. يمكن زيادة حجم HTML بسبب ذلك. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملف Excel إلى HTML باستخدام الخاصية [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles). عندما تقوم بتعيينها بالقيمة true، يتم استبعاد جميع الأنماط غير المستخدمة من مخرجات HTML. يعرض اللقطة الشاشة التالية عينةً من الأنمطة غير المستخدمة داخل مخرجات HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**

الشيفرة النموذجية التالية تنشئ دفتر عمل وتنشئ أيضًا نمط اسم لم يستخدم. نظرًا لتعيين [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) إلى true، فلن يتم تصدير هذا النمط الاسمي الغير مستخدم إلى [HTML الناتج](61767778.zip). ولكن إذا قمت بتعيينها إلى false، فسيكون هذا النمط الغير المستخدم موجودًا داخل الـHTML الناتج الذي يمكنك رؤيته في العلامة HTML كما هو مبين في اللقطة الشاشة أعلاه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
