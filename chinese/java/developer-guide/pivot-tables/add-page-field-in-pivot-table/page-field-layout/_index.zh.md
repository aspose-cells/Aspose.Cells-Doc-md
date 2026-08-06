---
title: 修改数据透视表中的页面字段布局
linktitle: 修改数据透视表中的页面字段布局
description: 了解如何使用 Aspose.Cells for Java 控制数据透视表中页面字段区域的布局,包括设置页面字段在数据透视表顶部的显示顺序、换行数量以及字段顺序。
keywords: Aspose.Cells, Java 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数量, 移动页面字段
type: docs
weight: 191
url: /zh/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
本文是 **在数据透视表中添加页面字段** 主题的延续。它演示如何控制页面字段区域的布局,即数据透视表顶部的筛选控件条,包括显示顺序、换行数量以及字段重新排序。
{{% /alert %}}
## **简介**
Microsoft Excel 中的数据透视表提供了一个专门的 **页面字段区域**,位于表格的行/列/数据主体的上方。该区域呈现为一行下拉筛选控件条(每个页面字段一个),用户点击它可以按年份或区域等条件对数据透视表进行切片。Aspose.Cells 通过 `pivotTable.getPageFields()` 集合对该区域进行建模,并提供三个属性来控制该控件条的视觉布局:
- `pivotTable.getPageFieldOrder()`(一个 `Aspose.Cells.PrintOrderType` 值)决定额外的页面字段是 *横向* 排列在现有字段旁边,还是 *纵向* 排列在它们下方。
- `pivotTable.getPageFieldWrapCount()` 设置在换行之前每行或每列放置的页面字段数量。
- `pivotTable.getPageFields().move(currIndex, destIndex)` 重新排序页面字段而不改变顺序模式。
本文通过三个代码示例演示如何在共享数据集上分别执行这些操作,以便您可以并排比较生成的布局。
## **源数据**
下面的所有三个示例将这八行销售数据加载到名为 `PivotData` 的工作表中。数据包含两个页面字段候选项(`Year`、`Region`)、一个行字段候选项(`Fruit`)和一个度量值(`Amount`),这使得页面字段条值得检查。
每个代码示例都以相同的顺序填充全部八行,因此各场景之间的源数据始终一致——只有页面字段的布局属性有所不同。
## **示例 1:先横向后纵向**
在第一个场景中,我们将两个页面字段(`Year`、`Region`)配置为在数据透视表顶部 **并排显示在同一行中**。我们将 `Fruit` 分配到行轴,按 `Year` 在前、`Region` 在后的顺序将字段放置到页面轴(`addFieldToArea` 调用的顺序决定起始索引),将 `Amount`(Sum)添加为数据字段,然后设置 `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` 和 `pivotTable.setPageFieldWrapCount(2)`。使用 `OVER_THEN_DOWN` 并将换行数量设为 2 时,两个页面字段将在数据透视表顶部并排水平排列成一行,因此该控件条占用宽度为 2 的一行。
```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();

// 表头（第 0 行）
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// 第 1 行：Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// 第 2 行：Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// 第 3 行：Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// 第 4 行：Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// 第 5 行：Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// 第 6 行：Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// 第 7 行：Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// 第 8 行：Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// 添加 PivotTableReport 工作表
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();

// 创建数据源为 PivotData!A1:D9 的数据透视表，放置在 PivotTableReport 的 A1 单元格
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// 添加字段
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // 水果
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // 年份
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // 区域
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // 金额
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);

// 配置页面字段区域布局：页面字段先行排列，每 2 个换行
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

// 刷新并计算
pivotTable.calculateData();

// 保存
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```
## **示例 2:先纵向后横向**
在此示例中,我们将 `Fruit` 放在行轴上,将 `Year` 和 `Region` 放在页面轴上(`Year` 在前),并将 `Amount`(Sum)作为数据字段——与示例 1 完全相同。然后我们设置 `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` 和 `pivotTable.setPageFieldWrapCount(2)`。使用 `DOWN_THEN_OVER` 并将换行数量设为 2 时,两个页面字段将垂直堆叠——`Year` 在顶部,`Region` 直接位于其下方——在数据透视表顶部形成一列。因此,该控件条占用宽度为 1 的两行,与示例 1 形成对比。
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");

String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **示例 3:移动页面字段**
在第三个场景中,我们保留相同的数据集和字段分配,设置中性布局(`OVER_THEN_DOWN`,换行数量为 `2`),然后演示 `pageFields.move` 操作。`move(0, 1)` 调用将索引 0 处的页面字段(`Year`)移动到位置 1,而原来位于位置 1 的页面字段(`Region`)则移到位置 0。此调用之后,`Region` 成为第一个页面字段,`Year` 成为第二个。换行和顺序模式保持不变,因此控件条仍然以水平并排的方式呈现——只是两个下拉框的顺序被交换了。
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");

int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **相关文章**
- [在数据透视表中添加页面字段](/cells/zh/java/add-page-field-in-pivot-table/) — 介绍如何将页面字段添加到数据透视表的父页面。
- [数据透视表中的行和列字段](/cells/zh/java/row-and-column-fields/) — 涵盖将字段分配到行轴和列轴,补充此处展示的页面轴工作。
- [管理数据透视表中的值字段](/cells/zh/java/manage-value-fields/) — 描述如何配置数据(值)区域,包括本文使用的 `Sum` 聚合。
- [刷新数据透视表](/cells/zh/java/refresh-pivot-table/) — 解释 `refreshData()` 和 `calculateData()`,这是在重新排序页面字段后所需的。
- [对数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/) — 演示如何在页面字段条布局完成后格式化呈现的数据透视表。
{{< app/cells/assistant language="java" >}}