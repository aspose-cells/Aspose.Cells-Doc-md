---
title: Lägg till Word Art text med inbyggda stilar med C++
linktitle: Lägg till Word Art Text med Inbyggda Stilar
type: docs
weight: 270
url: /sv/cpp/add-word-art-text-with-built-in-styles/
description: Lär dig hur man lägger till Word Art text med inbyggda stilar med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
 Du kan lägga till Word Art-text med inbyggda stilar med Aspose.Cells. Använd [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/) för detta ändamål.

## **Lägg till Word Art Text med Inbyggda Stilar**
Följande kodexempel lägger till Word Art-texter med olika inbyggda stilar. Vänligen kontrollera [output excel-filen](5115470.xlsx) som genererats med denna kod. Så här ser [output excel-filen](5115470.xlsx) ut i Microsoft Excel.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add Word Art Text with Built-in Styles
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle1, u"Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle2, u"Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle3, u"Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle4, u"Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle5, u"Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "WordArt added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
