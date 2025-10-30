---
title: Obtener puntos de conexión de una forma con C++
linktitle: Obtener puntos de conexión de forma
type: docs
weight: 3500
url: /es/cpp/get-connection-points-from-shape/
description: Aprende cómo recuperar los puntos de conexión de una forma usando Aspose.Cells for C++.
---

Aspose.Cells ofrece funciones completas para gestionar formas en hojas de cálculo. A veces es necesario obtener los puntos de conexión de una forma para alineación o colocación. El siguiente código se puede usar para obtener la lista de puntos de conexión de una forma usando el método [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/)

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
