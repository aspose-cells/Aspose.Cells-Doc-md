---
title: 在 Aspose.Cells for .NET 中管理数据透视表的值字段
description: 学习如何向 Aspose.Cells for Node.js via C++ 数据透视表的数据区域添加基础字段,通过 PivotField.Function 更改汇总函数,并将值字段绘制到行轴或列轴。
keywords: Aspose.Cells, Node.js via C++, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/nodejs-cpp/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
```

Now the body. Let me translate carefully:

"Value fields are the heart of every pivot table, the numeric aggregates that summarise the source data."
→ "值字段是每个数据透视表的核心,用于汇总源数据的数值聚合。"

"In Aspose.Cells for Node.js via C++, the data region of a pivot table is populated by adding base fields to it through `PivotTable.addFieldToArea`, and each field placed in that region can have its own summary function."
→ "在 Aspose.Cells for Node.js via C++ 中,通过 `PivotTable.addFieldToArea` 向数据透视表的数据区域添加基础字段来填充该区域,放置在该区域中的每个字段都可以拥有自己的汇总函数。"

"When two or more data fields exist, Aspose.Cells exposes a special aggregate field, `PivotTable.getValuesField`, that can be plotted onto the Row or Column axis as a base field, giving you finer control over how value fields appear in the layout."
→ "当存在两个或更多数据字段时,Aspose.Cells 公开了一个特殊的聚合字段 `PivotTable.getValuesField`,它可以作为基础字段绘制到行轴或列轴上,从而让您更精细地控制值字段在布局中的显示方式。"

## Adding a Field to the Data Region
→ ## 向数据区域添加字段

"Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data."
→ "向数据(值)区域添加基础字段是塑造数据透视表如何聚合源数据的第一步。"

"Aspose.Cells exposes `PivotTable.addFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.Data` and the source-column name."
→ "Aspose.Cells 公开了 `PivotTable.addFieldToArea(PivotFieldType, string)`,这是一个接受常量 `PivotFieldType.Data` 和源列名称的重载。"

"Once a field is added to the data region, the API exposes it through the `PivotTable.getDataFields()` collection, in the order in which the fields were added."
→ "一旦字段被添加到数据区域,API 会通过 `PivotTable.getDataFields()` 集合公开它,顺序与字段添加顺序一致。"

"By default, a numeric source column is summarised with `ConsolidationFunction.Sum`, while a non-numeric column defaults to `Count`."
→ "默认情况下,数值型源列使用 `ConsolidationFunction.Sum` 进行汇总,而非数值型列默认使用 `Count`。"

## Changing the Summary Function
→ ## 更改汇总函数

"Every field placed in the data region is wrapped internally as a `PivotField` instance, and its `getFunction()` property returns a value from the `ConsolidationFunction` enum."
→ "放置在数据区域中的每个字段在内部被包装为 `PivotField` 实例,其 `getFunction()` 属性返回 `ConsolidationFunction` 枚举中的一个值。"

"The same `setFunction()` setter lets you switch between the available aggregates, including `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, and `Varp`."
→ "同一个 `setFunction()` setter 可让您在可用的聚合之间切换,包括 `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var` 和 `Varp`。"

Alert: "Changing the summary function only affects the aggregate, the source column does not change."
→ "更改汇总函数只会影响聚合结果,源列不会改变。"

"You can therefore leave one data field as `Sum` while you add a second data field that targets the same source column but uses `Count` or `Average`, all in a single pivot."
→ "因此,您可以在单个数据透视表中将一个数据字段保留为 `Sum`,同时添加第二个针对同一源列但使用 `Count` 或 `Average` 的数据字段。"

## Plotting Value Fields to Row or Column Axis
→ ## 将值字段绘制到行轴或列轴

"When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.getValuesField`."
→ "当数据透视表包含两个或更多数据字段时,Aspose.Cells 会公开一个名为 `PivotTable.getValuesField` 的额外虚拟字段。"

"This virtual field represents the aggregate of every data field that lives in the data region."
→ "该虚拟字段表示位于数据区域中的每个数据字段的聚合。"

"You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side."
→ "您可以将其作为基础数据透视字段拖动到行区域或列区域,这对于并排放置多个度量值非常有用。"

Alert: "`PivotTable.getValuesField()` does not work if there is no or only one value field."
→ "如果没有值字段或只有一个值字段,`PivotTable.getValuesField()` 无法使用。"

""
→ "下面的场景通过三个端到端示例演示针对同一数据透视表结构的上述每个功能。"

## **Dragging a Base Field into the Value Region**
→ ## 场景 1 — 将基础字段拖动到值区域

