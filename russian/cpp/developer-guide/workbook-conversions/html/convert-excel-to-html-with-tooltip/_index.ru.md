---
title: Конвертация Excel в HTML с подсказкой с помощью C++
linktitle: Преобразовать Excel в HTML c всплывающей подсказкой
type: docs
weight: 200
url: /ru/cpp/convert-excel-to-html-with-tooltip/
description: Конвертация Excel в HTML с добавлением подсказок с помощью Aspose.Cells и C++.
---

## **Преобразование Excel в HTML со всплывающей подсказкой**

Бывают случаи, когда в сгенерированном HTML часть текста обрезана, и вы хотите отображать полный текст в виде подсказки при наведении. Aspose.Cells поддерживает это свойством [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/). Установка свойства [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/) в **true** добавит полный текст в виде подсказки в сгенерированный HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML файле.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Следующий пример кода загружает [исходный Excel-файл](98107416.xlsx) и генерирует [выходной HTML-файл](98107417.zip) с подсказкой.

Образец кода

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
