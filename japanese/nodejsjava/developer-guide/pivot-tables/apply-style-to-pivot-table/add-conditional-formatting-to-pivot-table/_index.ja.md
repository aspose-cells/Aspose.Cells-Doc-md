---
title: ピボットテーブルに条件付き書式を追加する
linktitle: ピボットテーブルに条件付き書式を追加する
description: Aspose.Cells for Node.js via Java でピボットテーブルに条件付き書式を追加します。applyTo と PivotConditionFormatScopeType スコープでデータ領域にルールをアンカーするか、addCellArea と getPivotAreas で対象を定義し、getFormatConditions().addCondition を通じてルールとスタイルを付与します。
keywords: Aspose.Cells, ピボットテーブル, 条件付き書式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /ja/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度適用され、その後の値に関係なくスタイルが保持されます。条件付き書式はルール駆動の対応物であり、200 を超える金額をハイライトしたり、中央値の 50% を色付けしたり、下位ランクの項目にフラグを付けたりできます。ハイライトはピボットテーブルが再計算または更新されるたびに値に合わせて変化します。  
Aspose.Cells for Node.js via Java では、ピボットテーブルの条件付き書式は `pivotTable.getConditionalFormats()` コレクションに格納されます。各エントリは `PivotConditionalFormat` であり、次の 2 つの質問に独立して答えます。
- **ルールはどこに適用されますか？** 対象領域は `applyTo(int row, int column, PivotConditionFormatScopeType scope)` で定義でき、これは Excel ユーザーインターフェイスのスコープ選択と同等です。または `addCellArea(CellArea)` と `getPivotAreas()` コレクションを使用して領域を明示的に指定します。
- **ルールは何をテストしますか？** `getFormatConditions()` に対して `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` を使用して 1 つ以上の条件を追加し、各条件は独自の `getStyle()` を持ちます。

{{% alert color="primary" %}}
`getFormatConditions()` オブジェクトの `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` または `FormatConditionCollection.addArea(CellArea)` を呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されたもので、ピボットテーブルには機能しません。セル領域はピボット領域に変換されず、リクエストは無視されます。必ず `PivotConditionalFormat` 自体（`applyTo`、`addCellArea`、または `getPivotAreas()`）で領域を定義し、`addCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用したルールの適用（Excel UI の方法）**
最初の方法は、Excel ユーザーインターフェイスが行うようにルールを配置します。ピボットテーブルのセルはゼロベースのワークシート座標で名前付けされ、`PivotConditionFormatScopeType` スコープが Aspose.Cells に対して、そのセルからルールがどこまで及ぶかを指示します。
- `PivotConditionFormatScopeType.DATA` – ピボットテーブルが生成するすべての値セル（総計を含む）。
- `PivotConditionFormatScopeType.FIELD` – セルが識別するフィールドに属する値セル（総計を除く）。セルは行フィールドラベルなどのフィールドセルである必要があり、値セルを指定すると例外がスローされます。
- `PivotConditionFormatScopeType.SELECTION` – セルが選択する交差点の値セルのみ、通常は単一の値セルです。
以下の例は、左上隅が E3 のフルーツ売上ピボットテーブルを作成し、`DATA` スコープでセル F4（行 3、列 5）に条件付き書式をアンカーし、200 を超える金額を赤背景に白文字で太字にハイライトします。Apple が 220、Banana が 330、Cherry が 200、合計が 750 の場合、ルールは F4、F5、F7 をハイライトします。解決された領域はデータ列全体の F4:F7 であり、条件を満たすセルだけがハイライトされます。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

同じルールを行フィールドラベル E4（行 3、列 4）に `FIELD` スコープでアンカーすると、対象は F4:F6 となります。これは総計行を除いた同じデータ列です。`SELECTION` スコープで F4 にアンカーすると、対象は F4 のみになります。

## **領域を手動で定義する**
2 番目の方法はスコープ選択を省略し、`PivotConditionalFormat` 上で領域を明示的に指定します。

### **addCellArea でワークシートの矩形を指定**
`addCellArea(CellArea)` は、指定された矩形をルールの対象として記録します。座標はゼロベースのワークシート座標であり、領域は提供された矩形そのものです。データ列への拡張や総計ロジックは行われません。現在のピボットレイアウトで興味のあるセルが既知の固定矩形である場合に使用します。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **PivotAreas で意味的なピボット領域を指定**
`getPivotAreas()` は、兄弟ページが静的スタイルに使用しているのと同じ意味的領域モデルです。`PivotArea` を作成し、`select` または `selectField` でフィールドまたは領域を選択し、`getPivotAreas().addPivotArea(PivotArea)` で追加します。意味的領域はフィールドに結び付けられるため、ピボットテーブルが更新されレイアウトが変わっても条件付き書式はフィールドに追従します。`getPivotAreas().add(PivotArea)` のオーバーロードもコンパイルは通りますが、非推奨とされているため `addPivotArea` を使用してください。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **ルールの保存場所と再読込時の持続性**
`getConditionalFormats()` に対する各 `add()` 呼び出しは、ピボットテーブルに `PivotConditionalFormat` を 1 つ追加します。条件、数式、スタイルはワークブックに保存され、以下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式が保持された状態で表示され、`getCellAreas()` は同じ領域を報告します。条件が全く設定されていないエントリは、ワークブックを保存したときに削除されます。これは Excel がルールのない条件付き書式を破棄するのと同様です。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **関連記事**
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)
- [ピボットテーブルの一部をフォーマット](/cells/ja/nodejs-java/format-part-of-pivot-table/)
- [ピボットテーブルの上位10件の表示またはフィルタ](/cells/ja/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}