---
title: استبعاد أنماط غير مستخدمة أثناء تحويل إكسل إلى HTML باستخدام جولانغ عبر C++
linktitle: استبعاد الأنماط غير المستخدمة
type: docs
weight: 30
url: /ar/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: تعلم كيفية استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

قد تحتوي ملفات Microsoft Excel على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى صيغة HTML، يتم أيضًا تصدير هذه الأنماط غير المستخدمة، مما قد يزيد من حجم HTML. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملف Excel إلى HTML باستخدام خاصية [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/). عند ضبطها على **true**، يتم استبعاد جميع الأنماط غير المستخدمة من HTML الناتج. تعرض الصورة أدناه عينة من نمط غير مستخدم داخل HTML الناتج.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**

يُنشئ الكود النموذجي التالي دفتر عمل ويقوم أيضًا بإنشاء نمط مسمى غير مستخدم. نظرًا لضبط [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) على **true**، لن يتم تصدير هذا النمط المسمى غير المستخدم إلى [HTML الناتج](61767778.zip). ومع ذلك، إذا قمت بضبطه على **false**، فسيكون هذا النمط غير المستخدم موجودًا داخل HTML الناتج، والذي يمكنك رؤيته بعد ذلك في ترميز HTML كما هو موضح في الصورة أعلاه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
