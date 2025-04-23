---
title: Вставка и удаление строк и столбцов файла Excel с помощью C++
linktitle: Вставка и удаление строк и столбцов
type: docs
weight: 70
url: /ru/cpp/inserting-and-deleting-rows-and-columns/
description: В этой статье показано, как вставлять и удалять строки и столбцы с использованием API Aspose.Cells for C++.
keywords: Aspose.Cells C++ управляет строками и столбцами, вставляет и удаляет строки и столбцы
---

## **Введение**

При создании нового листа Excel с нуля или работе с существующим листом нам может потребоваться добавить дополнительные строки или столбцы для размещения большего объема данных. Напротив, также может потребоваться удалить строки или столбцы из указанных позиций в листе.
Для выполнения этих требований Aspose.Cells предоставляет очень простой набор классов и методов, о которых ниже идет речь.

### **Управлять строками и столбцами**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет обращаться к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/), которая отображает все ячейки листа.

Коллекция [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) предоставляет несколько методов для управления строками и столбцами в листе. Некоторые из них приведены ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое листа смещается вниз или вправо, а при удалении — вверх или влево.

{{% /alert %}}

## **Вставить строки и столбцы**

### **Как вставить строку**

Вставьте строку в лист на любую позицию, вызвав метод [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Метод [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) принимает индекс строки, в которую будет вставлена новая строка.

```c++
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как вставить несколько строк**

Чтобы вставить несколько строк в лист, вызовите метод [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Метод [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) принимает два параметра:

- Индекс строки, индекс строки, с которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

```c++
#include <iostream>
#include <fstream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Как вставить строку с форматированием**

Для вставки строки с параметрами форматирования используйте перегрузку [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/), которая принимает [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) в качестве параметра. Установите свойство [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) класса [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) со значением [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) Enum. Перечисление [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) содержит три члена, перечисленные ниже.

- SameAsAbove: Форматирует строку так же, как и вышеуказанная.
- SameAsBelow: Форматирует строку так же, как и нижеуказанная.
- Очистить: Очищает форматирование.

```c++
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как вставить столбец**

Разработчики также могут вставлять столбец в лист в любой точке, вызвав метод [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Метод [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) принимает индекс столбца, в который будет вставлен новый столбец.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Удалить строки и столбцы**

### **Как удалить несколько строк**

Для удаления нескольких строк из листа вызовите метод [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Метод [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые нужно удалить.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как удалить столбец**

Чтобы удалить столбец из листа в любой точке, вызовите метод [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Метод [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) принимает индекс столбца для удаления.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
