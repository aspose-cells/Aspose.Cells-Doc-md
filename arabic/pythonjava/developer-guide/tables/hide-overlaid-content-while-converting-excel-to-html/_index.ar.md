---
title: إخفاء المحتوى المُتداخل أثناء تحويل Excel إلى HTML
type: docs
weight: 40
url: /ar/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **إخفاء المحتوى المُتداخل أثناء تحويل Excel إلى HTML**
عندما تقوم بحفظ ملف Excel الخاص بك إلى HTML، يمكنك تحديد أنواع مختلفة للاشتراطات لسلاسل الخلايا. بشكل افتراضي، يقوم Aspose.Cells بإنشاء HTML وفقًا لما في Microsoft Excel، ولكن عندما تُغيّر خاصية [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) إلى [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)، فإنه يخفي جميع السلاسل عن يمين الخلية التي تكون متداخلة أو متراكبة مع سلسلة الخلية.

يحمل مقتطف الكود التالي ملف Excel العيّني [الملف العيّني لإخفاء المحتوى المُتداخل مع CROSS_HIDE_RIGHT](sampleHidingOverlaidContentWithCrossHideRight.xlsx) ويقوم بحفظه إلى [HTML الناتج](HTML-outputHidingOverlaidContentWithCrossHideRight.zip) بعد ضبط [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) على [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). يوضح اللقطة الشاشية كيف تؤثر [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) على HTML الناتج من النتج الافتراضي.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
