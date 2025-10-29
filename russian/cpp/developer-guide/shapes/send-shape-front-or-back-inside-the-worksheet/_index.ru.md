---
title: Отправить фигуру вперед или назад внутри рабочего листа с помощью C++
linktitle: Отправить форму вперед или назад внутри листа
type: docs
weight: 3400
url: /ru/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Узнайте, как изменять z порядок фигур в листе с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Когда в одном месте находится несколько фигур, их видимость определяется их положением по z-порядку. Aspose.Cells предоставляет метод [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/), который изменяет z-область фигуры. Если вы хотите отправить фигуру на задний план, используйте отрицательное число, например -1, -2, -3 и т.д. Если хотите поднять фигуру на передний план, используйте положительное число, например 1, 2, 3 и т.д.

## **Отправить форму вперед или назад внутри листа**

Следующий пример кода демонстрирует использование метода [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/). Пожалуйста, посмотрите [приведенный пример файла Excel](50528330.xlsx), использованный в коде, и [сгенерированный выходной файл Excel](50528331.xlsx). Скриншот показывает эффект работы кода на примере файла Excel при запуске.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
