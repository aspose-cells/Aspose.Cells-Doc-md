---
title: ピボットテーブルに条件付き書式を追加する
linktitle: ピボットテーブルに条件付き書式を追加する
description: Aspose.Cells for Node.js via C++ でピボットテーブルに条件付き書式を追加します。applyTo と PivotConditionFormatScopeType スコープを使用してデータ領域にルールをアンカーするか、addCellArea と pivotAreas で対象を定義し、formatConditions.addCondition でルールとスタイルを添付します。
keywords: Aspose.Cells for Node.js via C++, ピボットテーブル, 条件付き書式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /ja/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定使用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度塗りつぶされ、値が何であってもそのスタイルを保持します。条件付き書式はルール駆動の対照であり、200 を超えるすべての金額をハイライトしたり、中央値の 50％ をシェードしたり、下位ランクの項目にフラグを付けたりします。ハイライトはピボットテーブルが再計算またはリフレッシュされるたびに値に追随します。
**Aspose.Cells** において、ピボットテーブルの条件付き書式は `pivotTable.getConditionalFormats()` コレクションに格納されます。各エントリは `PivotConditionalFormat` で、次の 2 つの質問に独立して答えます：
- **ルールはどこに適用されますか？** 対象領域は `applyTo(row, column, scope)` で定義でき、Excel ユーザーインターフェイスのスコープピッカーに対応します。または `addCellArea(cellArea)` と `pivotConditionalFormat.getPivotAreas()` コレクションを使用して明示的に領域を指定します。
- **ルールは何をテストしますか？** 条件は `pivotConditionalFormat.getFormatConditions()` で取得した `formatConditions` に追加されます。`formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` を使用し、各条件は `getStyle()` で取得できるスタイルを持ちます。

{{% alert color="primary" %}}
`pivotConditionalFormat` の `formatConditions` オブジェクトに対して `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` や `formatConditions.addArea(cellArea)` を呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されており、ピボットテーブルでは機能しません。セル領域はピボット領域に変換されず、リクエストは無視されます。常に `pivotConditionalFormat` オブジェクト自体で領域を定義（`applyTo`、`addCellArea`、または `getPivotAreas()`）し、`addCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用してルールを適用する（Excel UI の方法）**
最初の方法は、Excel のユーザーインターフェイスと同様にルールを配置します。ピボットテーブルのセルはゼロベースのワークシート座標で指定され、`PivotConditionFormatScopeType` スコープは Aspose.Cells に対してそのセルからルールがどれだけの範囲に及ぶかを指示します：
- `PivotConditionFormatScopeType.DATA` - ピボットテーブルが生成するすべての値セル（総計を含む）。
- `PivotConditionFormatScopeType.FIELD` - セルが識別するフィールドに属する値セル（総計は除外）。セルは行フィールドラベルなどのフィールドセルである必要があり、値セルを渡すと例外がスローされます。
- `PivotConditionFormatScopeType.SELECTION` - セルが選択する交差点の値セルのみ（通常は単一の値セル）。
以下の例では、左上隅が E3 の果物売上ピボットテーブルを作成し、セル F4（行 3、列 5）に `DATA` スコープで条件付き書式をアンカーし、200 を超えるすべての金額を赤背景に白太字でハイライトします。Apple が 220、Banana が 330、Cherry が 200、総計が 750 の場合、ルールは F4、F5、F7 を塗りつぶします。解決された領域はデータ列全体の F4:F7 で、条件を満たすセルだけがハイライトされます。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

`FIELD` スコープで同じルールを行フィールドラベル E4（行 3、列 4）にアンカーすると、対象は F4:F6 になります。これは総計行を除いた同じデータ列です。スコープが全体の値領域ではなく `Fruit` フィールドを指すためです。`SELECTION` スコープで F4 にアンカーした場合、対象は F4 のみになります。

## **領域を手動で定義する**
2 番目の方法はスコープピッカーを省略し、`PivotConditionalFormat` 上で領域を明示的に指定します。

### **addCellArea を使用したワークシート矩形**
`addCellArea(cellArea)` は、指定された矩形をルールの対象として記録します。座標はゼロベースのワークシート座標で、領域は提供された矩形そのものです。データ列への拡張や総計ロジックはありません。対象セルが現在のピボットレイアウトの既知の固定矩形である場合に使用します。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **getPivotAreas を使用した意味的ピボット領域**
`pivotConditionalFormat.getPivotAreas()` は、兄弟ページが静的スタイルに使用しているのと同じ意味的領域モデルです。`PivotArea` を作成し、`select` または `selectField` でフィールドや領域を選択し、`pivotAreas.addPivotArea(pivotArea)` で追加します。意味的領域はフィールドに結び付いたままになるため、ピボットテーブルがリフレッシュされレイアウトが変わっても条件付き書式はフィールドに追随します。`pivotAreas.add(pivotArea)` のオーバーロードはまだコンパイルできますが、非推奨とされているので `addPivotArea` を使用してください。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **ルールの保存場所とリロード後の存続方法**
`conditionalFormats.add()` の呼び出しごとに、ピボットテーブルに 1 つの `PivotConditionalFormat` が追加されます。条件、数式、スタイルはワークブックに保存されます。以下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式が保持されたまま表示され、`getCellAreas()` は同じ領域を報告します。条件が設定されていないエントリは、ワークブック保存時に削除されます。これは、Excel がルールのない条件付き書式を破棄するのと同様です。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **関連項目**
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルの一部をフォーマットする](/cells/ja/nodejs-cpp/format-part-of-pivot-table/)
- [ピボットテーブルで上位10件の表示またはフィルタリング](/cells/ja/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値でピボットテーブルをフィルタリングする](/cells/ja/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}