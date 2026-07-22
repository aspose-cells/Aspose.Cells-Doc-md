---
title: 数据透视表中的页面字段
linktitle: 数据透视表中的页面字段
description: 学习如何使用 Aspose.Cells for Java 在数据透视表中添加和配置页面字段，包括添加页面字段、单选过滤和多选过滤。
keywords: Aspose.Cells, Java, 数据透视表, 页面字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 过滤
type: docs
weight: 250
url: /zh/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中页面字段的完整生命周期。您可以通过高级便捷 API 或通过底层 `PageFields` 集合来添加页面字段，并且可以以单选模式驱动页面筛选器、清除筛选器以显示每个页面项，或者将该字段切换为多选模式，以便用户通过 Excel 中的复选框 UI 一次选择多个页面项。
{{% /alert %}}

## **简介**

页面字段是一种透视字段，用于控制透视表主体所显示的源数据的*哪个子集*。最终用户将其视为 Excel 中已渲染透视表顶部的一个下拉列表，选择其中一个可用的页面项后，透视表主体会重新构建，从而仅汇总属于该页面项的记录。当一个透视字段被注册为 `PivotFieldType.Page` 而不是 `PivotFieldType.Row`、`PivotFieldType.Column` 或 `PivotFieldType.Data` 时，它就成为一个页面字段。

页面字段可以在两种行为模式下运行。在默认的**单选**行为模式下，一次只能显示一个页面项，因此透视表主体恰好汇总一个子集。在**多选**行为模式下，该字段会显示一个复选框列表，透视表主体会汇总所有被勾选的页面项的并集。同一源字段可以通过切换一个属性在这两种行为之间来回切换。

Aspose.Cells for Java 提供了两种等效的方式来注册页面字段。高级 API 是 `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")`，它接受源列名称，并通过一次调用添加该字段。底层 API 是 `PivotTable.PageFields.add(PivotField)`，当您已经持有 `PivotField` 引用并希望将同一字段实例添加到页面区域时，可以使用此 API。这两个 API 最终都会填充同一个 `PageFields` 集合，本文的其余部分将演示如何在这两者之间进行选择，以及如何驱动每种过滤模式。

## **添加页面字段**

有两种方法可以在页面区域中注册透视字段。高级调用以字符串形式接受源列名称，这是最常用的路径。底层调用接受现有的 `PivotField` 实例，当同一字段对象必须在多个透视区域中重用时，这种方式非常方便。这两种调用都会将该字段放入 `PivotTable.PageFields` 之中，之后它将作为页面下拉列表显示在已渲染透视表的顶部。

### 使用 addFieldToArea 添加页面字段

下面的示例构建一个小的 Fruit / Year / Amount 数据集，在 E3 单元格处放置一个数据透视表，将 `Fruit` 放在行区域，将 `Amount` 放在数据区域，将 `Year` 放在页面区域，刷新数据透视表，然后保存工作簿。

```java
import com.aspose.cells.*;

// 创建一个新的工作簿
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// 设置标题行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 填充 9 行示例数据：水果、年份、数量
Object[][] data = new Object[][]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// 在 E3 单元格添加数据透视表
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 将字段添加到相应区域：水果作为行字段，数量作为数据字段，年份作为页面筛选字段
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// 刷新并计算数据透视表数据
pivotTable.refreshData();
pivotTable.calculateData();

// 保存工作簿
workbook.save("pageFieldSample.xlsx");
```

### 使用 PageFields.add 添加页面字段

当您已经使用 `PivotField` 实例时，可以将其直接传递给 `PivotTable.PageFields.add`。数据透视表和页面字段的构建方式与前面的场景完全相同；只是最终的页面区域注册被替换为了底层 API 调用。

```java
import com.aspose.cells.*;

// - 透视表和页面字段的构建方式与
//   场景1a完全相同(Fruit/Year/Amount数据,透视表位于E3,Fruit->行,
//   Amount->数据)。下面我们从BaseFields集合中获取Year PivotField,
//   并将其传递给PageFields.Add - 这是
//   AddFieldToArea的底层替代方法。其结果与
//   场景1a功能相同。

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// 表头
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// 示例数据 (9行)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// 在E3添加覆盖A1:C10的透视表
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> 行, Amount -> 数据 (Year将在下面添加到页面)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 底层方法:从BaseFields中获取现有的Year PivotField,
// 并通过PageFields.Add(PivotField)将其注册到页面区域。
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// 刷新以使新的页面字段在保存的工作簿中生效
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **单选过滤（显示一个页面项）**

在默认的单选行为模式下，页面字段呈现为单个下拉列表，`PivotField.CurrentPageItem` 整数用于选择哪个页面项驱动透视表主体。分配一个特定的索引将选中该项；分配特殊值 `0x7FFD`（十进制 32765）则清除筛选器，从而一次性汇总所有页面项。单选是默认模式，您无需显式启用它。

### 显示所有项

将 `CurrentPageItem` 设置为魔术值 `0x7FFD` 等同于清除页面筛选器：透视表主体会汇总每个页面项，就像未应用任何筛选器一样。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// 填充水果/年份/金额数据
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// 在 E3 创建数据透视表
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);

// 配置透视字段：水果到行，金额到数据，年份到页
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");

pivot.refreshData();
pivot.calculateData();

// 清除页面筛选器，以便页面字段中的每个项目都可见。
// 0x7FFD（十进制 32765）是表示"所有项目"的特殊哨兵值，
// 等同于在 Excel 的页面字段下拉菜单中选择"(全部)"。
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");
```

