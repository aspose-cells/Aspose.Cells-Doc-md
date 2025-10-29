---
title: 刷新和计算含有计算项数据透视表，使用 C++
linktitle: 刷新和计算包含计算项的数据透视表
type: docs
weight: 40
url: /zh/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: 使用 Aspose.Cells 和 C++ 刷新并计算包含计算项的数据透视表。
---

{{% alert color="primary" %}}

Aspose.Cells现在支持刷新和计算包含计算项的数据透视表。请像往常一样使用[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/)和[**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)执行此功能。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

以下示例代码加载了包含三个计算项（如“add”、“div”、“div2”）的[源 Excel 文件](5115238.xlsx)，首先将单元格 D2 的值修改为 20，然后使用 Aspose.Cells API 刷新并计算数据透视表，并将工作簿保存为 PDF 格式。生成的 [输出 PDF](5115229.pdf) 证明 Aspose.Cells 成功刷新和计算了包含计算项的数据透视表。可以通过手动在 D2 输入 20 并用 Alt+F5 快捷键或点击数据透视表的刷新按钮，使用 Microsoft Excel 进行验证。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
