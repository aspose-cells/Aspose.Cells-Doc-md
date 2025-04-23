---
title: Работа с 3D форматом фигуры или диаграммы с помощью C++
linktitle: Работа с ThreeDFormat формы или диаграммы
type: docs
weight: 250
url: /ru/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Узнайте, как управлять 3D форматом фигур или диаграмм с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) вместе с классом [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) для работы с 3D-форматом фигур или диаграмм. Класс [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) содержит различные свойства, которые можно установить для достижения различных результатов в соответствии с требованиями приложения.

## **Работа с ThreeDFormat формы или диаграммы**
Следующий пример загружает [исходный Excel-файл](5115419.xlsx), получает доступ к первой фигуре на первом листе, устанавливает подполя свойства [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) и сохраняет книгу в [выходной Excel-файл](5115410.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
