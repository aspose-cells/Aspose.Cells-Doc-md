---  
title: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل باستخدام C++  
linktitle: تعيين الهوامش للتعليق أو الشكل داخل ورقة العمل  
type: docs  
weight: 1500  
url: /ar/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: تعلم كيفية تعيين هوامش التعليقات أو الأشكال داخل ورقة العمل باستخدام Aspose.Cells مع C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

 تتيح لك Aspose.Cells تعيين هوامش أي شكل أو تعليق باستخدام خاصية [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/). هذه الخاصية ترجع كائن [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) الذي يحتوي على خصائص مختلفة مثل [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/)، وغيرها والتي يمكن استخدامها لتعيين الهوامش العليا، اليسرى، السفلية، اليمنى.  

## **تعيين هوامش التعليق أو الشكل داخل ورقة العمل**  

 يرجى الاطلاع على الكود النموذجي التالي. يقوم بتحميل ملف إكسل نموذجي [sample Excel file](61767851.xlsx) يحتوي على شكلين. يصل الكود إلى الأشكال واحدًا تلو الآخر ويضبط الهوامش العلوية، اليسرى، السفلية، اليمنى. يرجى الاطلاع على ملف إكسل الناتج [output Excel file](61767852.xlsx) الذي تم إنشاؤه بواسطة الكود وصورة لقطة تظهر تأثير الكود على ملف الإكسل الناتج.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **الكود المثالي**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    Workbook workbook(u"sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Iterate through each shape in the worksheet
    for (int32_t i = 0; i < ws.GetShapes().GetCount(); i++)
    {
        Shape sh = ws.GetShapes().Get(i);

        // Access the text alignment
        ShapeTextAlignment txtAlign = sh.GetTextBody().GetTextAlignment();

        // Set auto margin false
        txtAlign.SetIsAutoMargin(false);

        // Set the top, left, bottom and right margins
        txtAlign.SetTopMarginPt(10);
        txtAlign.SetLeftMarginPt(10);
        txtAlign.SetBottomMarginPt(10);
        txtAlign.SetRightMarginPt(10);
    }

    // Save the output Excel file
    workbook.Save(u"outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

