---
title: Aspose.Cells for .NET でピボットテーブルの値フィールドを管理する
description: Aspose.Cells for Node.js via C++ で、ピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.Function で集計関数を変更する方法、値フィールドを Row または Column 軸にプロットする方法を学習します。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/nodejs-cpp/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
```

Now the body content. Let me translate paragraph by paragraph:

"Value fields are the heart of every pivot table, the numeric aggregates that summarise the source data. In Aspose.Cells for Node.js via C++, the data region of a pivot table is populated by adding base fields to it through `PivotTable.addFieldToArea`, and each field placed in that region can have its own summary function. When two or more data fields exist, Aspose.Cells exposes a special aggregate field, `PivotTable.getValuesField`, that can be plotted onto the Row or Column axis as a base field, giving you finer control over how value fields appear in the layout."

Translation:
"値フィールドはすべてのピボットテーブルの中心であり、ソースデータを集計する数値集計です。Aspose.Cells for Node.js via C++ では、`PivotTable.addFieldToArea` を通じて基本フィールドを追加することでピボットテーブルのデータ領域が設定され、その領域に配置された各フィールドは独自の集計関数を持つことができます。2 つ以上のデータフィールドが存在する場合、Aspose.Cells は特別な集計フィールド `PivotTable.getValuesField` を公開し、これを基本フィールドとして Row または Column 軸にプロットでき、値フィールドがレイアウトにどのように表示されるかをより細かく制御できます。"

"## Adding a Field to the Data Region" -> "## データ領域へのフィールドの追加"

"Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data. Aspose.Cells exposes `PivotTable.addFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.Data` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.getDataFields()` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `ConsolidationFunction.Sum`, while a non-numeric column defaults to `Count`."

Translation:
"基本フィールドをデータ（値）領域に追加することは、ピボットテーブルがソースデータをどのように集計するかを形作る最初のステップです。Aspose.Cells は `PivotTable.addFieldToArea(PivotFieldType, string)` を提供しており、これは定数 `PivotFieldType.Data` とソース列名を受け取るオーバーロードです。フィールドがデータ領域に追加されると、API は `PivotTable.getDataFields()` コレクションを通じてそれを公開し、フィールドが追加された順序で並びます。デフォルトでは、数値ソース列は `ConsolidationFunction.Sum` で集計され、非数値列は `Count` がデフォルトとなります。"

"## Changing the Summary Function" -> "## 集計関数の変更"

"Every field placed in the data region is wrapped internally as a `PivotField` instance, and its `getFunction()` property returns a value from the `ConsolidationFunction` enum. The same `setFunction()` setter lets you switch between the available aggregates, including `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var`, and `Varp`."

Translation:
"データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `getFunction()` プロパティは `ConsolidationFunction` 列挙型の値を返します。同じ `setFunction()` セッターを使用すると、`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` などの利用可能な集計を切り替えることができます。"

Alert: "Changing the summary function only affects the aggregate, the source column does not change."
"集計関数の変更は集計のみに影響し、ソース列は変更されません。"

"You can therefore leave one data field as `Sum` while you add a second data field that targets the same source column but uses `Count` or `Average`, all in a single pivot."
"したがって、1 つのデータフィールドを `Sum` のままにして、同じソース列を対象とするが `Count` または `Average` を使用する 2 つ目のデータフィールドを、単一のピボットで追加することができます。"

"## Plotting Value Fields to Row or Column Axis" -> "## Row または Column 軸への値フィールドのプロット"

"When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.getValuesField`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side."
"ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.getValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これを基本ピボットフィールドとして Row または Column 領域にドラッグでき、複数のメジャーを並べてレイアウトする場合に便利です。"

Alert: "`PivotTable.getValuesField()` does not work if there is no or only one value field."
"`PivotTable.getValuesField()` は、値フィールドが存在しないか 1 つしかない場合は機能しません。"

""
"以下のシナリオでは、上記の各機能を同じピボット構造に対して実証する 3 つのエンドツーエンドの例を紹介します。"

