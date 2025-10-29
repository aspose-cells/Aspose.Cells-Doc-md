---
title: Заменить текст в smart art с помощью C++
linktitle: Замена текста в умном изображении
type: docs
weight: 1200
url: /ru/cpp/replace-text-in-smart-art/
description: Узнайте, как обновить текст в smart art, используя Aspose.Cells for C++, устанавливая свойство Shape.Text.
---

## **Возможные сценарии использования**

Smart art — один из основных объектов в рабочей книге. Часто возникает необходимость обновить текст в smart art. Aspose.Cells предоставляет эту функцию, устанавливая свойство [**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/).

Образец исходного файла можно загрузить по следующей ссылке:

[SmartArt.xlsx](77496338.xlsx)

## **Образец кода**

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
