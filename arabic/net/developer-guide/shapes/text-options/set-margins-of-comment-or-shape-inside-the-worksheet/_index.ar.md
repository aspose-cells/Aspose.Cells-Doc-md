---
title: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل
type: docs
weight: 1500
url: /ar/net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

تسمح Aspose.Cells لك بتعيين الهوامش لأي شكل أو تعليق باستخدام الخاصية [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/fontsettingcollection/properties/textalignment)، تعيد هذه الخاصية كائن فئة [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment) الذي يحتوي على خصائص مختلفة مثل [**TopMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/topmarginpt)، [**LeftMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/leftmarginpt)، [**BottomMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/bottommarginpt)، [**RightMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rightmarginpt)، إلخ التي يمكن استخدامها لتحديد هوامش الأعلى، الأيسر، السفلي والأيمن.

## **تعيين هوامش التعليق أو الشكل داخل ورقة العمل**

يرجى الاطلاع على الكود عينة التالي. يقوم بتحميل [ملف Excel عيني](61767851.xlsx) الذي يحتوي على شكلين. يقوم الكود بالوصول إلى الأشكال واحد تلو الآخر ويضبط هوامشها العلوية واليسرى والسفلية واليمنى. يرجى الاطلاع على [ملف Excel الناتج](61767852.xlsx) الذي تم إنشاؤه بواسطة الكود ولقطة شاشة توضح تأثير الكود على ملف Excel الناتج.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
