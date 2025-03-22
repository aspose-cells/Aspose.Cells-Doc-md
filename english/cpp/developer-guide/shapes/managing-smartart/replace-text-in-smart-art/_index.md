---
title: Replace text in smart art with C++
linktitle: Replace text in smart art
type: docs
weight: 1200
url: /cpp/replace-text-in-smart-art/
description: Learn how to update text in smart art using Aspose.Cells for C++ by setting the Shape.Text property.
---

## **Possible Usage Scenarios**

Smart art is one of the major objects in a workbook. Many times there is a need to update the text in smart art. Aspose.Cells provides this feature by setting the [**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) property.

The sample source file can be downloaded from the following link:

[SmartArt.xlsx](77496338.xlsx)

## **Sample Code**

```c++
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

                for (int k = 0; k < groupedShapes.GetCount(); ++k)
                {
                    Shape smartArtShape = groupedShapes.Get(k);
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