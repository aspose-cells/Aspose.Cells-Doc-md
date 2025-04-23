---
title: Автоматическая настройка строк и столбцов с помощью C++
linktitle: Автоподбор строк и столбцов
type: docs
weight: 20
url: /ru/cpp/autofit-rows-and-columns/
description: В этой статье показано, как автоматически подгонять строки, столбцы, строки объединённых ячеек и строки в диапазоне ячеек с помощью API Aspose.Cells for C++.
keywords: Автоподбор строк, автоподбор столбцов, автоподбор строки в диапазоне ячеек, автоподбор строк объединенных ячеек
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям автоматически изменять ширину и высоту ячеек в соответствии с их содержимым. Эта функция также доступна через Aspose.Cells, поэтому разработчики могут автоматически подгонять размеры ячейки во время выполнения.

{{% /alert %}}

## **Автоматическая подгонка размера**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет обращаться к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов для управления рабочим листом. В этой статье рассматривается использование класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) для автоматической подгонки строк или столбцов.

### **Автоматическая подгонка строки - простой**

Самый простой способ автоматически подогнать ширину и высоту строки — вызвать метод [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Метод [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) принимает индекс строки (подгоняемой) в качестве параметра.

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

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Как автоматически подогнать строку в диапазоне ячеек**

Строка состоит из многих столбцов. Aspose.Cells позволяет автоматически подгонять строку на основе содержимого в диапазоне ячеек внутри строки, вызвав переопределённую версию метода [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/). Он принимает следующие параметры:

- Индекс строки, индекс строки, которую нужно автоматически подогнать.
- Индекс первого столбца, индекс первого столбца строки.
- Индекс последнего столбца, индекс последнего столбца строки.

Метод [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) проверяет содержимое всех столбцов в строке и затем автоматически подгоняет ее.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как автоматически подогнать столбец в диапазоне ячеек**

Столбец состоит из многих строк. Можно автоматически подогнать столбец на основе содержимого в диапазоне ячеек в столбце, вызвав переопределённую версию метода [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/), которая принимает следующие параметры:

- Индекс столбца, индекс столбца, который нужно автоматически подогнать.
- Индекс первой строки, индекс первой строки столбца.
- Индекс последней строки, индекс последней строки столбца.

Метод [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) проверяет содержимое всех строк в столбце и затем автоматически подгоняет его.

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

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Как автоматически подогнать строки для объединенных ячеек**

С помощью Aspose.Cells возможно автоматически подгонять строки даже для ячеек, объединённых с помощью API [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/). Класс [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) предоставляет свойство [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/), которое можно использовать для автоматической подгонки строк для объединённых ячеек. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) принимает перечисление [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/), которое включает следующие значения:

- None: игнорировать объединённые ячейки.
- FirstLine: расширяет только высоту первой строки.
- LastLine: расширяет только высоту последней строки.
- EachLine: расширяет высоту каждой строки.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Вы также можете попробовать использовать переопределённые версии методов [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) и [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/), которые принимают диапазон строк/столбцов и экземпляр [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) для автоподгонки выбранных строк/столбцов с нужными параметрами [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/).

Подписи указанных методов следующие:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)

{{% /alert %}}

## **Важно знать**

{{% alert color="primary" %}}

Если ячейка объединена, методы AutoFit не будут применяться, что является поведением, аналогичным Microsoft Excel. Можно обойти это, используя API автофильтра. Кроме того, если текст в ячейке обёрнут, метод [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) также не будет применён. Другой важный момент — методы *AutoFit* требуют много времени, потому их нужно вызывать как можно реже для повышения эффективности вашего приложения.

{{% /alert %}}

## **Дополнительные темы**
- [AutoFit строк для объединенных ячеек](/cells/ru/cpp/autofit-rows-for-merged-cells/)