"##— Dragging a Base Field into the Value Region" -> "## シナリオ 1 — 基本フィールドを値領域にドラッグする"

"This scenario shows how to put a single base field (`Amount`) into the data region of an existing pivot table. The shared pivot structure places `Category` and `Item` on the Row axis and `Year` on the Column axis. After the operation, `Amount` appears in the data region and is computed as the `Sum` of `Amount` by default."

Translation:
"このシナリオでは、単一の基本フィールド (`Amount`) を既存のピボットテーブルのデータ領域に配置する方法を示します。共有されるピボット構造は、`Category` と `Item` を Row 軸に配置し、`Year` を Column 軸に配置します。操作後、`Amount` はデータ領域に表示され、デフォルトで `Amount` の `Sum` として計算されます。"

"##— Changing the Summary Function" -> "## シナリオ 2 — 集計関数の変更"

""

Translation:
"このシナリオは、シナリオ 1 と同じピボット構造から始まりますが、`Amount` フィールドをデータ領域に 2 回追加します。両方のデータフィールドは同じソース列を参照しますが、2 番目のフィールドは `setFunction()` セッターを使用してオーバーライドされ、デフォルトの `Sum` の代わりに `Count` になります。"

"##— Plotting Value Fields to Row or Column Axis" -> "## シナリオ 3 — Row または Column 軸への値フィールドのプロット"

"With two data fields in place, `PivotTable.getValuesField()` becomes usable. This scenario drags that aggregate virtual field onto the Column region so that every measure in the data region appears as its own column block next to `Year`."

Translation:
"2 つのデータフィールドが配置されると、`PivotTable.getValuesField()` が使用可能になります。このシナリオでは、その集計仮想フィールドを Column 領域にドラッグし、データ領域の各メジャーが `Year` の隣に独自の列ブロックとして表示されるようにします。"

"Together, these three scenarios cover every aspect of value-field manipulation in Aspose.Cells for Node.js via C++, from a single data field with the default `Sum` to a multi-measure pivot in which the virtual `ValuesField` controls the layout on the Row or Column axis."

Translation:
"これらの 3 つのシナリオを合わせると、デフォルトの `Sum` を持つ単一のデータフィールドから、仮想 `ValuesField` が Row または Column 軸のレイアウトを制御する複数メジャーのピボットまで、Aspose.Cells for Node.js via C++ における値フィールド操作のすべての側面をカバーしています。"

"## Related Articles" -> "## 関連記事"

For the article links, I should keep them as English in the link texts but I need to translate. Actually, let me look at the rules again - the rule says we can keep English for valid exceptions. But for cleaner translation, I should translate. Let me translate the link texts.

Wait, looking at the original:
- "Pivot Table Row and Column Fields in Aspose.Cells for Node.js via C++" - This is the link text
- "Page Fields in Pivot Tables" - link text
- "Refreshing Pivot Tables in Aspose.Cells for Node.js via C++" - link text
- "Applying Styles to Pivot Tables" - link text

These should be translated. But I need to be careful about the product name doubling rule. Let me check:
"Pivot Table Row and Column Fields in Aspose.Cells for Node.js via C++" - "Aspose.Cells for Node.js via C++" appears once. Good.

So the translations:
- "Aspose.Cells for Node.js via C++ におけるピボットテーブルの行と列のフィールド"
- "ピボットテーブルのページフィールド"
- "Aspose.Cells for Node.js via C++ におけるピボットテーブルの更新"
- "ピボットテーブルへのスタイルの適用"


```
Changing the summary function only affects the aggregate, the source column does not change.
```

Translation:
```
集計関数の変更は集計のみに影響し、ソース列は変更されません。
```

OK let me finalize the document. I need to make sure I:
1. Don't double the product name
2. Keep all code/API references
3. Keep all placeholders
4. Translate everything else properly

Let me write the final output now.

Wait, I need to think about "PivotTable.addFieldToArea" - in the rules it says "Method and Property Names" should not be translated. So I keep these as-is.

