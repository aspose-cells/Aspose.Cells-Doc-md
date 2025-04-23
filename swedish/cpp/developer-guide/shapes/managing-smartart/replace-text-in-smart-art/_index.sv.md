---
title: Ersätt text i smart art med C++
linktitle: Ersätt text i Smart Art
type: docs
weight: 1200
url: /sv/cpp/replace-text-in-smart-art/
description: Lär dig hur man uppdaterar text i smart art med Aspose.Cells for C++ genom att sätta egenskapen Shape.Text.
---

## **Möjliga användningsscenario**

Smart art är en av de viktigaste objekten i ett arbetsbok. Ofta finns behov av att uppdatera texten i smart art. Aspose.Cells erbjuder denna funktion genom att sätta egenskapen [**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/).

Den provkällfilen kan laddas ner från följande länk:

[SmartArt.xlsx](77496338.xlsx)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"SmartArt.xlsx";
    U16String outputFilePath = outDir + u"outputSmartArt.xlsx";

    Workbook workbook(inputFilePath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    for (int i = 0; i < worksheets.GetCount(); ++i)
    {
        Worksheet worksheet = worksheets.Get(i);
        ShapeCollection shapes = worksheet.GetShapes();

        for (int j = 0; j < shapes.GetCount(); ++j)
        {
            Shape shape = shapes.Get(j);
            shape.SetAlternativeText(u"ReplacedAlternativeText");

            if (shape.IsSmartArt())
            {
                GroupShape smartArtGroup = shape.GetResultOfSmartArt();
                auto groupedShapes = smartArtGroup.GetGroupedShapes();

                for (int k = 0; k < groupedShapes.GetLength(); ++k)
                {
                    Shape smartArtShape = groupedShapes[k];
                    smartArtShape.SetText(u"ReplacedText");
                }
            }
        }
    }

    OoxmlSaveOptions options;
    options.SetUpdateSmartArt(true);

    workbook.Save(outputFilePath, options);

    std::cout << "SmartArt updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
