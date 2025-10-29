---
title: 用C++读写工作表的查询表
linktitle: 工作表的查询表读取和写入
type: docs
weight: 40
url: /zh/cpp/reading-and-writing-query-table-of-worksheet/
description: 学习如何使用Aspose.Cells和C++读取和写入Excel工作表中的查询表。
---

{{% alert color="primary" %}}

Aspose.Cells提供`Worksheet.QueryTables`集合，通过索引返回`QueryTable`对象。它具有以下两个属性：

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

这些都是布尔值。你可以通过**Data > Connections > Properties**在Microsoft Excel中查看。

{{% /alert %}}

## 工作表的查询表读取和写入

以下示例代码读取第一个工作表的第一个`QueryTable`，并打印两个属性。然后将`QueryTable.PreserveFormatting`设为`true`。

您可以从以下链接下载用于此代码的源Excel文件和代码生成的输出Excel文件。

- [源Excel文件](5115533.xlsx)
- [输出Excel文件](5115537.xlsx)

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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### 控制台输出

上述示例代码的控制台输出：

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## 检索查询表结果范围

Aspose.Cells提供读取查询表结果范围地址（即单元格范围）的选项。以下代码演示了如何读取查询表的结果范围地址。示例文件可在[此处](72417290.xlsx)下载。

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
