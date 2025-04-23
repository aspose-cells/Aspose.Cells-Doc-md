---
title: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel إلى HTML، يمكنك تحديد أنواع ت cross المختلفة لسلاسل الخلايا. بشكل افتراضي، يُنشئ Aspose.Cells لـ Python via .NET HTML وفقًا لـ Microsoft Excel، ولكن عند تغيير نوع التقاطع إلى [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/)، فإنه يخفي جميع السلاسل على الجانب الأيمن من الخلية التي تم التراكب عليها أو تداخلها مع نص الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى Html**

يحمل الكود العيني التالي [ملف الإكسل العيني](64716894.xlsx) ويقوم بحفظه إلى [HTML مخرج](64716893.zip) بعد ضبط [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) كـ [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/). يشرح لقطة الشاشة كيف يؤثر [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) على مخرج الـ HTML من مخرج الافتراضي.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
