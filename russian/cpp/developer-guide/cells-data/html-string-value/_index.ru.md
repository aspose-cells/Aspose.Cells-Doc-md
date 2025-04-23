---
title: Добавление HTML обогащенного текста внутри ячейки с помощью C++
linktitle: Значение HTML строки
type: docs
weight: 50
url: /ru/cpp/adding-html-rich-text-inside-the-cell/
description: Узнайте, как добавлять HTML обогащённый текст внутри ячейки через API Aspose.Cells for C++.
keywords: Добавить HTML форматированный текст внутрь ячейки, Установить HTML форматированный текст внутрь ячейки, Добавить HTML форматированный текст в ячейку
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование HTML, ориентированного на Microsoft Excel, в формат XLS/XLSX. Это означает, что HTML, сгенерированный Microsoft Excel, может быть преобразован обратно в формат XLS/XLSX с использованием Aspose.Cells.

Аналогично, если есть простой HTML-код, Aspose.Cells может преобразовать его в HTML-обогащенный текст. Aspose.Cells предоставляет метод [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/), который может взять такой простой HTML и преобразовать его в форматированный текст ячейки.

{{% /alert %}}

Приведенный ниже образец кода показывает, как добавить HTML-форматированный текст в ячейку. Пожалуйста, посмотрите скриншот выходного файла Excel.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Связанные статьи

- [Отображение маркеров путем установки значения ячейки с использованием HTML](/cells/ru/cpp/display-bullets-by-setting-cell-value-using/)
- [Получение строки HTML5 из ячейки](/cells/ru/cpp/get-html5-string-from-cell/)
