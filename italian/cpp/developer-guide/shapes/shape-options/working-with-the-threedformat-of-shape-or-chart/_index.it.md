---
title: Lavorare con il formato 3D di forma o grafico con C++
linktitle: Lavorare con il ThreeDFormat della forma o del grafico
type: docs
weight: 250
url: /it/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Impara come manipolare il formato 3D di forme o grafici usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells fornisce la proprietà [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) insieme alla classe [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) per lavorare con il formato 3D di forme o grafici. La classe [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) contiene diverse proprietà che possono essere impostate per ottenere risultati diversi secondo le esigenze dell'applicazione.

## **Lavorare con il ThreeDFormat della forma o del grafico**
Il seguente esempio di codice carica il [file Excel di origine](5115419.xlsx) e accede alla prima forma nel primo foglio di lavoro. Quindi imposta le sotto-proprietà della proprietà [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) e salva il workbook nel [file Excel di output](5115410.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
