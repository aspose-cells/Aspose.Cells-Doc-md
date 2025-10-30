---
title: Texte in SmartArt mit C++ ersetzen
linktitle: Ersetzen Sie Text in SmartArt
type: docs
weight: 1200
url: /de/cpp/replace-text-in-smart-art/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ Text in Smart Art aktualisieren, indem Sie die Eigenschaft Shape.Text setzen.
---

## **Mögliche Verwendungsszenarien**

Smart Art ist eines der Hauptobjekte in einer Arbeitsmappe. Häufig besteht der Bedarf, den Text in Smart Art zu aktualisieren. Aspose.Cells bietet dieses Feature durch Setzen der Eigenschaft [**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/).

Die Beispielquelle kann von folgendem Link heruntergeladen werden:

[SmartArt.xlsx](77496338.xlsx)

## **Beispielcode**

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
{{< app/cells/assistant language="cpp" >}}
