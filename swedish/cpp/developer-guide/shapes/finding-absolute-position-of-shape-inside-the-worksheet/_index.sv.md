---
title: Hitta absolut position för form inuti kalkbladet med C++
linktitle: Hitta absolut position av formen innanför arbetsbladet
type: docs
weight: 8000
url: /sv/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Bestäm den absoluta positionen för en form i ett kalkblad med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland behöver du veta den absoluta positionen av en form i ett arbetsblad. Aspose.Cells tillhandahåller [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) och [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) egenskaper för detta ändamål. Dessa egenskaper returnerar den absoluta positionen för formen inuti arbetsbladet i pixlar.

{{% /alert %}}

Följande exempel på kod visar den absoluta positionen för den första formen i arbetsbladet i pixlar. Exempelkoden visar följande konsolresultat:

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
