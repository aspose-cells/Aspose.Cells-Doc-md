---
title: Trouver la position absolue d une forme dans la feuille de calcul avec C++
linktitle: Trouver la position absolue de la forme dans la feuille de calcul
type: docs
weight: 8000
url: /fr/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Déterminez la position absolue d une forme dans une feuille de calcul en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, vous devez connaître la position absolue d'une forme dans une feuille de calcul. Aspose.Cells fournit les propriétés [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) et [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) à cette fin. Ces propriétés renvoient la position absolue de la forme dans la feuille de calcul en pixels.

{{% /alert %}}

Le code d'exemple suivant affiche la position absolue de la première forme dans la feuille de calcul en pixels. Le code d'exemple affiche la sortie console suivante :

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
