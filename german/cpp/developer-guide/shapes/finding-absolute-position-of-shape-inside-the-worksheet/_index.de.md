---
title: Position der Shape innerhalb des Arbeitsblatts mit C++ bestimmen
linktitle: Ermittlung der absoluten Position einer Form innerhalb des Arbeitsblatts
type: docs
weight: 8000
url: /de/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Bestimmen Sie die absolute Position einer Form in einem Arbeitsblatt mit Aspose.Cells in C++.
---

{{% alert color="primary" %}}

Manchmal müssen Sie die absolute Position einer Form in einem Arbeitsblatt kennen. Aspose.Cells bietet hierfür die Eigenschaften [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) und [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/). Diese Eigenschaften geben die absolute Position der Form im Arbeitsblatt in Pixel zurück.

{{% /alert %}}

Der folgende Beispielcode zeigt die absolute Position der ersten Form im Arbeitsblatt in Pixeln an. Der Beispielcode zeigt die folgende Konsolenausgabe:

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
