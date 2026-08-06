---
title: 修改数据透视表中的页面字段布局
linktitle: 修改数据透视表中的页面字段布局
description: 学习如何使用 Aspose.Cells for C++ 控制数据透视表中页面字段区域的布局，包括设置页面字段在数据透视表顶部的显示顺序、换行数和字段顺序。
keywords: Aspose.Cells, C++ 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数, 移动页面字段
type: docs
weight: 191
url: /zh/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
本文是 **在数据透视表中添加页面字段** 主题的延续。它演示了如何控制页面字段区域的布局（即数据透视表顶部的筛选控件条），包括显示顺序、换行数和字段重新排序。
{{% /alert %}}
## **简介**
Microsoft Excel 中的数据透视表具有一个专用的 **页面字段区域**，位于表格的行/列/数据主体之上。该区域以一排下拉筛选控件（每个页面字段一个）的形式呈现，最终用户通过点击它来按年份或地区等条件切片数据透视表。Aspose.Cells for C++ 通过 `PivotTable.PageFields` 集合对该区域进行建模，并提供以下三个属性来控制该控件条的视觉布局：
- `PivotTable.PageFieldOrder`（一个 `Aspose.Cells.PrintOrderType` 枚举值）决定其他页面字段是 *放置在* 现有字段 *旁边* 还是 *下方*。
- `PivotTable.PageFieldWrapCount` 设置每行或每列在换行之前可放置的页面字段数量。
- `PivotTable.PageFields.Move(currIndex, destIndex)` 在不更改排序模式的情况下重新排序页面字段。
本文通过三个代码示例，在同一共享数据集上演示上述各项操作，方便您并排比较生成的布局效果。
## **源数据**
下面的三个示例都将这八行销售数据加载到名为 `PivotData` 的工作表中。数据包含两个页面字段候选项（`Year`、`Region`）、一个行字段候选项（`Fruit`）和一个度量值（`Amount`），这使得页面字段条的检查具有实际意义。
在每个代码示例中，这八行数据都按相同的顺序填充，因此各场景之间的源数据完全一致——只有页面字段布局属性不同。
## **示例 1：先行后列**
在第一个场景中，我们将两个页面字段（`Year`、`Region`）配置为 **在数据透视表顶部以单行水平并排显示**。我们把 `Fruit` 分配到行轴，将 `Year` 放在页面轴的第一位，`Region` 放在第二位（`AddFieldToArea` 调用的顺序决定起始索引），并将 `Amount`（Sum）添加为数据字段，然后将 `PageFieldOrder` 设置为 `PrintOrderType.OverThenDown`，并将 `PageFieldWrapCount` 设为 `2`。使用 `OverThenDown` 配合换行数 2 时，两个页面字段会在数据透视表顶部以单行水平并排显示，因此该控件条占据宽度为 2 的一行。
```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // 表头（第0行）
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // 第1行：苹果，2022，北方，150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // 第2行：苹果，2023，北方，180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // 第3行：香蕉，2022，南方，120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // 第4行：香蕉，2023，南方，140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // 第5行：樱桃，2022，东方，200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // 第6行：樱桃，2023，东方，220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // 第7行：葡萄，2022，西方，90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // 第8行：葡萄，2023，西方，110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // 添加数据透视表报表工作表
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // 在 PivotTableReport 工作表的 A1 位置创建数据源为 PivotData!A1:D9 的数据透视表
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // 添加字段
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // 水果
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // 年份
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // 地区
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // 金额
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // 配置页面字段区域布局：先水平放置页面字段，每2个换行
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // 刷新并计算
    pivotTable.CalculateData();

    // 保存
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **示例 2：先列后行**
在本示例中，我们将 `Fruit` 放在行轴上，将 `Year` 和 `Region` 放在页面轴上（`Year` 在前），并将 `Amount`（Sum）作为数据字段——与示例 1 完全相同。然后将 `PageFieldOrder` 设置为 `PrintOrderType.DownThenOver`，并将 `PageFieldWrapCount` 设置为 `2`。使用 `DownThenOver` 配合换行数 2 时，两个页面字段会垂直堆叠——`Year` 在顶部，`Region` 直接位于下方——在数据透视表顶部形成单列。因此与示例 1 不同，该控件条占据宽度为 1 的两行。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **示例 3：移动页面字段**
在第三个场景中，我们保留该数据集和字段分配，设置一个中性布局（`OverThenDown` 配合换行数 `2`），然后演示 `PageFields.Move` 操作。`Move(0, 1)` 调用会将索引 0 处的页面字段（`Year`）移动到位置 1，而原本位于位置 1 的页面字段（`Region`）则移到位置 0。调用完成后，`Region` 成为第一个页面字段，`Year` 成为第二个页面字段。换行和排序模式保持不变，因此控件条仍然水平并排渲染——只是两个下拉控件的顺序发生了交换。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **相关文章**
- [在数据透视表中添加页面字段](/cells/zh/cpp/add-page-field-in-pivot-table/) — 父级页面，介绍如何向数据透视表添加页面字段。
- [数据透视表中的行和列字段](/cells/zh/cpp/row-and-column-fields/) — 介绍如何将字段分配到行轴和列轴，与本文所展示的页面轴操作互为补充。
- [管理数据透视表中的值字段](/cells/zh/cpp/manage-value-fields/) — 说明如何配置数据（值）区域，包括本文中使用的 `Sum` 聚合方式。
- [刷新数据透视表](/cells/zh/cpp/refresh-pivot-table/) — 解释 `RefreshData` 和 `CalculateData`，在重新排序页面字段后必须调用这些方法。
- [向数据透视表应用样式](/cells/zh/cpp/apply-style-to-pivot-table/) — 演示在页面字段条布局完成后，如何为渲染后的数据透视表设置格式。
{{< app/cells/assistant language="" >}}