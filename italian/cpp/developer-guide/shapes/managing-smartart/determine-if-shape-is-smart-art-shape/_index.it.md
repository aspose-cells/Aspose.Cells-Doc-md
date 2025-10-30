---
title: Determina se una forma è una forma di smart art con C++
linktitle: Determinare se la forma è una forma di arte intelligente
type: docs
weight: 400
url: /it/cpp/determine-if-shape-is-smart-art-shape/
description: Impara come determinare se una forma è una forma di smart art usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

I Smart Art Shapes sono forme speciali in Microsoft Excel che ti consentono di creare diagrammi complessi in modo automatico. È possibile verificare se la forma è una forma di arte intelligente o una forma normale utilizzando la proprietà [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/).

## **Determinare se la forma è una forma SmartArt**

Il seguente codice di esempio carica il [file di Excel di esempio](55541792.xlsx) contenente una forma di arte intelligente come mostrato in questa schermata. Quindi stampa il valore della proprietà [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) della prima forma. Si prega di consultare l'output della console del codice di esempio fornito di seguito.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
