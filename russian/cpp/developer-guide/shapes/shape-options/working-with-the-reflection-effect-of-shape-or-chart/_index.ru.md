---
title: Работа с эффектом отражения формы или диаграммы с помощью C++
linktitle: Работа с эффектом отражения формы или диаграммы
type: docs
weight: 210
url: /ru/cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом отражения фигур или диаграмм с использованием Aspose.Cells и C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) вместе с классом [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) для работы с эффектом отражения формы или диаграммы. Класс [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) содержит следующие свойства, которые можно установить для достижения различных результатов в соответствии с требованиями приложения.

- [Размытие](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)
- [Направление](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)
- [Расстояние](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)
- [Направление затухания](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)
- [Поворот с формой](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)
- [Размер](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)
- [Прозрачность](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)
- [Тип](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)

## **Работа с эффектом отражения формы или диаграммы**
Следующий пример загружает [исходный Excel-файл](5115424.xlsx), получает доступ к первой фигуре на листе по умолчанию, устанавливает различные свойства класса [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) и затем сохраняет книгу в [выходной Excel-файл](5115423.xlsx).

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

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
