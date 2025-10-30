---
title: Lavorare con l effetto bagliore di forma o grafico con C++
linktitle: Lavorare con l effetto Glow della forma o del grafico
type: docs
weight: 240
url: /it/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Impara come lavorare con l’effetto bagliore di forme o grafici usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells fornisce la proprietà [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) insieme alla classe [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) per lavorare con l’effetto bagliore di forma o grafico. La classe [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) contiene le seguenti proprietà che possono essere impostate per ottenere risultati differenti in base ai requisiti dell'applicazione.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Lavorare con l'effetto Glow della forma o del grafico**
Il seguente esempio di codice carica il [file excel sorgente](5115407.xlsx) e accede alla prima forma nel primo foglio di lavoro e imposta le sotto-proprietà di [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) quindi salva il libro di lavoro in [file excel di output](5115414.xlsx).

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

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
