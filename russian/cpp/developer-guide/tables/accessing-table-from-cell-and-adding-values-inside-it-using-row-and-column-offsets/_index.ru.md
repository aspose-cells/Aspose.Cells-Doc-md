---  
title: Доступ к таблице из ячейки и добавление значений внутри нее с помощью смещений строк и столбцов в C++  
linktitle: Доступ к таблице из ячейки и добавление значений в нее с использованием смещений строк и столбцов  
type: docs  
weight: 230  
url: /ru/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: Обращение к таблице из ячейки и добавление значений с использованием Aspose.Cells и C++.  
---  

{{% alert color="primary" %}}  

Обычно вы добавляете значения внутри объекта Table или List, используя метод [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/). Но иногда вам может потребоваться добавлять значения внутри объекта Table или List, используя смещения строки и столбца.  

Чтобы получить доступ к таблице или списковому объекту из ячейки, используйте метод [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/). Чтобы добавить значения внутри с помощью смещений строки и столбца, используйте метод [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

{{% /alert %}}  

Следующий скриншот показывает исходный файл Excel, используемый в коде. Он содержит пустую таблицу и выделяет ячейку D5 внутри таблицы. Мы получим доступ к этой таблице из ячейки D5 с помощью метода [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/), а затем добавим значения внутри с использованием методов [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) и [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

## Пример  

### Снимки экрана сравнивают исходные и выходные файлы  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

На следующем снимке экрана показан созданный код. Как видно, ячейка D5 имеет значение, и ячейка F6, которая находится в смещении 2,2 от таблицы, имеет значение.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### C++ код для обращения к таблице из ячейки и добавления значений внутри нее с помощью смещений строки и столбца  

Следующий примерный код загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.  

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
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell D5 which lies inside the table
    Cell cell = worksheet.GetCells().Get(u"D5");

    // Put value inside the cell D5
    cell.PutValue(u"D5 Data");

    // Access the Table from this cell
    ListObject table = cell.GetTable();

    // Add some value using Row and Column Offset
    table.PutCellValue(2, 2, u"Offset [2,2]");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
