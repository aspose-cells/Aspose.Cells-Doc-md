---
title: Экспорт диапазона области печати в HTML с C++
linktitle: Экспорт диапазона области печати в HTML
type: docs
weight: 60
url: /ru/cpp/export-print-area-range-to/
description: Узнайте, как экспортировать диапазон области печати в HTML с использованием Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Это распространенный сценарий, когда нужно экспортировать только область печати, то есть выбранный диапазон ячеек, а не весь лист, в HTML. Эта функция уже доступна для рендеринга PDF, однако теперь вы можете выполнять эту задачу и для HTML. Сначала установите область печати в объекте настройки страницы листа. Затем используйте флаг [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/), чтобы экспортировать только выбранный диапазон.

## **Образец кода**

Следующий пример загружает книгу и экспортирует диапазон области печати в HTML. Тестовый файл для этой функции можно скачать по следующей ссылке:

[sampleInlineCharts.xlsx](79527946.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
