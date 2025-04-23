---
title: Работа с эффектом свечения формы или графика с помощью C++
linktitle: Работа с эффектом свечения формы или диаграммы
type: docs
weight: 240
url: /ru/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом свечения форм или графиков с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) вместе с классом [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) для работы с эффектом свечения формы или графика. Класс [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) содержит следующие свойства, которые могут быть установлены для достижения различных результатов в соответствии с требованиями приложения.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Работа с эффектом свечения формы или диаграммы**
Следующий пример кода загружает [исходный excel файл](5115407.xlsx) и получает доступ к первой фигуре в первом листе, устанавливает под-свойства свойства [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) и сохраняет рабочую книгу в [выходной excel файл](5115414.xlsx).

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

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
