---
title: Настройка тени эффектов текста фигуры или текстового блока с помощью C++
linktitle: Настройка тени эффектов текста
type: docs
weight: 250
url: /ru/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Узнайте, как установить тень эффектов текста для фигур или текстовых блоков, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете установить **Тень** **Эффектов текста** любой фигуры или текстового блока. Используйте свойство [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/). Оно управляет настройками текста фигуры и возвращает объекты [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). После доступа к нему установите **Тень** через свойство [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Это свойство типа [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/), имеющее несколько значений, например:

- Смещение по диагонали вниз и вправо
- Смещение вниз
- Смещение по диагонали вверх и вправо
- Слева внутри
- По центру внутри
- Диагональная перспектива вверху слева
- ПерспективаДиагональНижнийПравый

{{% /alert %}}

Следующий фрагмент кода демонстрирует использование свойства [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) для установки тени эффектов текста фигуры или текстового поля.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add text box with these dimensions
    TextBox tb = ws.GetShapes().AddTextBox(2, 0, 2, 0, 100, 400);

    // Set the text of the textbox
    tb.SetText(u"This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

    // Set all the text runs shadow to preset offset bottom
    for (int i = 0; i < tb.GetTextBody().GetCount(); i++)
    {
        tb.GetTextBody().Get(i).GetTextOptions().GetShadow().SetPresetType(PresetShadowType::OffsetBottom);
    }

    // Set the font color and size of the textbox
    tb.GetFont().SetColor(Color::Red());
    tb.GetFont().SetSize(16);

    // Save the output file
    wb.Save(outDir + u"outputSettingTextEffectsShadowOfShapeOrTextbox.xlsx", SaveFormat::Xlsx);

    std::cout << "Text effects shadow of shape or textbox set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