For "Row" and "Column" - these could be considered labels/axis names. In the original they are sometimes capitalized (Row, Column) and sometimes lowercase (row, column). I'll keep them as they are since they are API/technical terms.

Actually, looking at the rules more carefully:
"Terminology Rules: ... row -> 行, column -> 列"

So I should translate row/column to 行/列 in Japanese text. But when they are part of API names (like `PivotFieldType.Row`, `PivotFieldType.Column`), keep as-is.

Let me re-read the text and see what's the best approach...

In the text, "Row" and "Column" are used in two ways:
1. As part of API names: `PivotFieldType.Row`, `PivotFieldType.Column`, `PivotFieldType.Data` - keep as-is
2. As axis names in Japanese: should be translated

So "Row axis" -> "Row 軸" or "行軸"
"Column axis" -> "Column 軸" or "列軸"

Hmm, looking at technical Japanese documentation, "行軸" and "列軸" would be more natural. But since "Row" and "Column" are used as labels in the pivot table, and the API uses Row/Column, I think it might be better to keep "Row" and "Column" capitalized in some places where they refer to the actual pivot table regions.

Actually, looking again, I think the cleanest approach is:
- When it's a clear axis name referring to the pivot table region, use 行/列
- When it might be ambiguous, keep as Row/Column

Let me translate consistently with 行/列 for axis terms:

"Row or Column axis" -> "行軸または列軸"
"on the Row axis" -> "行軸に"
"on the Column axis" -> "列軸に"
"Row region" -> "行領域"
"Column region" -> "列領域"

Actually, I'll use the English terms "Row" and "Column" capitalized in some places because they are explicit labels in pivot tables and might be confusing in Japanese. But for "axis" I'll use 軸.

Hmm, let me just translate naturally. In Japanese technical docs, these are often kept as "Row" and "Column" when referring to pivot table areas because of established convention. Let me keep them capitalized when they refer to specific pivot table regions/axes.

Actually, let me reconsider. The document mentions "Row or Column axis" several times. I think translating naturally is fine. Let me use:
- "Row 軸" / "Column 軸" - this is natural in Japanese technical docs
- "Row 領域" / "Column 領域" - same

Or I could use:
- "行軸" / "列軸" - more Japanese
- "行領域" / "列領域" - more Japanese

I'll go with the more Japanese versions for body text but keep Row/Column when it's part of code/API references.

Let me reconsider once more. Looking at the original text:
- "the data region of a pivot table is populated"
- "each field placed in that region"
- "plotted onto the Row or Column axis"
- "a base pivot field"
- "the Row or Column region"

In these contexts, "Row" and "Column" are clearly axis names. I'll translate them to 行 and 列 in Japanese.

OK let me finalize. Let me write the output now.

For frontmatter:
- title: The product name "Aspose.Cells for Node.js via C++" appears in the title. In Japanese, this would be "Aspose.Cells for Node.js via C++ の値フィールド" or "Aspose.Cells for Node.js via C++ における値フィールド". Let me use the simpler form.

- description: needs to be in Japanese, no colons
- keywords: Translate to Japanese but keep product names

Let me write the final document now.

Wait, I also need to check - the assistant shortcode at the end:
``

This should be kept as-is.

OK let me write it.

One more consideration - for `Amount`, `Category`, `Item`, `Year` - these are column/data names in the examples. They are mentioned in body text. Should I translate them? Looking at the context, these are field names in the example data. I think it's clearer to keep them as English since they represent actual field names in the example. But the placeholder text for the code blocks mentions them in English already. Let me keep them in English in the body text too for consistency.

Actually, looking at the text:
"places `Category` and `Item` on the Row axis and `Year` on the Column axis"

These are code-style backticked field names. I'll keep them as-is.

For "Apple", "Banana", "Carrot", "Daikon", "Fruit", "Vegetable", "2020", "2021", "100", "150", etc. - these are data values in the examples. Keep in English.

