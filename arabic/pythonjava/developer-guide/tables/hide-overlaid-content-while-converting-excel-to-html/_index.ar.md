---
title: إخفاء المحتوى المتراكب أثناء تحويل Excel إلى HTML
type: docs
weight: 40
url: /ar/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **إخفاء المحتوى المتراكب أثناء تحويل Excel إلى HTML**
عند حفظ ملف Excel بتنسيق HTML ، يمكنك تحديد أنواع متقاطعة مختلفة لسلاسل الخلية. بشكل افتراضي ، يقوم Aspose.Cells بإنشاء HTML وفقًا لـ Microsoft Excel ولكن عندما تقوم بتغيير ملف[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)إلى[الاعتراض_يخفي_حقا](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)ثم يخفي جميع السلاسل الموجودة على الجانب الأيمن من الخلية والتي تكون متراكبة أو متداخلة مع سلسلة الخلية.

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](sampleHidingOverlaidContentWithCrossHideRight.xlsx)ويحفظها في[إخراج HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)بعد ضبط[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)كما[الاعتراض_يخفي_حقا](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). توضح لقطة الشاشة كيف[الاعتراض_يخفي_حقا](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)يؤثر على ناتج HTML من الإخراج الافتراضي.

![ما يجب القيام به: image_بديل_نص](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
