---
title: 使用C++处理数据透视表的数据字段显示格式
linktitle: 操作数据透视表中的数据字段显示格式
type: docs
weight: 140
url: /zh/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: 学习如何使用Aspose.Cells for C++操作数据透视表中数据字段的显示格式。
---

{{% alert color="primary" %}}

Aspose.Cells支持数据透视表中所有数据字段的数据显示格式。

{{% /alert %}}

## **“从最小到最大排名”和“从最大到最小排名”显示格式选项**

Aspose.Cells提供设置数据透视字段显示格式的能力。API提供了 [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) 属性，要将排名从最大到最小设置，可以将 [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) 属性设置为 [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/)。以下代码片段演示了如何设置显示格式选项。

可从此处下载示例源文件和输出文件以测试示例代码:

[源 Excel 文件]（101089332.xlsx）

[输出 Excel 文件]（101089333.xlsx）

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
