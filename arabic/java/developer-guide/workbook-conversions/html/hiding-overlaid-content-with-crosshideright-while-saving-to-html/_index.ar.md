---
title: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى HTML ، يمكنك تحديد أنواع مختلفة للصليب لسلاسل الخلايا. بشكل افتراضي ، تقوم Aspose.Cells بتوليد HTML وفقًا لـ Microsoft Excel ولكن عندما تقوم بتغيير [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) إلى [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) ، فإنه يخفي جميع السلاسل عند الجانب الأيمن من الخلية المتداخلة أو المتداخلة مع سلسلة الخلايا.

## **إخفاء المحتوى المتداخل باستخدام CrossHideRight أثناء الحفظ إلى HTML**

يقوم الرمز البريدي التالي بتحميل [ملف Excel عينة](64716916.xlsx) وحفظه في [HTML الناتج](64716915.zip) بعد تعيين [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) كـ [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). توضح اللقطة الشاشية كيف يؤثر [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) على HTML الناتج من الإخراج الافتراضي.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
