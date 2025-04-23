---
title: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل
type: docs
weight: 1500
url: /ar/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح لك Aspose.Cells for Python via .NET بتعيين هوامش أي شكل أو تعليق باستخدام خاصية [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment). تُرجع هذه الخاصية كائن من فئة [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment) الذي يمتلك خصائص مختلفة مثل [**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt)، [**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt)، [**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt)، [**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt)، وغيرها، والتي يمكن استخدامها لتعيين الهوامش العلوية، اليسرى، السفلية واليمنى.

## **تعيين هوامش التعليق أو الشكل داخل ورقة العمل**

يرجى الاطلاع على الكود عينة التالي. يقوم بتحميل [ملف Excel عيني](61767851.xlsx) الذي يحتوي على شكلين. يقوم الكود بالوصول إلى الأشكال واحد تلو الآخر ويضبط هوامشها العلوية واليسرى والسفلية واليمنى. يرجى الاطلاع على [ملف Excel الناتج](61767852.xlsx) الذي تم إنشاؤه بواسطة الكود ولقطة شاشة توضح تأثير الكود على ملف Excel الناتج.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
