---
title: 用C++读写带有查询表数据源的表格
linktitle: 读取和写入带有查询表数据源的表格
type: docs
weight: 30
url: /zh/cpp/read-and-write-table-with-query-table-data-source/
description: 学习如何用Aspose.Cells for C++读写带有QueryTable为数据源的表格。
---

## **读取和写入带有查询表数据源的表格**
使用Aspose.Cells可以读取和写入带有QueryTable作为数据源的表格。这项支持适用于XLS文件。以下代码演示了如何读取和写入此类表格，先读取表格，再修改它以添加总计行。

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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

源文件和输出文件已附在此供参考。

[源文件](96928091.xls)

[输出文件](96928092.xls)
