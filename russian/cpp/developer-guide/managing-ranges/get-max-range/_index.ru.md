---
title: Получить максимальный диапазон в листе с помощью C++
linktitle: Получить максимальный диапазон на рабочем листе
type: docs
weight: 360
url: /ru/cpp/get-max-range-in-a-worksheet/
description: Эта статья описывает, как получить максимальный диапазон, максимальный диапазон данных и максимальный диапазон отображения файлов Excel с помощью библиотеки Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

При чтении данных с рабочего листа нам необходимо знать максимальную область.

При копировании всех данных с рабочего листа нам необходимо знать максимальную область.

При экспорте определенной области в HTML и PDF необходимо знать максимальную область.

Aspose.Cells for C++ содержит различные способы поиска максимального диапазона в листе. 

{{% /alert %}} 

## **Получение максимального диапазона**
В Aspose.Cells, если объекты [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) и [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) инициализированы, эти строки и столбцы будут учитываться при определении максимальной области, даже если в пустых строках или столбцах нет данных.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Получение максимального диапазона данных**
В большинстве случаев нам нужно получить все диапазоны, содержащие все данные, даже если пустые ячейки за пределами диапазона отформатированы.
И настройки о формах, таблицах и сводных таблицах будут игнорироваться.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Получение максимального диапазона отображения**
Когда мы экспортируем все данные с листа в HTML, PDF или изображения, нам необходимо получить область, содержащую все видимые объекты, включая данные, стили, графику, таблицы и сводные таблицы.
Следующие коды показывают, как отобразить максимальную дисплей-область в HTML:

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Вот [исходный файл Excel](Book1.xlsx).