OK, time to write the final output.

Let me also double-check the placeholder count:
- Input has 3 CODE_BLOCK placeholders
- Output should have 3

Let me count in my translation:
- Scenario 1: 1 placeholder
- Scenario 2: 1 placeholder
- Scenario 3: 1 placeholder

Total: 3 placeholders. 

Now let me write the final translated document.
</think>

値フィールドはすべてのピボットテーブルの中心であり、ソースデータを集計する数値の集計値です。Aspose.Cells for Node.js via C++ では、`PivotTable.addFieldToArea` を通じて基本フィールドを追加することでピボットテーブルのデータ領域が設定され、その領域に配置された各フィールドは独自の集計関数を持つことができます。2 つ以上のデータフィールドが存在する場合、Aspose.Cells は特別な集計フィールド `PivotTable.getValuesField` を公開し、これを基本フィールドとして行または列の軸にプロットでき、レイアウト上での値フィールドの表示方法をより細かく制御できます。

## データ領域へのフィールドの追加

基本フィールドをデータ（値）領域に追加することは、ピボットテーブルがソースデータをどのように集計するかを形作る最初のステップです。Aspose.Cells は `PivotTable.addFieldToArea(PivotFieldType, string)` を提供しており、これは定数 `PivotFieldType.Data` とソース列名を受け取るオーバーロードです。フィールドがデータ領域に追加されると、API は `PivotTable.getDataFields()` コレクションを通じてそれを公開し、フィールドが追加された順序で並びます。デフォルトでは、数値ソース列は `ConsolidationFunction.Sum` で集計され、非数値列は `Count` がデフォルトとなります。

## 集計関数の変更

データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `getFunction()` プロパティは `ConsolidationFunction` 列挙型の値を返します。同じ `setFunction()` セッターを使用すると、`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` などの利用可能な集計を切り替えることができます。

集計関数の変更は集計結果のみに影響し、ソース列は変更されません。
{{% /alert %}}

したがって、1 つのデータフィールドを `Sum` のままにして、同じソース列を対象とするが `Count` または `Average` を使用する 2 つ目のデータフィールドを、単一のピボット内で追加することができます。

## 値フィールドを行または列の軸にプロットする

ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.getValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これを基本ピボットフィールドとして行領域または列領域にドラッグでき、複数のメジャーを並べて配置する場合に便利です。

`PivotTable.getValuesField()` は、値フィールドが存在しないか 1 つしかない場合は機能しません。

以下のシナリオでは、上記で説明した各機能を同じピボット構造に対して実証する 3 つのエンドツーエンドの例を順に紹介します。

## シナリオ 1 — 基本フィールドを値領域にドラッグする

このシナリオでは、単一の基本フィールド (`Amount`) を既存のピボットテーブルのデータ領域に配置する方法を示します。共有されるピボット構造は、`Category` と `Item` を行軸に配置し、`Year` を列軸に配置します。操作の後、`Amount` はデータ領域に表示され、デフォルトで `Amount` の `Sum` として計算されます。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 のヘッダー
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// A2:D9 のデータ行（j で分岐するネストされたループを使用）
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

// F3 に PivotTable1 という名前のピボットテーブルを追加
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットレイアウト: 行に Category と Item、列に Year、データフィールドに Amount
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");javascript
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

workbook.save("output_function.xlsx");javascript
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

これらの 3 つのシナリオを合わせると、デフォルトの `Sum` を持つ単一のデータフィールドから、仮想 `ValuesField` が行軸または列軸のレイアウトを制御する複数メジャーのピボットまで、Aspose.Cells for Node.js via C++ における値フィールド操作のすべての側面をカバーしています。

## 関連記事

- [Aspose.Cells for Node.js via C++ におけるピボットテーブルの行と列のフィールド](/cells/ja/nodejs-cpp/row-and-column-fields/)
- [ピボットテーブルのページフィールド](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++ におけるピボットテーブルの更新](/cells/ja/nodejs-cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}
