---
title: Укажите название шрифта по Восточной Азии и латинский в настройках текста фигуры с помощью C++
linktitle: Укажите Дальний Восток и латинское название шрифта в опциях текста формы
type: docs
weight: 1600
url: /ru/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Узнайте, как указать названия шрифтов по Восточной Азии и латинский в настройках текста фигуры, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда текст на языке Восточной Азии, например японском, китайском, тайском и др., отображается неправильно. Aspose.Cells предоставляет свойство [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/), которое можно использовать для указания названия шрифта Восточной Азии. Кроме того, можно указать латинский шрифт с помощью свойства [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/).

## **Укажите Дальний Восток и латинское название шрифта в опциях текста формы**

Следующий пример создает текстовое поле и добавляет внутри него японский текст. Затем указывается латинское и Восточноазиатское название шрифтов для текста и сохраняется рабочая книга как [выходной файл Excel](67338274.xlsx). Следующий скриншот показывает латинские и Восточноазиатские названия шрифтов выходного текстового поля в Microsoft Excel.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet ws = wb.GetWorksheets().Get(0);

    int idx = ws.GetTextBoxes().Add(5, 5, 50, 200);
    TextBox tb = ws.GetTextBoxes().Get(idx);

    tb.SetText(u"\u3053\u3093\u306B\u3061\u306F\u4E16\u754C");

    tb.GetTextOptions().SetLatinName(u"Comic Sans MS");
    tb.GetTextOptions().SetFarEastName(u"KaiTi");

    wb.Save(u"outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", SaveFormat::Xlsx);

    std::cout << "Textbox created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
