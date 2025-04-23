---
title: 使用C++进行汇总功能
linktitle: 合并函数
type: docs
weight: 20
url: /zh/cpp/consolidation-function/
description: 学习如何使用Aspose.Cells结合C++对数据透视表的字段应用汇总函数。
---

## **合并函数**

Aspose.Cells 可用于将合并函数应用于数据透视表的数据字段（或值字段）。在 Microsoft Excel 中，您可以右键单击值字段，然后选择“值字段设置...”选项，然后选择选项卡“按以下方式汇总值”。从那里，您可以选择任何您喜欢的合并函数，如求和、计数、平均值、最大值、最小值、乘积、去重计数等。

Aspose.Cells提供[**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/)枚举以支持以下合并功能。

- 汇总函数::平均值
- 汇总函数::计数
- 汇总函数::计数字符串
- 汇总函数::唯一计数
- 汇总函数::最大值
- 汇总函数::最小值
- 汇总函数::乘积
- 汇总函数::标准偏差
- 汇总函数::总体标准偏差
- 汇总函数::总和
- 汇总函数::方差
- 汇总函数::总体方差

### **应用合并功能到数据字段的数据透视表**

以下代码将**平均值**整合函数应用于第一个数据字段（或数值字段），将**不重复计数**整合函数应用于第二个数据字段（或数值字段）。

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
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Microsoft Excel 2013仅支持去重计数合并功能。

{{% /alert %}}
