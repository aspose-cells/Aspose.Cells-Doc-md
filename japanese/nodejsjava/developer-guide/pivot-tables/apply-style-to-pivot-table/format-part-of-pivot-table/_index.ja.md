---
title: ピボットテーブルの一部を書式設定
linktitle: ピボットテーブルの一部を書式設定
description: Aspose.Cells for Node.js via Java を使用して、PivotTable.format によりセマンティックな PivotArea 領域または CellArea 四角形にスタイルを適用し、PivotTable.getPivotFormats() に保存された書式をピボットテーブルの更新時に保持しながら、ピボットテーブルの一部を書式設定します。
keywords: Aspose.Cells for Node.js via Java, ピボットテーブル, 書式設定, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /ja/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
`PivotTable.formatAll` はピボットテーブル全体に単一のスタイルを適用し、親ページで説明されています。ラベル、値、合計、またはレポートの特定領域を区別しません。  
実際には、ピボットテーブルの一部だけを強調表示したいことが多いです。一般的な対象は、ある行フィールドに属するラベル、あるフィールドが生成する値セル、総計行、または最初の 2 行のような任意の矩形です。  
ピボットテーブルのワークシートセルに直接スタイルを適用することは同等ではありません。Excel はピボットテーブルの書式を普通のセルスタイルレコードではなく、セマンティックな `PivotArea` 領域として保存します。`PivotArea` の書式はフィールドのラベルやデータ値などの領域に結び付けられ、ピボットテーブルが再計算、更新、または拡張されると再解決されます。一方、セルに直接書き込まれたスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。  
Aspose.Cells は完全な `PivotTable.format` オーバーロード ファミリーを公開しており、両方の書式設定方法が利用可能です。
- `format(PivotArea, Style)` は `PivotArea.select` または `PivotArea.selectField` で構築されたセマンティック領域にスタイルを固定します。
- `format(CellArea, Style)` はピボットテーブル内のワークシート矩形にスタイルを固定します。
- `format(int row, int column, Style)` は単一セルを対象とします。
- `formatAll(Style)` はピボットテーブル全体をフォーマットします。

## **PivotArea を書式設定**
ハイライトがフィールドまたはレポート領域に連動する必要がある場合は、セマンティック領域のワークフローが推奨されます。
1. `new PivotArea(pivotTable)` で `PivotArea` を作成します。このオブジェクトは、特定のピボットテーブルに属するセマンティック領域を表します。
1. `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` を使用して、指定軸上のゼロベース位置でフィールドを選択します。
   - `PivotTableSelectionType.DATA_AND_LABEL` はフィールドのラベルとデータの両方を選択します。
   - `PivotTableSelectionType.LABEL_ONLY` はフィールドのラベルのみを選択します。
   - `PivotTableSelectionType.DATA_ONLY` はフィールドのデータセルのみを選択します。
1. `PivotArea.selectField(PivotFieldType axisType, string fieldName)` で名前でフィールドを選択します。行フィールドを名前で選択すると、領域はそのフィールドの項目が生成する値セルに解決されます。
1. `Workbook.createStyle()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定し、`PivotTable.format(area, style)` に渡します。
1. `PivotArea` のオーバーロードを呼び出すたびに、`PivotTable.getPivotFormats()` に `PivotTableFormat` エントリが 1 つ追加されます。
1. フィールドにアンカーされた書式はピボットデータが計算されると適用されます。したがって、書式を適用した後に `PivotTable.calculateData()` を呼び出し、スタイルを表示できるようにします。
以下の例は小規模な「果物販売」ピボットテーブルを作成し、`PivotArea.select` と `PivotTableSelectionType.LABEL_ONLY` を使用して `Fruit` 行ラベルをスタイル化し、同じ行フィールドから生成された値セルを `PivotArea.selectField` でスタイル化し、最後にピボットテーブルを再計算して両方のスタイルを描画します。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **ピボットテーブルのセル領域を書式設定**
`PivotTable.format(CellArea, Style)` は、関心領域が単なるワークシート矩形であり、セマンティックなピボット領域でない場合に使用します。  
`CellArea` は `StartRow`、`StartColumn`、`EndRow`、`EndColumn` の公開フィールドで記述されます。これらの値はゼロベースのワークシート座標であり、終了座標は矩形に含まれる最後の行と列を示すため、開始位置から終了位置までのセルが含まれます。  
フィールドにアンカーされた書式とは異なり、`CellArea` の書式は即座にセルに適用されます。スタイルを表示させるために `calculateData()` を再度呼び出す必要はありません。  
`CellArea` の矩形にはラベルセルと値セルが混在する場合があります。次のセクションでは、Aspose.Cells と Excel がその矩形を内部でどのように表現しているかを説明します。  
以下の例はピボットテーブルの矩形 `E4:F5` を斜体のライトブルー スタイルでフォーマットし、再計算なしでブックを保存します。

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
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **PivotArea と CellArea のマッピング方法**
Excel はピボットテーブルの書式を普通のワークシートセルスタイルレコードではなく `pivotArea` レコードとして保存します。Aspose.Cells でも同じモデルが使用されているため、書式要求は記録時にピボット領域に変換されます。  
ユーザーが提供する `CellArea` と内部に保存されるピボット領域との関係は多対多です。
- 1 つの `CellArea` が複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方を含む場合、ラベル書式とデータ書式が別々に分解されます。ピボットモデルはラベル書式とデータ書式を独立して扱うためです。
- 1 つのピボット領域が複数の離散した `CellArea` インスタンスに解決されることがあります。総計行や項目が連続しないフィールドなどのセマンティック領域は、複数の矩形にまたがることがあります。そのため `PivotArea.getCellAreas()` は単一の矩形ではなくコレクションを返します。  
`PivotTable.format` を通じて実行されたすべての書式操作は `PivotTable.getPivotFormats()` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を公開します。`PivotArea` のオーバーロードは呼び出しごとに 1 つのエントリを追加しますが、異なるセマンティック領域を含む `CellArea` は複数のエントリを追加することがあります。  
保存された領域を識別するために、各 `PivotArea` は `getOnlyLabel()` と `getOnlyData()` フラグを公開します。以下の例はラベルと値の両方をカバーする単一矩形をフォーマットし、`PivotTable.getPivotFormats()` を検査して、各保存されたピボット領域が解決する `CellArea` 座標を出力します。

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
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
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
書式が普通のセルスタイルではなくピボット領域として保存されているため、再計算やリフレッシュ後も残ります。ピボットテーブルを `PivotTable.refreshData()` で更新したり、`calculateData()` で再計算したり、保存後に再読み込みした場合でも、すべての保存されたピボット領域は現在の位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトをリフレッシュ後もフィールドやセマンティック領域に結び付けておきたい場合は `select` または `selectField` で構築した `PivotArea` を使用し、現在のピボットテーブル配置で固定矩形をフォーマットすればよい場合は `CellArea` を使用します。単一セルを対象にするには `format(int row, int column, Style)` オーバーロードを使用します。ピボットテーブル全体を一度に再スタイル化したい場合は、親ページで説明されている `formatAll` を使用してください。

## **Related Articles**
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)
- [ピボットテーブルの行と列フィールドの追加](/cells/ja/nodejs-java/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/nodejs-java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}