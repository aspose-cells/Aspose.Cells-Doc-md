---
title: Get Connection Points from Shape with C++
linktitle: Get Connection Points from Shape
type: docs
weight: 3500
url: /cpp/get-connection-points-from-shape/
description: Learn how to retrieve shape connection points using Aspose.Cells for C++.
---

Aspose.Cells provides rich features to manage shapes in spreadsheets. Sometimes there's a need to get the connection points of a shape for alignment or placement. The following code can be used to get the list of connection points of a shape using the [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/) method.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sampleGetFonts.xlsx");

    Vector<Font> fonts = workbook.GetFonts();

    for (int i = 0; i < fonts.GetLength(); ++i)
    {
        std::cout << fonts[i].ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

.