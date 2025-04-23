---
title: Hämta anslutningspunkter från form med C++
linktitle: Hämta anslutningspunkter från figur
type: docs
weight: 3500
url: /sv/cpp/get-connection-points-from-shape/
description: Lär dig hur man hämtar formens anslutningspunkter med Aspose.Cells for C++.
---

Aspose.Cells erbjuder många funktioner för att hantera former i kalkblad. Ibland behövs det att få anslutningspunkterna för att justera eller placera formen. Följande kod kan användas för att få listan av anslutningspunkter för en form med `[Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/)`-metoden.

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