### 显示一个特定项

将 `CurrentPageItem` 设置为一个实际索引将仅选中该页面项。该索引是该项在页面字段已排序项列表中的位置，因此例如 `1` 表示选择排序后的第二项。

```java
import com.aspose.cells.*;

// 创建工作簿
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// 添加示例数据（水果/年份/金额）
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// 在 E3 处添加数据透视表
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// 添加字段：Fruit→行，Amount→数据，Year→页
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// 页字段特定操作
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = 排序顺序中的第二项（例如 "2021"）

// 刷新并计算数据透视表
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **多选过滤**

多选过滤将页面下拉列表转换为一个复选框列表，允许最终用户同时选择多个页面项。Aspose.Cells 提供了两个协同工作的属性。`PivotField.IsMultipleItemSelectionAllowed` 必须设置为 `true`，多选 UI 才会生效。启用该属性后，`PivotItem.IsHidden` 控制哪些项显示在复选框列表中，因此您可以显示所有项，或者仅将特定项列入白名单。

下面的代码在场景 1a 中构建的同一 Year 页面字段上启用多选，然后展示两种模式：A 部分通过对每个条目保持 `IsHidden` 为 `false` 来显示每个页面项；B 部分通过 `switch (pivotItems[i].getStringValue())` 块将您选择的源值列入白名单，并隐藏所有其他项。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// 样本数据：水果 | 年份 | 数量
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

String[][] data = new String[][]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};

for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}

Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// -- 启用页面字段上的多选
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// 部分 A -- 选择所有项目（使每个项目可见）
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}

// 部分 B -- 按源值仅选择特定项目
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **注意：** 通过 `PivotItem.IsHidden` 使用多选过滤时，**必须至少保留一个 `PivotItem` 可见**（`IsHidden == false`）。如果每个项都被隐藏，Excel 在打开文件时要么崩溃，要么渲染出一个空白的透视表。请始终确保您的多选白名单中至少包含源数据中的一个项。

## **应该使用哪个 API 和哪种模式？**

下表汇总了何时使用每个 API 和模式，以便您无需详细阅读每个场景即可选择正确的组合。

| 场景 / 用例 | 推荐 API | 使用的属性 | 备注 |
|---|---|---|---|
| 按源列名称添加页面字段（最常见） | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | 高级 API，一行代码。除非您需要 `PivotField` 引用，否则请使用此 API。 |
| 当您已有 `PivotField` 对象时添加页面字段 | `PivotTable.PageFields.add(PivotField)` | n/a | 当字段对象是从其他位置获取或需要重用时使用。 |
| 过滤到单个页面项（默认模式） | `PivotField.CurrentPageItem` | 设置为特定索引 | 例如，`1` 显示已排序列表中的第二项。 |
| 显示所有项 / 清除页面筛选器 | `PivotField.CurrentPageItem` | 设置为 `0x7FFD` | 魔术值 `0x7FFD`（十进制 32765）是"所有项"的特殊值。 |
| 在 Excel 中启用多选 UI | `PivotField.IsMultipleItemSelectionAllowed` | 设置为 `true` | 在任何 `IsHidden` 调用生效之前必需设置。 |
| 在多选列表中隐藏 / 显示单个项 | `PivotItem.IsHidden` | 按项设置 | 必须至少保留一个项可见（`IsHidden == false`）。 |

{{% alert color="primary" %}}
配置多选过滤时，请始终记住可见性约束。如果多选页面字段中的每个 `PivotItem` 都被隐藏，Excel 在打开时要么崩溃，要么渲染出一个空白的透视表。请根据源数据构建您的白名单，确保至少有一个项保持可见，这样您保存的工作簿在每台机器上都能可靠打开。
{{% /alert %}}



{{< app/cells/assistant language="java" >}}