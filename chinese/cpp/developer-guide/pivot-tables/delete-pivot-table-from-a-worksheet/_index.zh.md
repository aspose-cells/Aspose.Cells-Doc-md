---
title: 用 C++ 从工作表中删除数据透视表
linktitle: 删除数据透视表
type: docs
weight: 60
url: /zh/cpp/delete-pivot-table-from-a-worksheet/
description: 使用 Aspose.Cells 的 C++ 代码删除 Excel 工作表中的数据透视表。
keywords: C++ 从工作表中删除数据透视表，C++ 删除 Excel 数据透视表，如何用 C++ 删除数据透视表，删除数据透视表，删除 Excel 中的数据透视表，C++ 删除数据透视表，C++ 移除数据透视表，移除数据透视表，删除数据透视表，如何删除数据透视表
---

{{% alert color="primary" %}}

Aspose.Cells提供了一个功能，用于删除或移除工作表中的数据透视表。您可以使用数据透视表对象或数据透视表位置来删除数据透视表。请使用[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/)方法使用数据透视表对象来删除数据透视表，使用其位置在数据透视表集合内[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/)方法删除数据透视表对象。

{{% /alert %}}

以下示例代码从工作表中删除两个数据透视表。首先，它使用 [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) 方法移除数据透视表，然后使用 [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) 方法继续移除。

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
