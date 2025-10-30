---
title: Ottenere i punti di connessione da una Forma con C++
linktitle: Ottenere i punti di connessione da una Forma
type: docs
weight: 3500
url: /it/cpp/get-connection-points-from-shape/
description: Impara a recuperare i punti di connessione delle forme usando Aspose.Cells for C++.
---

Aspose.Cells offre caratteristiche ricche per gestire forme nei fogli di calcolo. A volte è necessario ottenere i punti di connessione di una forma per allineamento o posizionamento. Il codice seguente può essere utilizzato per ottenere la lista dei punti di connessione di una forma usando il metodo [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/).

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
{{< app/cells/assistant language="cpp" >}}
