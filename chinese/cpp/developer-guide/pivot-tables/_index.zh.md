---
title: 创建数据透视表
linktitle: 创建数据透视表
description: 使用 Aspose.Cells for C++ 创建数据透视表并设置其格式。
keywords: 创建数据透视表, 插入数据透视表, 设置数据透视表格式。
type: docs
weight: 160
url: /zh/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **什么是数据透视表？**
数据透视表是一种交互式汇总报表：无需使用任何公式，即可将大量逐行排列的原始数据汇总为紧凑的矩阵。您可以选择将哪些列用作行标签、哪些列用作列标签，以及将哪些列作为值进行聚合——数据透视表负责分组和计算：
- **汇总** — 按产品、地区或季度汇总销售额，无需冗长的公式链。
- **比较** — 将类别置于行中、将时间段置于列中，可将扁平列表转换为交叉分析报表，一眼即可看出趋势。
- **下钻** — 双击任意汇总值，查看其对应的源行。
- **刷新** — 源数据发生变化时，只需刷新一次即可重新计算整个报表。
常见应用场景包括销售仪表板、费用构成分析和库存分析，可回答“这些数字如何按类别和时间细分？”之类的问题。在 Aspose.Cells for C++ 中，可通过工作表的 [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) 方法创建数据透视表。创建数据透视表后，可使用 [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) 类对其进行操作。

## **创建数据透视表**
以下示例代码演示了如何创建数据透视表并对其进行操作。请查看使用此代码生成的[输出 Excel 文件](23167010.xlsx)，以及下方显示该文件在 Microsoft Excel 中的呈现效果的屏幕截图。
![数据透视表输出示例](create-pivot-table_1.png)

## **示例代码**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // 创建一个新工作簿并获取第一个工作表
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // 写入源数据：每个运动项目和季度的销售额
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // 在目标单元格 E3 处添加数据透视表，数据源为 A1:C8
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // 分配数据透视表字段：将 Sport 放置在行区域，将 Quarter 放置在列区域，将 Sales 放置在数据区域
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // 保存工作簿
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}