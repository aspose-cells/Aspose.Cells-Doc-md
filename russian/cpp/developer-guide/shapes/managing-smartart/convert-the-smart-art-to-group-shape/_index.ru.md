---
title: Преобразовать Smart Art в групповую фигуру с помощью C++
linktitle: Преобразовать умное изображение в групповую форму
type: docs
weight: 200
url: /ru/cpp/convert-the-smart-art-to-group-shape/
description: Узнайте, как преобразовать фигуру Smart Art в групповую фигуру с помощью Aspose.Cells for C++ и получить доступ к отдельным частям групповой фигуры.
---

## **Возможные сценарии использования**

Вы можете преобразовать Smart Art Shape в Group Shape, используя метод [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/). Это позволит вам обрабатывать Smart Art Shape как Group Shape. Следовательно, у вас будет доступ к отдельным частям или элементам Group Shape.

## **Преобразование SmartArt в форму группы**

Следующий пример кода загружает [пример файла Excel](55541793.xlsx), содержащего фигуру smart art, как показано на скриншоте. Затем он превращает фигуру smart art в групповую и выводит свойство Shape::IsGroup. Ниже приведен пример вывода в консоль.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
