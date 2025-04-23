---
title: 用C++根据原始值搜索数据
linktitle: 使用原始值搜索数据
type: docs
weight: 380
url: /zh/cpp/search-data-using-original-values/
description: 学习如何通过Aspose.Cells for C++ API根据原始值进行数据搜索。
keywords: 使用原始值搜索数据，使用原始值查找数据，按原始值搜索数据，按原始值查找数据
---

{{% alert color="primary" %}}

有时，数据的值因为以某种方式格式化而被隐藏。例如，假设单元格 D4 公式为 =Sum(A1:A2) 并且其值为 20 但格式为---，那么值 20 将被隐藏，并且无法使用 Microsoft Excel 查找选项找到。但是，您可以使用 Aspose.Cells 使用 [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/) 找到它

{{% /alert %}}

以下示例代码说明了上述观点。它会找到无法使用Microsoft Excel的查找选项找到的单元格D4，但Aspose.Cells可以使用[**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/)找到它。请阅读代码内的注释以获取更多信息。

## 使用原始值搜索数据的C++代码

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

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add 10 in cell A1 and A2
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(10);

    // Add Sum formula in cell D4 but customize it as ---
    Cell cell = worksheet.GetCells().Get(u"D4");

    Style style = cell.GetStyle();
    style.SetCustom(u"---", true);
    cell.SetStyle(style);

    // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
    cell.SetFormula(u"=Sum(A1:A2)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
    FindOptions options;
    options.SetLookInType(LookInType::OriginalValues);
    options.SetLookAtType(LookAtType::EntireContent);

    Cell foundCell;
    int32_t obj = 20;

    // Find 20 which is Sum(A1:A2) and formatted as ---
    foundCell = worksheet.GetCells().Find(obj, foundCell, options);

    // Print the found cell
    std::cout << foundCell.ToString().ToUtf8() << std::endl;

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## 示例代码生成的控制台输出

这是上面示例代码的控制台输出。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
