---
title: 使用 C++ 禁用数据透视表功能区
linktitle: 禁用数据透视表功能区
type: docs
weight: 90
url: /zh/cpp/disable-pivot-table-ribbons/
description: 学习如何使用 Aspose.Cells for C++ 禁用 Excel 文件中的数据透视表工具栏。
---

{{% alert color="primary" %}}

基于数据透视表的报表很有用，但如果目标用户没有详细的Excel知识来配置这些报表，则容易出错。在此情况下，组织通常会限制用户更改基于数据透视表的报表。添加额外过滤器、切片器、字段或更改报表中某些内容的顺序等常用功能，通常不建议每个用户都能使用。另一方面，这些用户仍应能够刷新报表和使用现有的过滤器或切片器。Aspose.Cells 为开发者提供了限制用户更改这些报表的能力。在创建这些报表时，Excel 提供了禁用数据透视表工具栏的功能，同样由 Aspose.Cells 提供。开发者可以禁用包含修改这些报表控件的工具栏。

{{% /alert %}}

## **使用PivotTable.EnableWizard禁用数据透视表功能区**

以下代码通过访问工作表中的数据透视表，并将 [**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) 设置为 **false** 来演示此功能。可以从[此链接](pivot_table_test.xlsx)下载示例数据透视表文件。

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
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
