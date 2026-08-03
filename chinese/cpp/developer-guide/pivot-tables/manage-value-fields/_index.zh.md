---
title: Aspose.Cells for C++ 中的值字段
linktitle: Aspose.Cells for C++ 中的值字段
description: 了解如何在 Aspose.Cells for C++ 中将基础字段添加到数据透视表的数据区域，使用 PivotField.Function 更改汇总函数，并将值字段绘制到行轴或列轴上。
keywords: Aspose.Cells, C++, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 将字段添加到数据区域
将基础字段添加到数据（值）区域是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开了 `PivotTable.AddFieldToArea(PivotFieldType, string)` 重载，该重载接受常量 `PivotFieldType.Data` 和源列名称。字段添加到数据区域后，API 会通过 `PivotTable.DataFields` 集合公开它，按添加字段的顺序排列。默认情况下，数值型源列使用 `ConsolidationFunction.Sum` 进行汇总，而非数值型列默认使用 `Count`。
## 更改汇总函数
放置在数据区域中的每个字段在内部都被包装为 `PivotField` 实例，其 `Function` 属性返回 `ConsolidationFunction` 枚举中的值。同一个 `Function` setter 允许您在可用的聚合之间切换，包括 `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var` 和 `Varp`。
{{% alert color="primary" %}}
更改 `Function` 仅影响聚合，源列不会改变。
{{% /alert %}}
因此，您可以将一个数据字段保留为 `Sum`，同时添加第二个针对同一源列但使用 `Count` 或 `Average` 的数据字段，所有这些都在单个数据透视表中完成。
## 将值字段绘制到行轴或列轴
当数据透视表包含两个或更多数据字段时，Aspose.Cells 会公开一个额外的虚拟字段，称为 `PivotTable.ValuesField`。此虚拟字段表示数据区域中每个数据字段的聚合。您可以将其作为基础数据透视字段拖到行区域或列区域，这对于将多个度量并排排列非常有用。
{{% alert color="primary" %}}
如果没有值字段或只有一个值字段，则 `PivotTable.ValuesField` 不起作用。
{{% /alert %}}
以下场景通过三个端到端示例演示了针对同一数据透视结构上述每项功能。
## 场景 1 — 将基础字段拖入值区域
此场景演示如何将单个基础字段（`Amount`）放入现有数据透视表的数据区域。共享的数据透视结构将 `Category` 和 `Item` 放在行轴上，将 `Year` 放在列轴上。操作完成后，`Amount` 出现在数据区域中，默认按 `Amount` 的 `Sum` 进行计算。
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
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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
## 场景 2 — 更改汇总函数
此场景从与场景 1 相同的数据透视结构开始，但将 `Amount` 字段添加到数据区域两次。两个数据字段都引用同一源列，但是使用 `PivotField.Function` setter 覆盖第二个字段，使其变为 `Count` 而不是默认的 `Sum`。
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
	Workbook workbook;
	Worksheet ws = workbook.GetWorksheets().Get(0);
	ws->SetName("Data");
	Vector<String> headers{ "Category", "Item", "Year", "Amount" };
	for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

	Vector<Vector<Object*>> data;
	// 填充数据 ...
	int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
	PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
	pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
	pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
	pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
	pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
	pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
	PivotField countField = pivotTable.GetDataFields().Get(1);
	countField->SetFunction(ConsolidationFunction_Count);
	pivotTable->CalculateData();
	workbook->Save("output_function.xlsx");
}
```
## 场景 3 — 将值字段绘制到行轴或列轴
有了两个数据字段，`PivotTable.ValuesField` 就变得可用了。此场景将该聚合虚拟字段拖到列区域，以便数据区域中的每个度量都作为其自己的列块出现在 `Year` 旁边。
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 // ... 构建数据 ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType::Column, pivotTable->GetValuesField()->GetName());
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```
总之，这三个场景涵盖了 Aspose.Cells for C++ 中值字段操作的方方面面，从使用默认 `Sum` 的单个数据字段，到使用虚拟 `ValuesField` 控制行轴或列轴上布局的多度量数据透视表。

{{< app/cells/assistant language="cpp" >}}
