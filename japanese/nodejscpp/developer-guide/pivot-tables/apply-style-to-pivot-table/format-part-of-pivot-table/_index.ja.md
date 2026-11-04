---
title: ピボットテーブルの一部のフォーマット
linktitle: ピボットテーブルの一部のフォーマット
description: Aspose.Cells for Node.js via C++ で、PivotTable.format を使用してセマンティックな PivotArea 領域または CellArea 矩形にスタイルを適用し、フォーマットは PivotTable.getPivotFormats() に保存され、ピボットテーブルが更新されても保持されます。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, フォーマット, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /ja/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
`PivotTable.formatAll` はピボットテーブル全体に単一のスタイルを適用します（親ページで説明しています）。ラベル、値、合計、またはレポートの特定領域を区別しません。  
実際には、ピボットテーブルの一部だけを目立たせることが多いです。一般的な対象としては、ある行フィールドに属するラベル、あるフィールドが生成する値セル、総計行、または最初の2行のような任意の矩形があります。  
ピボットテーブルのワークシートセルに直接スタイルを適用しても同等ではありません。Excel はピボットテーブルの書式設定を、通常のセルスタイルレコードではなくセマンティックな `PivotArea` 領域として保存します。`PivotArea` の書式はフィールドのラベルやデータ値などの領域に付随したままで、ピボットテーブルが再計算、更新、または展開されると再解決されます。一方、セルに直接書き込まれたスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。  
Aspose.Cells は、両方のタイプの書式設定が利用できるように、完全な `PivotTable.format` オーバーロードファミリーを提供します。  
- `format(PivotArea, Style)` は、`PivotArea.select` または `PivotArea.selectField` で構築されたセマンティック領域にスタイルを固定します。  
- `format(CellArea, Style)` は、ピボットテーブル内のワークシート矩形にスタイルを固定します。  
- `format(number row, number column, Style)` は、単一のセルを対象とします。  
- `formatAll(Style)` は、ピボットテーブル全体をフォーマットします。

## **ピボット領域をフォーマットする**
レポートのフィールドまたは領域にハイライトを追従させる必要がある場合、セマンティック領域のワークフローが推奨されます。  
1. `new PivotArea(pivotTable)` で `PivotArea` を作成します。このオブジェクトは、特定のピボットテーブルに属するセマンティック領域を表します。  
2. `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)` を使用して、指定軸上のゼロベース位置でフィールドを選択します。  
   - `PivotTableSelectionType.DataAndLabel` は、フィールドのラベルとデータの両方を選択します。  
   - `PivotTableSelectionType.LabelOnly` は、フィールドのラベルのみを選択します。  
   - `PivotTableSelectionType.DataOnly` は、フィールドのデータセルのみを選択します。  
3. `PivotArea.selectField(PivotFieldType axisType, string fieldName)` でフィールド名で選択します。行フィールドを名前で選択すると、その領域はフィールドの項目が生成する値セルに解決されます。  
4. `workbook.createStyle()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定して、`pivotTable.format(area, style)` に渡します。  
5. `PivotArea` のオーバーロードを呼び出すたびに、`pivotTable.getPivotFormats()` に `PivotTableFormat` エントリが 1 件追加されます。  
6. フィールドに固定された書式は、ピボットデータが計算されたときに適用されます。そのため、書式を適用した後に `pivotTable.calculateData()` を呼び出し、スタイルが表示されるようにします。  
以下の例は、小規模なフルーツ販売ピボットテーブルを作成し、`PivotArea.select` と `PivotTableSelectionType.LabelOnly` を使用して `Fruit` 行ラベルにスタイルを適用し、同じ行フィールドが生成する値セルに対して `PivotArea.selectField` でスタイルを適用し、最後にピボットテーブルを再計算して両方のスタイルを描画します。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
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
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **ピボットテーブルのセル領域をフォーマットする**
対象領域がセマンティックなピボット領域ではなく、単純なワークシート矩形である場合は、`PivotTable.format(CellArea, Style)` を使用します。  
`CellArea` は `startRow`、`startColumn`、`endRow`、`endColumn` プロパティで記述されます。これらの値はゼロベースのワークシート座標で、終了座標は矩形に含まれる最終行と最終列を示すため、領域は開始位置から終了位置までのセルを含みます。  
フィールドに固定された書式とは異なり、`CellArea` の書式は即座にセルに適用されます。スタイルが表示されるように `pivotTable.calculateData()` を再度呼び出す必要はありません。  
`CellArea` 矩形はラベルセルと値セルを同時に含むことがあります。次のセクションでは、Aspose.Cells と Excel がその矩形を内部的にどのように表現しているかを説明します。  
以下の例は、ピボットテーブルの矩形 `E4:F5` に斜体で薄青色のスタイルを適用し、追加の再計算なしでワークブックを保存します。

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
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **PivotArea と CellArea のマッピング**
Excel はピボットテーブルの書式設定を、通常のワークシートセルスタイルレコードではなく `pivotArea` レコードとして保存します。同様のモデルが Aspose.Cells でも使用されており、書式設定要求は記録時にピボット領域に変換されます。  
ユーザーが提供した `CellArea` と内部で保存されるピボット領域との関係は、双方向に多対多です。  
- 1つの `CellArea` が複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方にまたがる場合、ピボットモデルはラベル書式とデータ書式を独立して扱うため、別々のラベルルールとデータルールに分解されます。  
- 1つのピボット領域が、いくつかの非連続 `CellArea` インスタンスに解決されることがあります。総計行などのセマンティック領域や、項目が連続していないフィールドは複数の矩形にまたがります。これが、`PivotArea.getCellAreas()` が単一の矩形ではなくコレクションを返す理由です。  
`pivotTable.format()` で実行されたすべての書式操作は `pivotTable.getPivotFormats()` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を示します。`PivotArea` のオーバーロードは呼び出しごとにちょうど1つのエントリを追加しますが、異なるセマンティック領域を含む `CellArea` は複数のエントリを追加することがあります。  
保存された領域を区別するために、各 `PivotArea` は `getOnlyLabel()` と `getOnlyData()` フラグを公開しています。以下の例では、ラベルと値の両方をカバーする単一の矩形をフォーマットし、`pivotTable.getPivotFormats()` を調べ、各保存されたピボット領域が解決する `CellArea` の座標を出力します。

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
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
書式が通常のセルスタイルではなくピボット領域として保存されているため、再計算や更新を経ても維持されます。`pivotTable.refreshData()` でピボットテーブルを更新したり、`pivotTable.calculateData()` で再計算したり、保存して再読み込みしたりすると、保存されたすべてのピボット領域が現在の領域位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

`select` や `selectField` で構築した `PivotArea` を使用すると、ハイライトがリフレッシュ間でフィールドやセマンティック領域に固定されたままになります。現在のピボットテーブルレイアウトで固定矩形をフォーマットするだけでよい場合は `CellArea` を使用します。単一セル向けの `format(number row, number column, Style)` オーバーロードは個別のセルを対象とします。ピボットテーブル全体を一度に再スタイル化したい場合は、親ページで説明されている `formatAll` を使用してください。

## **関連記事**
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/nodejs-cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}