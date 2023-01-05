---
title: إخفاء المحتوى المتراكب أثناء تحويل Excel إلى HTML
type: docs
weight: 40
url: /ar/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **إخفاء المحتوى المتراكب أثناء تحويل Excel إلى HTML**
عند حفظ ملف Excel في HTML ، يمكنك تحديد أنواع متقاطعة مختلفة لسلاسل الخلية. بشكل افتراضي ، يقوم Aspose.Cells بإنشاء HTML وفقًا لـ Microsoft Excel ولكن عند تغيير[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)إلى[تعبر_إخفاء_حقا](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)ثم يخفي جميع السلاسل الموجودة على الجانب الأيمن من الخلية والتي تكون متراكبة أو متداخلة مع سلسلة الخلية.

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](sampleHidingOverlaidContentWithCrossHideRight.xlsx)ويحفظها في[الإخراج HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)بعد ضبط[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)مثل[تعبر_إخفاء_حقا](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). توضح لقطة الشاشة كيف[تعبر_إخفاء_حقا](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)يؤثر على الإخراج HTML من الإخراج الافتراضي.

![ما يجب القيام به: image_بديل_نص](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
