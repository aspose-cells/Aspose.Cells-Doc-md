---
title: Укажите, как пересекать строки в выводимом HTML с помощью HtmlCrossType в C++
linktitle: Укажите HtmlCrossType в выводимом HTML
type: docs
weight: 140
url: /ru/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Узнайте, как управлять переполнением строк в HTML выводе с помощью Aspose.Cells for C++ и HtmlCrossType.
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, превышающую ширину ячейки, строка переполняется, если следующая ячейка в следующем столбце пустая или null. При сохранении файла Excel в HTML этот переполнение можно контролировать, задавая тип пересечения с помощью перечисления [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). Оно включает следующие значения:

- **HtmlCrossType.Default**: Отображается как в MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка пересечется или будет усечена.

- **HtmlCrossType.MSExport**: Отображение строки как при экспорте HTML из MS Excel.

- **HtmlCrossType.Cross**: Отображение строки пересечения HTML, производительность при создании больших HTML-файлов будет более чем в десять раз быстрее, чем при установке значения Default или FitToCell.

- **HtmlCrossType.FitToCell**: отображает строку только внутри ширины ячейки.

## **Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType**

Следующий пример кода загружает [пример файла Excel](51740732.xlsx) и сохраняет его в формате HTML, задавая разные значения [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). Пожалуйста, скачайте [выходные HTML](51740734.zip), созданные этим кодом. Пример файла Excel содержит изображение с красной рамкой, как показано на этом скриншоте, который демонстрирует эффект значений [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) на выводимый HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
