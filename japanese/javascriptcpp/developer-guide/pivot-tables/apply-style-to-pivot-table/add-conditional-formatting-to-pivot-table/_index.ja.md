---
title: ピボットテーブルに条件付き書式を追加する
linktitle: ピボットテーブルに条件付き書式を追加する
description: Aspose.Cells for JavaScript via C++ でピボットテーブルに条件付き書式を追加します。applyTo と PivotConditionFormatScopeType のスコープでデータ領域にルールを固定するか、addCellArea と pivotAreas で対象を定義し、formatConditions.addCondition を使用してルールとスタイルを適用します。
keywords: Aspose.Cells for JavaScript via C++, ピボットテーブル, 条件付き書式, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /ja/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定される利用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度塗りつぶされ、その後の値の変化に関係なくスタイルが保持されます。条件付き書式はルール駆動の対応物であり、200 を超える金額をハイライトしたり、中央値の 50％をシェードしたり、下位ランクの項目にフラグを付けたりします。ピボットテーブルが再計算またはリフレッシュされるたびにハイライトが値に追随します。  
Aspose.Cells では、ピボットテーブルの条件付き書式は `pivotTable.conditionalFormats` コレクションに格納されます。各エントリは `PivotConditionalFormat` で、以下の 2 つの質問に独立して答えます。
- **ルールはどこに適用されるか？** 対象領域は、Excel のユーザーインターフェイスのスコープセレクタに相当する `applyTo(row, column, scope)` または、`addCellArea(cellArea)` と `pivotAreas` コレクションを使用して明示的に領域を指定します。
- **ルールは何をテストするか？** `formatConditions` に `addCondition(type, operatorType, formula1, formula2)` で 1 つ以上の条件を追加し、各条件は独自の `style` を保持します。

{{% alert color="primary" %}}
`formatConditions.add(cellArea, type, operatorType, formula1, formula2)` または `formatConditions.addArea(cellArea)` をピボット条件付き書式の `formatConditions` オブジェクトで呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されており、ピボットテーブルでは機能しません。セル領域はピボット領域に変換されず、リクエストは黙って無視されます。必ず `PivotConditionalFormat` 自体（`applyTo`、`addCellArea`、または `pivotAreas`）で領域を定義し、`addCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープを使用してルールを適用する（Excel UI の方法）**
最初の方法は、Excel ユーザーインターフェイスが行うようにルールを配置します。ピボットテーブルのセルは、0 ベースのワークシート座標で名前付けされ、`PivotConditionFormatScopeType` スコープが Aspose.Cells に対してそのセルからルールがどこまで及ぶかを指示します。
- `PivotConditionFormatScopeType.Data` – ピボットテーブルが生成するすべての値セル（総計を含む）。
- `PivotConditionFormatScopeType.Field` – セルが示すフィールドに属する値セル（総計を除く）。セルは行フィールドラベルなどのフィールドセルである必要があり、値セルを渡すと例外がスローされます。
- `PivotConditionFormatScopeType.Selection` – セルが選択する交差点の値セルのみ、通常は単一の値セルです。
以下の例は、左上隅が E3 にあるフルーツ売上ピボットテーブルを作成し、`Data` スコープでセル F4（行 3、列 5）に条件付き書式を固定し、200 を超える金額を赤背景に白太字でハイライトします。Apple が 220、Banana が 330、Cherry が 200、合計が 750 の場合、ルールは F4、F5、F7 に適用されます。解決された領域はデータ列全体の F4:F7 で、条件を満たすセルだけが強調表示されます。

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Anchor the conditional format at F4 (row 3, column 5) with the Data scope
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Rule - highlight amounts greater than 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) returns the file as bytes
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

同じルールを行フィールドラベル E4（行 3、列 4）に `Field` スコープで固定すると、対象は F4:F6 となります。これは総計行を除いた同じデータ列です。`Selection` スコープで F4 に固定すると、対象は F4 のみです。

## **領域を手動で定義する**
スコープセレクタを省略し、`PivotConditionalFormat` 上で領域を明示的に指定します。

### **addCellArea を使用したワークシート矩形**
`addCellArea(cellArea)` は、指定した矩形をルールの対象として記録します。座標は 0 ベースのワークシート座標で、領域は提供された矩形そのものです。データ列への拡張や総計ロジックは行われません。現在のピボットレイアウトで対象セルが既知の固定矩形である場合に使用します。

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Target the rectangle F4:F6 (the value cells without the grand total)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Rule - italic on light yellow for amounts between 150 and 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **pivotAreas を使用したセマンティックなピボット領域**
`pivotAreas` は、兄弟ページで静的スタイルに使用されているのと同じセマンティック領域モデルです。`PivotArea` を作成し、`select` または `selectField` でフィールドまたは領域を選択し、`pivotAreas.addPivotArea(pivotArea)` で追加します。セマンティック領域はフィールドに結び付けられるため、ピボットテーブルがリフレッシュされレイアウトが変わっても条件付き書式はフィールドに追随します。`pivotAreas.add(pivotArea)` のオーバーロードも動作しますが、非推奨とされているため `addPivotArea` の使用を推奨します。

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Attach the rule to the Amount data field as a semantic region
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Rule - grey text for amounts below 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **ルールはどこに保存され、再読み込み時にどう保持されるか**
各 `conditionalFormats.add()` 呼び出しは、ピボットテーブルに 1 つの `PivotConditionalFormat` を追加します。条件、数式、スタイルはワークブックに保存されます。最初の例で保存されたファイルを Node で再び開くと、タイプ、演算子、数式がそのまま保持された同じルールが表示され、`getCellAreas()` は同じ領域を報告します。このプラットフォームでは、条件の `type` と `operator` プロパティは数値の列挙値として表れます。条件がまったく設定されていないエントリは、ワークブック保存時に削除されます。これは Excel がルールのない条件付き書式を破棄するのと同様です。

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Reload the file written by the first example
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // This prints:
    // Conditional formats: 1
    // Format 0: 1 2 formula1==200   (type 1 = CellValue, operator 2 = GreaterThan)
    //     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
    process.exit(0);
});
```

## **関連項目**
- [ピボットテーブルにスタイルを適用する](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルの一部をフォーマットする](/cells/ja/javascript-cpp/format-part-of-pivot-table/)
- [ピボットテーブルで上位10件を表示またはフィルタリングする](/cells/ja/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値でピボットテーブルをフィルタリングする](/cells/ja/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}