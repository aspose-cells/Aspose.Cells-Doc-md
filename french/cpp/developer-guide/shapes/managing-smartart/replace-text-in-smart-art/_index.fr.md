---
title: Remplacer le texte dans le smart art avec C++
linktitle: Remplacer le texte dans l art intelligent
type: docs
weight: 1200
url: /fr/cpp/replace-text-in-smart-art/
description: Apprenez comment mettre à jour le texte dans SmartArt en utilisant Aspose.Cells for C++ en définissant la propriété Shape.Text.
---

## **Scénarios d'utilisation possibles**

Le smart art est l’un des objets principaux dans un classeur. Souvent, il est nécessaire de mettre à jour le texte dans le smart art. Aspose.Cells offre cette fonctionnalité en définissant la propriété [**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/).

Le fichier source d'exemple peut être téléchargé à partir du lien suivant :

[SmartArt.xlsx](77496338.xlsx)

## **Code d'exemple**

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
