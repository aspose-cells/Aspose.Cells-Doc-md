---
title: Rotera text med form inuti bladet med C++
linktitle: Rotera Text med Form
type: docs
weight: 1300
url: /sv/cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lär dig hur man kontrollerar textrotation med former i Excel ark med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan lägga till text inuti vilken form som helst med Microsoft Excel. Om du lägger till en form med den mycket gamla Microsoft Excel 2003, kommer texten inte att rotera med formen. Men om du lägger till en form med nyare versioner av Microsoft Excel, såsom 2007, 2010, 2013 eller 2016, kommer texten att rotera med formen. Du kan kontrollera om texten ska rotera med formen eller inte med hjälp av [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/)-egenskapen. Standardvärdet för denna egenskap är **true**, vilket innebär att texten roterar med formen. Om du ställer in det till **false**, roterar inte texten med formen.

## **Rotera text med Shape i kalkylbladet**

Följande exempel laddar [exempel-Excel-filen](64716896.xlsx) som innehåller en triangel och dess text roterar med formen. Om du öppnar exempel-Excel-filen i Microsoft Excel och roterar triangelformen, kommer texten också att rotera med den. Koden ställer sedan in [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/)-egenskapen till **false** och sparar den som [utdata Excel-fil](64716897.xlsx). Om du nu öppnar utdatafilen i Excel och roterar triangelformen kommer inte texten att rotera med den. Se skärmskärmbilder nedan som visar effekten av koden på exempel-Excel-filen för referens.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleRotateTextWithShapeInsideWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add message inside it
    Cell b4 = ws.GetCells().Get(u"B4");
    b4.PutValue(u"Text is not rotating with shape because RotateTextWithShape is false.");

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Access shape text alignment
    ShapeTextAlignment shapeTextAlignment = sh.GetTextBody().GetTextAlignment();

    // Do not rotate text with shape by setting RotateTextWithShape as false
    shapeTextAlignment.SetRotateTextWithShape(false);

    // Save the output Excel file
    wb.Save(outDir + u"outputRotateTextWithShapeInsideWorksheet.xlsx");

    Aspose::Cells::Cleanup();
}
```
