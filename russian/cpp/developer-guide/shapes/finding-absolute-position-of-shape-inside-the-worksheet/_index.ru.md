---
title: Определение абсолютной позиции фигуры внутри рабочего листа с C++
linktitle: Нахождение абсолютной позиции формы внутри Листа книги Excel
type: docs
weight: 8000
url: /ru/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Определите абсолютную позицию фигуры в рабочем листе с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Иногда вам нужно знать абсолютное положение формы на листе. Aspose.Cells предоставляет свойства [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) и [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) для этой цели. Эти свойства возвращают абсолютное положение формы внутри листа в пикселях.

{{% /alert %}}

Следующий образец кода отображает абсолютное положение первой формы на листе в пикселях. Образец кода отображает следующий вывод в консоли:

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
