---
title: Tiling di immagine come texture all’interno della forma con C++
linktitle: Immagine del piastrella come texture all interno della forma
type: docs
weight: 1700
url: /it/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Impara come tiling di un immagine come texture all’interno di una forma usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando l'immagine è piccola e non copre l'intera superficie della forma senza perdere la sua qualità, hai l'opzione di piastrellarla. La piastrellatura riempie la superficie della forma con un'immagine piccola ripetendola come se fossero piastrelle.

## **Immagine del piastrella come texture all'interno della forma**

È possibile riempire la superficie della forma con un'immagine e ripetere l'immagine utilizzando la proprietà [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) e impostandola su **true**. Si prega di vedere il seguente codice di esempio, il [file Excel di esempio](46465050.xlsx) e la schermata per un riferimento.

## **Screenshot**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
