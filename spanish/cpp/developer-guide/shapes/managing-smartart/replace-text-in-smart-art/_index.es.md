---
title: Reemplazar texto en smart art con C++
linktitle: Reemplazar texto en el arte inteligente
type: docs
weight: 1200
url: /es/cpp/replace-text-in-smart-art/
description: Aprenda cómo actualizar el texto en smart art usando Aspose.Cells for C++ estableciendo la propiedad Shape.Text.
---

## **Escenarios de uso posibles**

Smart art es uno de los objetos principales en un libro de trabajo. Muchas veces es necesario actualizar el texto en smart art. Aspose.Cells proporciona esta función configurando la propiedad [**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/).

El archivo fuente de muestra se puede descargar desde el siguiente enlace:

[SmartArt.xlsx](77496338.xlsx)

## **Código de muestra**

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
