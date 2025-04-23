---
title: C++ ile akıllı sanata metin değiştirme
linktitle: Akıllı sanatta metni değiştir
type: docs
weight: 1200
url: /tr/cpp/replace-text-in-smart-art/
description: Aspose.Cells for C++ kullanarak akıllı sanattaki metni güncellemek için Shape.Text özelliğinin nasıl ayarlanacağını öğrenin.
---

## **Olası Kullanım Senaryoları**

Akıllı sanat, çalışma kitabındaki ana nesnelerden biridir. Çoğu zaman akıllı sanattaki metni güncellemek gerekebilir. Aspose.Cells, bu özelliği [**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) özelliğini ayarlayarak sağlar.

Örnek kaynak dosyası aşağıdaki bağlantıdan indirilebilir:

[SmartArt.xlsx](77496338.xlsx)

## **Örnek Kod**

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
