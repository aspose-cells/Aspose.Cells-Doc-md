---
title: Converti il Smart Art in forma di gruppo con C++
linktitle: Convertire l Arte intelligente in Forma di gruppo
type: docs
weight: 200
url: /it/cpp/convert-the-smart-art-to-group-shape/
description: Impara come convertire una forma di Smart Art in Forma di Gruppo usando Aspose.Cells for C++ e accedere alle singole parti del gruppo.
---

## **Possibili Scenari di Utilizzo**

È possibile convertire la forma di Arte intelligente in Forma di gruppo utilizzando il metodo [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/). Questo ti consentirà di gestire la forma di arte intelligente come una forma di gruppo. Di conseguenza, avrai accesso alle singole parti o forme della forma di gruppo.

## **Convertire la SmartArt in una forma di gruppo**

Il seguente esempio di codice carica il [file Excel di esempio](55541793.xlsx) contenente una forma di smart art come mostrato nello screenshot. Quindi converte la forma smart art in forma di gruppo e stampa la proprietà Shape::IsGroup. Vedi l'output della console di seguito.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
