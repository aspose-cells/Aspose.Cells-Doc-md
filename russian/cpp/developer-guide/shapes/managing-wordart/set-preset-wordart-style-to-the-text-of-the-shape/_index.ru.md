---
title: Установите предустановленный стиль WordArt для текста формы с помощью C++
linktitle: Установите предустановленный стиль WordArt для текста формы
type: docs
weight: 280
url: /ru/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Узнайте, как установить предустановленный стиль WordArt для текста формы с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Вы можете установить предустановленный стиль WordArt для текста формы с помощью Aspose.Cells. Используйте методы [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) или [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/).

## **Установите предустановленный стиль WordArt для текста формы**
Следующий пример кода создает текстовое поле с некоторым текстом и затем устанавливает предустановленный стиль WordArt его текста с помощью метода [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/). Вот как выглядит файл [выходной Excel](5115445.xlsx) в Microsoft Excel.

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a textbox with some text
    TextBox textbox = worksheet.GetShapes().AddTextBox(0, 0, 0, 0, 100, 700);
    textbox.SetText(u"Aspose File Format APIs");
    textbox.GetFont().SetSize(44);

    // Sets preset WordArt style to the text of the shape.
    FontSetting fntSetting = textbox.GetRichFormattings()[0];
    fntSetting.SetWordArtStyle(PresetWordArtStyle::WordArtStyle3);

    // Save the workbook in xlsx format
    workbook.Save(u"..\\Data\\02_OutputDirectory\\outputSetPresetWordArtStyle.xlsx");

    std::cout << "Workbook saved successfully with preset WordArt style!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