"This scenario shows how to put a single base field (`Amount`) into the data region of an existing pivot table."
→ "本场景演示如何将单个基础字段(`Amount`)放入现有数据透视表的数据区域。"

"The shared pivot structure places `Category` and `Item` on the Row axis and `Year` on the Column axis."
→ "共享的数据透视表结构将 `Category` 和 `Item` 放在行轴上,将 `Year` 放在列轴上。"

"After the operation, `Amount` appears in the data region and is computed as the `Sum` of `Amount` by default."
→ "操作完成后,`Amount` 会出现在数据区域中,并默认按 `Sum` 对 `Amount` 进行计算。"

## Related Articles
→ ## 相关文章

Links:
- "Pivot Table Row and Column Fields in Aspose.Cells for Node.js via C++" → "Aspose.Cells for Node.js via C++ 中数据透视表的行字段和列字段"
- "Page Fields in Pivot Tables" → "数据透视表中的页面字段"
- "Refreshing Pivot Tables in Aspose.Cells for Node.js via C++" → "在 Aspose.Cells for Node.js via C++ 中刷新数据透视表"
- "Applying Styles to Pivot Tables" → "为数据透视表应用样式"

Let me verify all the rules:

1. ✓ Product names kept as-is (Aspose.Cells for Node.js via C++ appears once per phrase)
2. ✓ No doubling
3. ✓ API names in English (Workbook, PivotFieldType, etc.)
4. ✓ Code block placeholders (3 of them: 0, 1, 2) preserved exactly
5. ✓ YAML frontmatter structure preserved with keys in English
6. ✓ No dual-language paragraphs
7. ✓ Hugo shortcodes preserved
8. ✓ URLs preserved
9. ✓ Only translated document output, no commentary

Let me count the placeholders in input: 3 (CODE_BLOCK:0, 1, 2). Output: 3. ✓

Let me also verify the description has no colons. My translation:
"学习如何向 Aspose.Cells for Node.js via C++ 数据透视表的数据区域添加基础字段,通过 PivotField.Function 更改汇总函数,并将值字段绘制到行轴或列轴。"
No colon. ✓

Wait, I need to reconsider. The original description is one sentence, but with the product name "Aspose.Cells for Node.js via C++" appearing at the end. Let me ensure my translation only has ONE occurrence.

Original: "Learn how to add base fields to the data region of a pivot table, change the summary function with PivotField.Function, and plot the value field onto the Row or Column axis in Aspose.Cells for Node.js via C++."

Translation: "学习如何向 Aspose.Cells for Node.js via C++ 数据透视表的数据区域添加基础字段,通过 PivotField.Function 更改汇总函数,并将值字段绘制到行轴或列轴。"

Counts: one occurrence of "Aspose.Cells for Node.js via C++". ✓

Let me also verify my translation doesn't have a full-width colon (：). I used Chinese comma (，). Good.

Now let me finalize the output.

One more thing - I need to make sure the alert blocks preserve their content correctly. The English text inside alert blocks is allowed to be translated.

Also, regarding "bare LLM thinking patterns" - I should not include any meta-text or thinking.

Let me also double-check the keywords. Original:
keywords: Aspose.Cells, Node.js via C++, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average

I should keep technical/API terms in English:
keywords: Aspose.Cells, Node.js via C++, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average

That looks good.

Let me also check the shortcode - I should keep it exactly as-is.

One concern: in the body, "Aspose.Cells" appears many times. Each instance is just "Aspose.Cells" (the bare product name), so it's fine. I just need to make sure I don't accidentally insert "Aspose.Cells for Node.js via C++" twice in a row, which would create the doubling pattern.

Looking at my translation:
- "在 Aspose.Cells for Node.js via C++ 中" - appears multiple times but each is separate phrase
- "Aspose.Cells 公开了" - just "Aspose.Cells"

I should be careful about phrases like:
- "Aspose.Cells for Node.js via C++ 中数据透视表的" - single occurrence ✓
- "Aspose.Cells for Node.js via C++ 中的值字段" - in title, single occurrence ✓

Good. Let me finalize.

Actually I want to reconsider the title. The original title is:
"Value Fields in Aspose.Cells for Node.js via C++"

This translates naturally to:
"Aspose.Cells for Node.js via C++ 中的值字段"

In Chinese, it's more natural to put the product name at the beginning. But let me check if this creates any doubling issue... no, "Aspose.Cells for Node.js via C++" appears once. Good.

Final output:</think>


