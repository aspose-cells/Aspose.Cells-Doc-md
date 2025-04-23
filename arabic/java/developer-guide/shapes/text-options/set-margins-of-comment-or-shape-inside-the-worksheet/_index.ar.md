---
title: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل
type: docs
weight: 90
url: /ar/java/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

تسمح Aspose.Cells لك بتحديد الهوامش لأي شكل أو تعليق باستخدام الخاصية [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/fontsettingcollection#TextAlignment). تُرجع هذه الخاصية كائن من فئة [**ShapeTextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeTextAlignment) تحتوي على خصائص مختلفة مثل [**TopMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#TopMarginPt)، [**LeftMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#LeftMarginPt)، [**BottomMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#BottomMarginPt)، [**RightMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RightMarginPt) وغيرها يمكن استخدامها لتحديد الهوامش العلوية، اليسرى، السفلية واليمنى.

## **تعيين هوامش التعليق أو الشكل داخل ورقة العمل**

يرجى رؤية الكود العيني التالي. يقوم بتحميل [ملف إكسل عيني](61767867.xlsx) الذي يحتوي على شكلين. يصل الكود إلى الأشكال واحد تلو الآخر ويضبط هوامشها العلوية واليسرى والسفلية واليمنى. يرجى الاطلاع على [ملف إكسل الناتج](61767866.xlsx) الذي تم إنشاؤه بواسطة الكود والصورة العينية التي تظهر تأثير الكود على ملف إكسل الناتج.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
