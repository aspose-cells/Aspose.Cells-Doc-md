---
title: Individuare la posizione assoluta di una forma all’interno del Foglio di Lavoro con C++
linktitle: Trova la posizione assoluta della forma all interno del foglio di lavoro
type: docs
weight: 8000
url: /it/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Determinare la posizione assoluta di una forma in un foglio di lavoro usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte è necessario conoscere la posizione assoluta di una forma in un foglio di lavoro. Aspose.Cells fornisce le proprietà [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) e [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) a questo scopo. Queste proprietà restituiscono la posizione assoluta della forma all'interno del foglio di lavoro in pixel.

{{% /alert %}}

Il codice di esempio seguente visualizza la posizione assoluta della prima forma nel foglio di lavoro in pixel. Il codice di esempio visualizza l'output della console seguente:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the sample Excel file inside the workbook object
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first shape inside the worksheet
    Shape shape = worksheet.GetShapes().Get(0);

    // Displays the absolute position of the shape
    std::wcout << L"Absolute Position of this Shape is (" << shape.GetLeftToCorner() << L" , " << shape.GetTopToCorner() << L")" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
