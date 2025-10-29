---
title: Получить точки подключения фигуры с C++
linktitle: Получить точки подключения фигуры
type: docs
weight: 3500
url: /ru/cpp/get-connection-points-from-shape/
description: Узнайте, как получать точки подключения фигуры с помощью Aspose.Cells for C++.
---

Aspose.Cells предоставляет богатый функционал для управления фигурами в таблицах. Иногда возникает необходимость получить точки подключения фигуры для выравнивания или размещения. Следующий код можно использовать для получения списка точек подключения фигуры с помощью метода [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/)

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
