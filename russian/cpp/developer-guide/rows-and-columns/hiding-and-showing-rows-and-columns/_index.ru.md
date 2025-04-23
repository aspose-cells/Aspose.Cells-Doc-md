---
title: Скрытие и отображение строк и столбцов с помощью C++
linktitle: Скрытие и отображение строк и столбцов
type: docs
weight: 60
url: /ru/cpp/hiding-and-showing-rows-and-columns/
description: Узнайте, как программно скрывать и показывать строки и столбцы в файлах Excel с помощью Aspose.Cells на C++.
---

{{% alert color="primary" %}}

Иногда имеет смысл скрыть некоторые строки или столбцы в листе и отображать их позже. Эта функция есть в Microsoft Excel и в Aspose.Cells.

{{% /alert %}}

## **Управление видимостью строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющий разработчикам обращаться к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), представляющую все ячейки на листе. Коллекция [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них рассмотрены ниже.

### **Скрытие строк и столбцов**

Разработчики могут скрыть строку или столбец, вызвав методы [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) и [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) соответственно из коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Оба метода принимают индекс строки и столбца в качестве параметра для скрытия конкретной строки или столбца.

```c++
#include <iostream>
#include <memory>
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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.

{{% /alert %}}

### **Показ строк и столбцов**

Разработчики могут показать любую скрытую строку или столбец, вызвав методы [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) и [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) из коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.

```cpp
#include <iostream>
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

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

При отображении скрытого столбца, если нужно восстановить его ранее установленную ширину или исходную ширину, пожалуйста, сделайте скрытие столбца с отрицательной шириной, например: `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **Скрытие нескольких строк и столбцов**

Разработчики могут скрыть сразу несколько строк или столбцов, вызвав методы [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) и [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) из коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Оба метода принимают начальный индекс строки или столбца и количество строк или столбцов, которые должны быть скрыты.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Также можно использовать методы [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) и [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) класса [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), чтобы сделать видимыми несколько строк и столбцов.

{{% /alert %}}
