---  
title: تعيين هوامش التعليق أو الشكل داخل ورقة العمل باستخدام Golang عبر C++  
linktitle: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل  
type: docs  
weight: 1500  
url: /ar/go-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: تعلم كيفية تعيين هوامش التعليقات أو الأشكال داخل ورقة العمل باستخدام Aspose.Cells مع Golang عبر C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

 تتيح لك Aspose.Cells تعيين هوامش أي شكل أو تعليق باستخدام خاصية [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/go-cpp/fontsettingcollection/gettextalignment/). هذه الخاصية ترجع كائن [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) الذي يحتوي على خصائص مختلفة مثل [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/)، وغيرها والتي يمكن استخدامها لتعيين الهوامش العليا، اليسرى، السفلية، اليمنى.  

## **تعيين هوامش التعليق أو الشكل داخل ورقة العمل**  

 يرجى الاطلاع على الكود النموذجي التالي. يقوم بتحميل ملف إكسل نموذجي [sample Excel file](61767851.xlsx) يحتوي على شكلين. يصل الكود إلى الأشكال واحدًا تلو الآخر ويضبط الهوامش العلوية، اليسرى، السفلية، اليمنى. يرجى الاطلاع على ملف إكسل الناتج [output Excel file](61767852.xlsx) الذي تم إنشاؤه بواسطة الكود وصورة لقطة تظهر تأثير الكود على ملف الإكسل الناتج.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **الكود المثالي**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetMarginsOfCommentOrShapeInsideTheWorksheet.go" >}}  
