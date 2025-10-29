---
title: 使用C++设置数据透视表选项——空单元格显示
linktitle: 设置数据透视表选项  对空单元格显示
type: docs
weight: 40
url: /zh/cpp/setting-pivot-table-option-for-empty-cells-show/
description: 学习如何在使用Aspose.Cells的C++中设置数据透视表中的“空单元格显示”选项。
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells设置不同的数据透视表选项。其中之一是"对空单元格显示"选项。通过设置此选项，数据透视表中的所有空单元格将显示为指定的字符串。

{{% /alert %}}

## **在Microsoft Excel中设置数据透视表选项**

要在Microsoft Excel中查找并设置此选项：

1. 选择数据透视表，右键单击。
2. 选择**数据透视表选项**。
3. 选择**布局和格式**选项卡。
4. 选择**对空单元格显示**选项并指定字符串。

## **使用Aspose.Cells设置数据透视表选项**

Aspose.Cells提供用于设置"对空单元格显示"数据透视表选项的[**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/)和[**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/)属性。

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
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 相关文章

- [格式化数据透视表](/cells/zh/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
