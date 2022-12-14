---
title: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ بتنسيق HTML
type: docs
weight: 100
url: /ar/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **سيناريوهات الاستخدام الممكنة**

عند حفظ ملف Excel بتنسيق HTML ، يمكنك تحديد أنواع متقاطعة مختلفة لسلاسل الخلية. بشكل افتراضي ، يقوم Aspose.Cells بإنشاء HTML وفقًا لـ Microsoft Excel ولكن عندما تقوم بتغيير ملف[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)إلى[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)ثم يخفي جميع السلاسل الموجودة على الجانب الأيمن من الخلية والتي تكون متراكبة أو متداخلة مع سلسلة الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ بتنسيق HTML**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716916.xlsx)ويحفظها في[إخراج HTML](64716915.zip)بعد ضبط[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)كما[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). توضح لقطة الشاشة كيف[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)يؤثر على الناتج HTML من الإخراج الافتراضي.

![ما يجب القيام به: image_بديل_نص](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
