---
title: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **سيناريوهات الاستخدام المحتملة**

عندما تقوم بحفظ ملف Excel الخاص بك إلى HTML، يمكنك تحديد أنواع عبر مختلفة لسلاسل الخلايا. بشكل افتراضي، يقوم Aspose.Cells بتوليد HTML وفقًا لـ Microsoft Excel ولكن عندما تغير نوع العبر إلى [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)، يخفي جميع السلاسل عند الجانب الأيمن للخلية التي تتداخل أو تتراكب مع سلسلة الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى Html**

يحمل الكود العيني التالي [ملف الإكسل العيني](64716894.xlsx) ويقوم بحفظه إلى [HTML مخرج](64716893.zip) بعد ضبط [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) كـ [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). يشرح لقطة الشاشة كيف يؤثر [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) على مخرج الـ HTML من مخرج الافتراضي.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
{{< app/cells/assistant language="csharp" >}}