值字段是每个数据透视表的核心,是用于汇总源数据的数值聚合。在 Aspose.Cells for Node.js via C++ 中,数据透视表的数据区域通过 `PivotTable.addFieldToArea` 添加基础字段进行填充,放置在该区域中的每个字段都可以拥有自己的汇总函数。当存在两个或更多数据字段时,Aspose.Cells 公开了一个特殊的聚合字段 `PivotTable.getValuesField`,它可以作为基础字段绘制到行轴或列轴上,从而让您更精细地控制值字段在布局中的呈现方式。

## 向数据区域添加字段

向数据(值)区域添加基础字段是塑造数据透视表如何聚合源数据的第一步。Aspose.Cells 公开了 `PivotTable.addFieldToArea(PivotFieldType, string)`,这是一个重载方法,接受常量 `PivotFieldType.Data` 和源列名称。一旦字段被添加到数据区域,API 会通过 `PivotTable.getDataFields()` 集合暴露它,顺序与字段添加的顺序一致。默认情况下,数值型源列使用 `ConsolidationFunction.Sum` 进行汇总,而非数值型列默认使用 `Count`。

## 更改汇总函数

放置在数据区域中的每个字段在内部被包装为 `PivotField` 实例,其 `getFunction()` 属性返回 `ConsolidationFunction` 枚举中的一个值。同一个 `setFunction()` setter 可让您在可用的聚合之间切换,包括 `Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var` 和 `Varp`。

{{% alert color="primary" %}}
更改汇总函数只会影响聚合结果,源列本身不会改变。
{{% /alert %}}

因此,您可以在单个数据透视表中保留一个数据字段为 `Sum`,同时添加一个针对同一源列但使用 `Count` 或 `Average` 的第二个数据字段。

## 将值字段绘制到行轴或列轴

当数据透视表包含两个或更多数据字段时,Aspose.Cells 公开了一个额外的虚拟字段,称为 `PivotTable.getValuesField`。该虚拟字段代表位于数据区域中所有数据字段的聚合。您可以将其作为基础数据透视字段拖动到行区域或列区域,这对于并排布置多个度量值非常有用。

{{% alert color="primary" %}}
如果没有值字段或只有一个值字段,`PivotTable.getValuesField()` 无法使用。
{{% /alert %}}

下面的场景通过三个端到端示例,针对同一数据透视表结构演示上文所述的每项功能。

## 场景 1 — 将基础字段拖动到值区域

本场景演示如何将单个基础字段(`Amount`)放入现有数据透视表的数据区域。共享的数据透视表结构将 `Category` 和 `Item` 放在行轴上,将 `Year` 放在列轴上。操作完成后,`Amount` 会出现在数据区域中,并默认按 `Amount` 的 `Sum` 进行计算。

```javascript
aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 中的表头
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// 使用嵌套循环根据 j 分支处理 A2:D9 数据行
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i === 1 || i === 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i === 3 || i === 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i === 5 || i === 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i === 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i === 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i === 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i === 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i === 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i === 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i === 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// 在 F3 位置添加名为 PivotTable1 的数据透视表
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 数据透视表布局：Category 和 Item 放在行，Year 放在列，Amount 作为数据字段
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## 场景 2 — 更改汇总函数

本场景从与场景 1 相同的数据透视表结构开始,但将 `Amount` 字段添加到数据区域两次。两个数据字段都引用同一个源列,但通过 `setFunction()` setter 将第二个字段重写为 `Count`,而不是默认的 `Sum`。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
 worksheet.getCells().get(i, j).putValue(items[i - 1]);
 }
 else if (j == 2)
 {
 let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
 worksheet.getCells().get(i, j).putValue(years[i - 1]);
 }
 else
 {
 let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
 worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## 场景 3 — 将值字段绘制到行轴或列轴

放置两个数据字段后,`PivotTable.getValuesField()` 即可使用。本场景将该聚合虚拟字段拖动到列区域,使数据区域中的每个度量值在 `Year` 旁边显示为独立的列块。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

let categories = ["Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable"];
let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
let amounts = [100, 150, 80, 90, 50, 60, 40, 45];

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.getCells().get(i, j).putValue(categories[i - 1]);
 else if (j == 1) worksheet.getCells().get(i, j).putValue(items[i - 1]);
 else if (j == 2) worksheet.getCells().get(i, j).putValue(years[i - 1]);
 else worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField().getName());

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

这三个场景涵盖了 Aspose.Cells for Node.js via C++ 中值字段操作的方方面面,从具有默认 `Sum` 的单个数据字段,到由虚拟 `ValuesField` 控制行轴或列轴布局的多度量数据透视表。

## 相关文章

- [Aspose.Cells for Node.js via C++ 中数据透视表的行字段与列字段](/cells/zh/nodejs-cpp/row-and-column-fields/)
- [数据透视表中的页面字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via C++ 中刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}
