---
title: Определить, является ли фигура Smart Art, с помощью C++
linktitle: Определить, является ли форма формой Smart Art
type: docs
weight: 400
url: /ru/cpp/determine-if-shape-is-smart-art-shape/
description: Узнайте, как определить, является ли фигура Smart Art, с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Умные формы Smart Art - это специальные формы в Microsoft Excel, которые позволяют автоматически создавать сложные диаграммы. Вы можете определить, является ли форма умной или обычной с помощью свойства [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/).

## **Определение, является ли форма формой Smart Art**

В следующем примере кода загружается [образец файла Excel](55541792.xlsx) с умной формой, как показано на этом скриншоте. Затем выводится значение свойства [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) первой формы. Пожалуйста, ознакомьтесь с выводом консоли в приведенном ниже примере кода.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
