---
title: Группировка и разгруппировка строк и столбцов с помощью C++
linktitle: Группировка и расгруппировка строк и столбцов
type: docs
weight: 50
url: /ru/cpp/grouping-and-ungrouping-rows-and-columns/
description: Узнайте, как группировать и разгруппировать строки и столбцы в файлах Excel с помощью Aspose.Cells на C++.
---

## **Введение**

В файле Microsoft Excel можно создать контур для данных, чтобы можно было показать и скрыть уровни детализации одним щелчком мыши.

Щелкните на **Символы сводки**, 1,2,3, + и -, чтобы быстро отобразить только строки или столбцы, которые предоставляют сводки или заголовки для разделов в листе, или можно использовать символы, чтобы увидеть детали под отдельной сводкой или заголовком, как показано ниже на рисунке:

|**Группировка строк и столбцов.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Управление группировкой строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), что позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) обеспечивает коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), которая представляет все ячейки в листе.

Коллекция [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) предоставляет несколько методов для управления строками или столбцами на листе, ниже подробно рассмотрены некоторые из них.

### **Группировка строк и столбцов**

Возможно сгруппировать строки или столбцы, вызвав методы [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) и [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Оба метода принимают следующие параметры:

- Индекс первой строки/столбца в группе.
- Индекс последней строки/столбца в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Group first six rows (from 0 to 5) and make them hidden
    worksheet.GetCells().GroupRows(0, 5, true);

    // Group first three columns (from 0 to 2) and make them hidden
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns grouped successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Настройки группировки**

Microsoft Excel позволяет настроить параметры группировки для отображения:

- Сводные строки под деталями.
- Сводные столбцы справа от деталей.

Разработчики могут настроить параметры группы, используя свойство [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

### **Итоговые строки под деталями**

Возможно управлять отображением итоговых строк под деталями, установив свойство [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/) класса [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) в **true** или **false**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Setting SummaryRowBelow property to false
    worksheet.GetOutline().SetSummaryRowBelow(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Итоговые столбцы справа от деталей**

Разработчики могут также управлять отображением итоговых столбцов справа от деталей, установив свойство [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/) класса [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) в **true** или **false**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Set summary column to the right
    worksheet.GetOutline().SetSummaryColumnRight(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Разгруппировка строк и столбцов**

Чтобы разгруппировать любые сгруппированные строки или столбцы, вызовите методы [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) и [**UngroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Оба метода принимают два параметра:

- Индекс первой строки/столбца, которую нужно разгруппировать.
- Индекс последней строки/столбца, которую нужно разгруппировать.

[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) имеет перегрузку, принимающую третий параметр логического типа. Установка его в **true** удаляет всю группированную информацию. В противном случае удаляется только внешняя информация о группе.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Ungrouping first six rows (from 0 to 5)
    worksheet.GetCells().UngroupRows(0, 5);

    // Ungrouping first three columns (from 0 to 2)
    worksheet.GetCells().UngroupColumns(0, 2);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```
