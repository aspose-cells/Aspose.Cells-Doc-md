---
title: Invia forma in primo o in secondo piano all’interno del foglio di lavoro con C++
linktitle: Invia la forma avanti o indietro all interno del foglio di lavoro
type: docs
weight: 3400
url: /it/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Impara come cambiare la posizione Z order delle forme in un foglio di lavoro usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando ci sono più forme presenti nello stesso luogo, la loro visibilità è determinata dalle loro posizioni di z-ordine. Aspose.Cells offre il metodo [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/), che cambia la posizione di z-ordine della forma. Se si desidera inviare una forma in background, si utilizza un numero negativo come -1, -2, -3, ecc. Se si desidera portare una forma in primo piano, si utilizza un numero positivo come 1, 2, 3, ecc.

## **Invia la forma avanti o indietro all'interno del foglio di lavoro**

Il seguente esempio di codice dimostra l'uso del metodo [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/). Si prega di consultare il [file Excel di esempio](50528330.xlsx) utilizzato nel codice e il [file Excel di output](50528331.xlsx) generato da esso. Lo screenshot mostra l'effetto del codice sul file Excel di esempio all'esecuzione.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
