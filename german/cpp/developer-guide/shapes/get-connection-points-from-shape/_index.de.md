---
title: Verbindungspunkte der Form mit C++ abrufen
linktitle: Verbindungspunkte der Form abrufen
type: docs
weight: 3500
url: /de/cpp/get-connection-points-from-shape/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ die Verbindungspunkte einer Form abrufen.
---

Aspose.Cells bietet umfangreiche Funktionen zum Verwalten von Formen in Tabellenkalkulationen. Manchmal ist es notwendig, die Verbindungspunkte einer Form für Ausrichtung oder Platzierung zu ermitteln. Der folgende Code kann verwendet werden, um die Liste der Verbindungspunkte einer Form mit der Methode [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/) zu erhalten.

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
