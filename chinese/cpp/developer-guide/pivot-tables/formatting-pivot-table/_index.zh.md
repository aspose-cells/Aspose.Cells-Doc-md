---
title: 用 C++ 格式化数据透视表
linktitle: 格式化数据透视表
type: docs
weight: 10
url: /zh/cpp/formatting-pivot-table/
description: 学习如何使用 Aspose.Cells for C++ 自定义数据透视表的外观。
---

## **数据透视表外观**

如何创建数据透视表介绍了如何创建简单的数据透视表。本文描述了如何通过设置各种属性来自定义数据透视表的外观:

- 数据透视表格式选项
- 数据透视字段格式选项
- 数据字段格式选项

### **设置数据透视表格式选项**

[**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/)类控制整体数据透视表，可以以多种方式进行格式设置。

#### **设置自动格式类型**

微软 Excel 提供多种预设的报表格式。Aspose.Cells 也支持这些格式。访问方式：

1. 将[**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isautoformat/)设置为**true**。
1. 从[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottableautoformattype/)枚举中分配一个格式选项。

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

#### **设置格式选项**

下面的代码示例演示如何格式化数据透视表以显示行和列的总计，以及如何设置报表的字段顺序。还演示了如何为空值设置自定义字符串。

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

#### **手动设置外观和感觉格式**

要手动调整数据透视表报告的显示方式，而不是使用预设的报表格式，可以使用 [**PivotTable.Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) 和 [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) 方法。创建一个样式对象以实现所需的格式，例如：

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

### **设置数据透视字段格式选项**

[**PivotField**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/)类表示数据透视表中的字段，并可以以多种方式进行格式设置。下面的代码示例演示了如何:

- 访问行字段。
- 设置合计。
- 设置自动排序。
- 设置自动显示。

#### **设置行/列/页字段格式**

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

### **设置数据字段格式**

以下代码示例显示如何设置数据字段的显示格式和数字格式。

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

### **清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/) 有一个名为 [**Clear()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/clear/) 的方法，允许您清除数据透视字段。当您想要清除区域中的所有数据透视字段时（例如页、列、行或数据），请使用它。
以下代码示例显示如何清除数据区域中的所有数据透视字段。

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
