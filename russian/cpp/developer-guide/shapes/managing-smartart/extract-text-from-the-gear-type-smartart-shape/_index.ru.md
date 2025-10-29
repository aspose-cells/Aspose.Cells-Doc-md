---
title: Извлечь текст из фигуры SmartArt типа Gear с помощью C++
linktitle: Извлечение текста из формы SmartArt типа Gear
type: docs
weight: 500
url: /ru/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Узнайте, как извлечь текст из фигур SmartArt типа Gear в Excel с помощью Aspose.Cells for C++, предоставляя пошаговое руководство и примеры кода.
---

## **Возможные сценарии использования**

Aspose.Cells for C++ умеет извлекать текст из фигуры SmartArt типа Gear. Для этого выполните следующие шаги:
1. Преобразовать фигуру SmartArt в групповую фигуру с помощью метода [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4).
2. Получить все отдельные фигуры, формирующие групповую фигуру, с помощью метода [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a).
3. Проходить по каждой отдельной фигуре и извлекать текст с помощью метода [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a).

## **Извлечение текста из формы SmartArt с шестеренчатым типом**

Следующий пример кода загружает [пример файла Excel](67338483.xlsx), содержащего фигуру SmartArt типа Gear, и извлекает текст из его отдельных фигур. Результаты смотрите в выводе консоли ниже.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
