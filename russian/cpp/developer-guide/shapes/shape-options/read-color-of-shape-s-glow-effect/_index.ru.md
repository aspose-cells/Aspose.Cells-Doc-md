---
title: Чтение цвета свечения эффекта формы с помощью C++
linktitle: Чтение цвета эффекта свечения фигуры
type: docs
weight: 330
url: /ru/cpp/read-color-of-shape-s-glow-effect/
description: Узнайте, как читать цвет свечения любого объекта с помощью Aspose.Cells for C++.
---

## Возможные сценарии использования

Если вы хотите узнать цвет эффекта свечения любой фигуры, пожалуйста, используйте свойство [**Shape.Glow.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/). Это поможет вам найти различные свойства, относящиеся к цвету эффекта свечения фигуры.

## Прочитать цвет эффекта свечения формы

Пожалуйста, ознакомьтесь с следующим образцом кода и его [исходным файлом Excel](22774108.xlsx) и выводом консоли для вашего справочного значения. Ниже приведен снимок экрана эффекта свечения фигуры в исходном файле Excel, когда просматривается в Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Код на C++ для чтения цвета свечения форм

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sourceGlowEffectColor.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);
    Shape shape = sheet.GetShapes().Get(0);
    GlowEffect effect = shape.GetGlow();
    CellsColor color = effect.GetColor();

    Color clr = color.GetColor();
    uint32_t argb = (static_cast<uint32_t>(clr.a) << 24) | 
                    (static_cast<uint32_t>(clr.r) << 16) | 
                    (static_cast<uint32_t>(clr.g) << 8) | 
                    static_cast<uint32_t>(clr.b);

    std::cout << "Color: " << argb << std::endl;
    std::cout << "ColorIndex: " << color.GetColorIndex() << std::endl;
    std::cout << "IsShapeColor: " << color.IsShapeColor() << std::endl;
    std::cout << "Transparency: " << color.GetTransparency() << std::endl;
    std::cout << "Type: " << static_cast<int>(color.GetType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Вывод в консоль

Вот вывод консоли вышеуказанного образца кода при выполнении с предоставленным [исходным файлом Excel](22774108.xlsx).

{{< highlight java >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
