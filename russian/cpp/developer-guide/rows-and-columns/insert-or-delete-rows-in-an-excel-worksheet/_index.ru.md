---
title: Вставка или удаление строк в листе Excel с помощью C++
linktitle: Вставка или удаление строк
type: docs
weight: 20
url: /ru/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Данная статья содержит C++ код для вставки и удаления строк в листе Excel.
keywords: C++ вставка или удаление строк в Excel, C++ вставка или удаление строк в Excel, C++ вставка строк в Excel, C++ удаление строк в Excel, вставка или удаление строк в листе Excel с помощью C++, вставка или удаление строк в Excel с помощью C++, вставка строк в Excel с помощью C++, удаление строк в Excel с помощью C++
---

{{% alert color="primary" %}}

При создании нового рабочего листа или работы с существующим листом в Excel вам может понадобиться добавить дополнительные строки или столбцы для размещения данных. В других случаях может потребоваться удалить строки или столбцы из указанных позиций на листе.

{{% /alert %}}

Aspose.Cells предлагает два метода для вставки и удаления строк: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) и [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). Эти методы оптимизированы для производительности и выполняют работу очень быстро.

Для вставки или удаления нескольких строк рекомендуем всегда использовать методы [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) и [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/), вместо использования методов [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) или [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) в цикле.

Aspose.Cells работает так же, как и Microsoft Excel. При добавлении строк или столбцов содержимое рабочего листа сдвигается вниз и вправо. При удалении строк или столбцов содержимое рабочего листа сдвигается вверх или влево. Ссылки в других рабочих листах и ячейках обновляются при добавлении или удалении строк.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
