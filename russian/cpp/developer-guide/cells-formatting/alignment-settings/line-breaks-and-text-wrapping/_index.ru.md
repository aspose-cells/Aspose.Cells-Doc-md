---
title: Перерывы строк и обертка текста с помощью C++
description: Как реализовать обертку текста и перенос слов с использованием библиотеки Aspose.Cells в C++. Используя библиотеку Aspose.Cells, вы можете легко вставлять текст в ячейки и задавать метод обертки текста, такой как ручной перенос слов, автоматическая обертка и др. В этом документе подробно описывается, как реализовать эти функции, и предоставляется пример кода для вашего ознакомления.
keywords: Aspose.Cells, перенос строки, перенос текста, макет текста
type: docs
weight: 60
url: /ru/cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в несколько в ячейке, а явные разрывы строк устанавливаются точно там, где вы их хотите.

{{% /alert %}}

## **Перенос текста в ячейке**

Для переноса текста в ячейке используйте свойство [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of the first column
    cell.SetColumnWidth(0, 35);

    // Increase the height of the first row
    cell.SetRowHeight(0, 36);

    // Add text to the first cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make the cell's text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(srcDir + u"WrappingText.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Использование явных переносов строк**

Вы можете использовать '\n' в C++ для вставки явных разрывов строк в ячейку.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create Workbook Object
    Workbook workbook;

    // Open first Worksheet in the workbook
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Aspose::Cells::Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 65);

    // Add Text to the First Cell with Explicit Line Breaks
    cell.Get(0, 0).PutValue(u"I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    U16String outputFilePath = u"WrappingText.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
