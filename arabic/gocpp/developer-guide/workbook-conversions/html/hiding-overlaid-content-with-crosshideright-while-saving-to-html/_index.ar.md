---
title: إخفاء المحتوى المتداخل باستخدام CrossHideRight عند الحفظ إلى HTML باستخدام جولانغ عبر C++
linktitle: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: استخدم CrossHideRight مع Aspose.Cells في C++ لإخفاء المحتوى المتداخل عند الحفظ إلى HTML.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل إلى HTML، يمكنك تحديد أنواع تقاطع مختلفة لنصوص الخلايا. بشكل افتراضي، يُولد Aspose.Cells HTML حسب Microsoft Excel، ولكن عندما تغير نوع التقاطع إلى [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype)، فإنه يخفي جميع النصوص على الجانب الأيمن من الخلية التي تتداخل أو تتداخل مع نص الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى Html**

يحمِّل رمز النموذج التالي ملف إكسل النموذجي (64716894.xlsx) ويحفظه إلى [الإخراج HTML](64716893.zip) بعد تعيين [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/) إلى [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). يوضح لقطة الشاشة كيف يؤثر [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) على الإخراج HTML من الإخراج الافتراضي.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
