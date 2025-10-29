---
title: 将CSV转换为JSON，使用C++
linktitle: 将CSV转换为JSON
type: docs
weight: 220
url: /zh/cpp/convert-csv-to-json/
description: 使用简单易用的Aspose.Cells for C++ API将CSV文件转换为JSON。
keywords: 转换，转换CSV为JSON，CSV转JSON，CSV，JSON，使用C++将CSV转换为JSON的代码
---

## **将CSV转换为JSON**

Aspose.Cells支持将CSV转换为JSON。为此，API提供了[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)和[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)类。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)类提供导出范围至JSON的选项。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)类具有以下属性：

- [**GetExportAsString()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getexportasstring/)：导出单元格的字符串值给JSON。
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/gethasheaderrow/)：指示范围是否包含标题行。
- [**GetIndent()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getindent/)：指示缩进。

[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)类使用[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)类设置的导出选项导出JSON。

以下代码示例演示了如何使用 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类加载 [源 CSV 文件](104398879.csv) 并在控制台中打印 JSON 输出。

### **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options for CSV format
    LoadOptions loadOptions(LoadFormat::Csv);

    // Load CSV file
    Workbook workbook(srcDir + u"SampleCsv.csv", loadOptions);

    // Get the last cell in the worksheet
    Cell lastCell = workbook.GetWorksheets().Get(0).GetCells().GetLastCell();

    // Set JsonSaveOptions
    JsonSaveOptions jsonSaveOptions;

    // Create a range from the first cell to the last cell
    Range range = workbook.GetWorksheets().Get(0).GetCells().CreateRange(0, 0, lastCell.GetRow() + 1, lastCell.GetColumn() + 1);

    // Export the range to JSON
    U16String data = JsonUtility::ExportRangeToJson(range, jsonSaveOptions);

    // Print JSON
    std::cout << data.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **控制台输出**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
