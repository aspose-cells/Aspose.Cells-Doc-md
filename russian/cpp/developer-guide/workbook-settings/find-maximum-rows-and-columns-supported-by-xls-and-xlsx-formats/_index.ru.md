---
title: Найти максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX, с помощью C++
linktitle: Найти максимальное количество строк и столбцов
type: docs
weight: 20
url: /ru/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Научитесь находить максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Различные форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65536 строк и 256 столбцов, а XLSX — 1048576 строк и 16384 столбца. Если хотите узнать, сколько строк и столбцов поддерживает конкретный формат, используйте свойства [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) и [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**

Следующий пример создает рабочую книгу сначала в формате XLS, затем в XLSX. После создания он выводит значения свойств [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) и [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). Пожалуйста, ознакомьтесь с выводом в консоли приведенного ниже кода для справки.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Print message about XLS format.
    std::cout << "Maximum Rows and Columns supported by XLS format." << std::endl;

    // Create workbook in XLS format.
    Workbook wb(FileFormatType::Excel97To2003);

    // Print the maximum rows and columns supported by XLS format.
    int maxRows = wb.GetSettings().GetMaxRow() + 1;
    int maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;
    std::cout << std::endl;

    // Print message about XLSX format.
    std::cout << "Maximum Rows and Columns supported by XLSX format." << std::endl;

    // Create workbook in XLSX format.
    wb = Workbook(FileFormatType::Xlsx);

    // Print the maximum rows and columns supported by XLSX format.
    maxRows = wb.GetSettings().GetMaxRow() + 1;
    maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
