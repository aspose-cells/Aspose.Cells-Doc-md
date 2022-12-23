---
title: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---
## **سيناريوهات الاستخدام الممكنة**

عند حفظ ملف Excel في HTML ، يمكنك تحديد أنواع متقاطعة مختلفة لسلاسل الخلية. بشكل افتراضي ، يقوم Aspose.Cells بإنشاء HTML وفقًا لـ Microsoft Excel ولكن عند تغيير نوع التقاطع إلى[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)، ثم يخفي جميع السلاسل الموجودة على الجانب الأيمن من الخلية والتي تكون متراكبة أو متداخلة مع سلسلة الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ في Html**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716894.xlsx) ويحفظها في[الإخراج HTML](64716893.zip) بعد ضبط[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)مثل[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). توضح لقطة الشاشة كيف[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)يؤثر على الإخراج HTML من الإخراج الافتراضي.

![ما يجب القيام به: image_بديل_نص](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
