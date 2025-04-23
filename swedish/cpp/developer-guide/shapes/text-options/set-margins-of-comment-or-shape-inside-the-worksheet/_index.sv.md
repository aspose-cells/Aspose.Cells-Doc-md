---  
title: Ställ in marginaler för Kommentar eller Form inuti arbetsbladet med C++  
linktitle: Ställ in marginaler för kommentar eller shape i kalkylbladet  
type: docs  
weight: 1500  
url: /sv/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Lär dig hur man ställer in marginaler för kommentarer eller former inuti ett arbetsblad med Aspose.Cells och C++.  
---  

## **Möjliga användningsscenario**  

Aspose.Cells tillåter dig att ställa in marginaler för vilken form eller kommentar som helst med hjälp av [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/)-egenskapen. Denna egenskap returnerar objekt av [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment)-klassen som har olika egenskaper, t.ex. [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), etc., vilka kan användas för att ställa in topp-, vänster-, botten- och högermarginaler.  

## **Ställ in marginaler för kommentar eller shape i kalkylbladet**  

Se följande exempel. Den laddar [exempel-Excel-fil](61767851.xlsx) som innehåller två former. Koden går in i varje form och ställer in deras topp-, vänster-, botten- och högermarginaler. Se [utdata Excel-fil](61767852.xlsx) som genererats av koden och en skärmbild som visar kodens effekt på utdatafilen.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Exempelkod**  

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

