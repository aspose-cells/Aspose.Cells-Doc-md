---
title: Текстура плитки внутри формы с помощью C++
linktitle: Размещение изображения в качестве текстуры внутри формы
type: docs
weight: 1700
url: /ru/cpp/tile-picture-as-a-texture-inside-the-shape/
description: Узнайте, как текстурировать изображение внутри формы с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Когда изображение маленькое и не покрывает всю поверхность формы без потери качества, то у вас есть возможность повторить его. Повторение заполняет поверхность формы маленьким изображением, повторяя их, как плитку.

## **Текстурное изображение внутри формы**

Вы можете заполнить поверхность фигуры некоторым изображением и наложить на нее плитки, используя свойство [**Shape.Fill.TextureFill.IsTiling**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/texturefill/istiling/) и установить его **true**. Пожалуйста, ознакомьтесь с следующим образцом кода, [образцом файла Excel](46465050.xlsx), а также снимком экрана для справки.

## **Снимок экрана**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleTextureFill_IsTiling.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape inside the worksheet
    Shape sh = ws.GetShapes().Get(0);

    // Tile Picture as a Texture inside the Shape
    sh.GetFill().GetTextureFill().SetIsTiling(true);

    // Save the output Excel file
    wb.Save(outDir + u"outputTextureFill_IsTiling.xlsx");

    std::cout << "Texture fill tiling applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
