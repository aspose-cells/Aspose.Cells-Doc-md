---
title: Форматирование сводных таблиц с помощью C++
linktitle: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/cpp/formatting-pivot-table/
description: Научитесь настраивать внешний вид сводных таблиц с помощью Aspose.Cells for C++.
---

## **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описано, как настроить внешний вид сводной таблицы, устанавливая различные свойства:

- Опции формата сводной таблицы
- Опции формата полей сводной таблицы
- Опции формата данных поля

### **Настройка параметров формата сводной таблицы**

Класс [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) контролирует общую сводную таблицу и может быть отформатирован различными способами.

#### **Установка типа автоформата**

Microsoft Excel предлагает множество предустановленных форматов отчетов. Aspose.Cells также поддерживает эти параметры форматирования. Чтобы получить к ним доступ:

1. Установите [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isautoformat/) в **true**.
1. Назначьте опцию форматирования из перечисления [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottableautoformattype/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    int pivotindex = 0;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report is automatically formatted
    pivotTable.SetIsAutoFormat(true);

    // Setting the PivotTable autoformat type
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Настройка параметров формата**

Образец кода ниже показывает, как отформатировать сводную таблицу для отображения итоговых сумм по строкам и столбцам, а также как задать порядок полей отчета. Он также показывает, как установить пользовательскую строку для null значений.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Setting the PivotTable report shows grand totals for columns.
    pivotTable.SetShowColumnGrandTotals(true);

    // Setting the PivotTable report displays a custom string in cells that contain null values.
    pivotTable.SetDisplayNullString(true);
    pivotTable.SetNullString(u"null");

    // Setting the PivotTable report's layout
    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Форматирование внешнего вида вручную**

Для ручного форматирования вида отчета сводной таблицы вместо использования предустановленных форматов используйте методы [**PivotTable.Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) и [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). Создайте объект стиля для желаемого форматирования, например:

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    auto pivot = worksheet.GetPivotTables().Get(0);

    // Set pivot table style
    pivot.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    // Create a new style
    Style style = workbook.CreateStyle();
    style.GetFont().SetName(u"Arial Black");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    // Apply style to pivot table
    pivot.FormatAll(style);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table style applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Настройка параметров формата поля сводной таблицы**

Класс [**PivotField**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/) представляет собой поле в сводной таблице и может быть отформатировано несколькими способами. Приведенный ниже образец кода показывает, как:

- Получить строковые поля.
- Настроить итоги.
- Настроить автосортировку.
- Настроить автоотображение.

#### **Настройка формата полей строки/столбца/страницы**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"Book1.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Accessing the row fields.
    PivotFieldCollection pivotFields = pivotTable.GetRowFields();

    // Accessing the first row field in the row fields.
    PivotField pivotField = pivotFields.Get(0);

    // Setting Subtotals.
    pivotField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    pivotField.SetSubtotals(PivotFieldSubtotalType::Count, true);

    // Setting autosort options.
    // Setting the field auto sort.
    pivotField.SetIsAutoSort(true);

    // Setting the field auto sort ascend.
    pivotField.SetIsAscendSort(true);

    // Setting the field auto sort using the field itself.
    pivotField.SetAutoSortField(-5);

    // Setting autoShow options.
    // Setting the field auto show.
    pivotField.SetIsAutoShow(true);

    // Setting the field auto show ascend.
    pivotField.SetIsAscendShow(false);

    // Setting the auto show using field(data field).
    pivotField.SetAutoShowField(0);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установка формата полей данных**

Приведенный ниже образец кода показывает, как установить формат отображения и числовой формат для полей данных.

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

    // Load a template file
    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::PercentageOf);

    // Setting the base field
    pivotField.GetShowValuesSetting().SetBaseFieldIndex(1);

    // Setting the base item
    pivotField.GetShowValuesSetting().SetBaseItemPositionType(PivotItemPositionType::Next);

    // Setting number format
    pivotField.SetNumber(10);

    // Saving the Excel file
    U16String outputFilePath = outDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Очистка полей сводной таблицы**

У класса [**PivotFieldCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/) есть метод с именем [**Clear()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/clear/), который позволяет очистить поля сводной таблицы. Используйте его, когда вам нужно очистить все поля сводной таблицы в областях, например страница, столбец, строка или данные.
Приведенный ниже образец кода показывает, как очистить все поля сводной таблицы в области данных.

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the pivot tables in the sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();

    // Get the first PivotTable
    PivotTable pivotTable = pivotTables.Get(0);

    // Clear all the data fields
    pivotTable.GetDataFields().Clear();

    // Add new data field
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Betrag Netto FW");

    // Set the refresh data flag off
    pivotTable.SetRefreshDataFlag(false);

    // Refresh and calculate the pivot table data
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
