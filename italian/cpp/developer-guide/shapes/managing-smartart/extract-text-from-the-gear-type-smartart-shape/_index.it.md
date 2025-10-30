---
title: Estrai testo da SmartArt di tipo Gear con C++
linktitle: Estrarre il testo dalla forma di Arte intelligente di tipo Gear
type: docs
weight: 500
url: /it/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Impara come estrarre testo da forme SmartArt di tipo Gear in Excel usando Aspose.Cells for C++ con guida passo passo ed esempi di codice.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells for C++ può estrarre testo da SmartArt di tipo Gear. Per farlo, segui questi passi:
1. Converti SmartArt Shape in forma di gruppo usando il metodo [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4).
2. Recupera tutte le forme individuali che compongono il SmartArt Shape utilizzando il metodo [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a).
Itera attraverso ogni singola forma ed estrai il testo usando il metodo [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a).

## **Estrarre il testo dalla forma SmartArt di tipo ingranaggio**

Il seguente esempio di codice carica un [file Excel di esempio](67338483.xlsx) contenente una Forma SmartArt di Tipo Ingranaggio e ne estrae il testo dalle sue forme individuali. Consulta l'output della console sotto per i risultati.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
