---
title: Aspose.Cells for C++ 中的值字段
description: 了解如何在 Aspose.Cells for C++ 中将基础字段添加到数据透视表的数据区域，使用 PivotField.Function 更改汇总函数，并将值字段绘制到行轴或列轴上。
linktitle: Aspose.Cells for C++ 中的值字段
keywords: Aspose.Cells, C++, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 将字段添加到数据区域
将基础字段添加到数据（值）区域是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开了 `PivotTable.AddFieldToArea(PivotFieldType, string)` 重载，该重载接受常量 `PivotFieldType.Data` 和源列名称。字段添加到数据区域后，API 会通过 `PivotTable.DataFields` 集合公开它，按添加字段的顺序排列。默认情况下，数值型源列使用 `ConsolidationFunction.Sum` 进行汇总，而非数值型列默认使用 `Count`。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
 Aspose::Cells::Startup();
 Workbook workbook;
 Worksheet worksheet = workbook.GetWorksheets().Get(0);
 worksheet.SetName(u"Data");
 Cells cells = worksheet.GetCells();
 // A1:D1 中的表头
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));
 // 使用嵌套循环根据 j 分支处理 A2:D9 的数据行
 for (int i = 1; i <= 8; i++)
 {
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
 break;
 case 1:
 if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
 else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
 else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
 else cells.Get(i, j).PutValue(U16String("Daikon"));
 break;
 case 2:
 cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) cells.Get(i, j).PutValue(100);
 else if (i == 2) cells.Get(i, j).PutValue(150);
 else if (i == 3) cells.Get(i, j).PutValue(80);
 else if (i == 4) cells.Get(i, j).PutValue(90);
 else if (i == 5) cells.Get(i, j).PutValue(50);
 else if (i == 6) cells.Get(i, j).PutValue(60);
 else if (i == 7) cells.Get(i, j).PutValue(40);
 else cells.Get(i, j).PutValue(45);
 break;
 }
 }
 }
 // 在 F3 位置添加名为 PivotTable1 的数据透视表
 PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);
 // 数据透视表布局：Category 和 Item 作为行，Year 作为列，Amount 作为数据字段
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");
 Aspose::Cells::Cleanup();
 return 0;
}
```

## 更改汇总函数
放置在数据区域中的每个字段在内部都被包装为 `PivotField` 实例，其 `Function` 属性返回 `ConsolidationFunction` 枚举中的值。同一个 `Function` setter 允许您在可用的聚合之间切换，包括 `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var` 和 `Varp`。

{{% alert color="primary" %}}
更改 `Function` 仅影响聚合，源列不会改变。
因此，您可以将一个数据字段保留为 `Sum`，同时添加第二个针对同一源列但使用 `Count` 或 `Average` 的数据字段，所有这些都在单个数据透视表中完成。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana", u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) {
                worksheet.GetCells().Get(i, j).PutValue(i <= 4 ? u"Fruit" : u"Vegetable");
            } else if (j == 1) {
                worksheet.GetCells().Get(i, j).PutValue(items[i - 1]);
            } else if (j == 2) {
                worksheet.GetCells().Get(i, j).PutValue(years[i - 1]);
            } else {
                worksheet.GetCells().Get(i, j).PutValue(amounts[i - 1]);
            }
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField countField = pivotTable.GetDataFields().Get(1);
    countField.SetFunction(ConsolidationFunction::Count);

    pivotTable.CalculateData();

    wb.Save(u"output_function.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 将值字段绘制到行轴或列轴
当数据透视表包含两个或更多数据字段时，Aspose.Cells 会公开一个额外的虚拟字段，称为 `PivotTable.ValuesField`。此虚拟字段表示数据区域中每个数据字段的聚合。您可以将其作为基础数据透视字段拖到行区域或列区域，这对于将多个度量并排排列非常有用。

{{% alert color="primary" %}}
如果没有值字段或只有一个值字段，则 `PivotTable.ValuesField` 不起作用。
以下场景通过三个端到端示例演示了针对同一数据透视结构上述每项功能。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Category"));
    cells.Get(0, 1).PutValue(U16String("Item"));
    cells.Get(0, 2).PutValue(U16String("Year"));
    cells.Get(0, 3).PutValue(U16String("Amount"));

    std::vector<U16String> categories = {
        U16String("Fruit"), U16String("Fruit"), U16String("Fruit"), U16String("Fruit"),
        U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable")
    };
    std::vector<U16String> items = {
        U16String("Apple"), U16String("Apple"), U16String("Banana"), U16String("Banana"),
        U16String("Carrot"), U16String("Carrot"), U16String("Daikon"), U16String("Daikon")
    };
    int years[8] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[8] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) cells.Get(i, j).PutValue(categories[i - 1]);
            else if (j == 1) cells.Get(i, j).PutValue(items[i - 1]);
            else if (j == 2) cells.Get(i, j).PutValue(years[i - 1]);
            else cells.Get(i, j).PutValue(amounts[i - 1]);
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::Count);

    pivotTable.AddFieldToArea(PivotFieldType::Column, pivotTable.GetValuesField().GetName());

    pivotTable.CalculateData();
    workbook.Save(u"output_plot.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}