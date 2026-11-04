---
title: ピボットテーブルの一部をフォーマットする
linktitle: ピボットテーブルの一部をフォーマットする
description: Aspose.Cells for JavaScript via C++ でピボットテーブルの一部を、PivotTable.Format を使用して意味的な PivotArea 領域または CellArea 四角形にスタイルを適用し、PivotTable.PivotFormats に保存されたフォーマットはピボットテーブルの更新時にも保持されます。
keywords: Aspose.Cells for JavaScript via C++, ピボットテーブル, フォーマット, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /ja/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
`PivotTable.FormatAll` はピボットテーブル全体に単一のスタイルを適用します（親ページで説明済み）。ラベル、値、合計、またはレポートの特定領域を区別しません。実務では、ピボットテーブルの一部だけを目立たせることが一般的です。対象としてよくあるのは、ある行フィールドに属するラベル、あるフィールドが生成した値セル、総計行、または先頭の 2 行のアイテムなどの任意の矩形です。
ピボットテーブルのワークシート上のセルに直接スタイルを適用しても同等ではありません。Excel はピボットテーブルの書式設定を普通のセルスタイルレコードではなく、意味的な `PivotArea` 領域として保存します。`PivotArea` の書式はフィールドのラベルやデータ値などの領域に結び付けられ、ピボットテーブルが再計算、更新、または展開されると再解決されます。一方、セルに直接書き込んだスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。
Aspose.Cells は完全な `PivotTable.Format` オーバーロードファミリーを公開しており、両方の書式設定が利用可能です。
- `Format(PivotArea, Style)` は `PivotArea.Select` または `PivotArea.SelectField` で構築した意味的領域にスタイルを結び付けます。
- `Format(CellArea, Style)` はピボットテーブル内のワークシート矩形にスタイルを結び付けます。
- `Format(int row, int column, Style)` は単一セルを対象とします。
- `FormatAll(Style)` はピボットテーブル全体をフォーマットします。

## **Pivot Area のフォーマット**
意味的領域ワークフローは、ハイライトがフィールドまたはレポートの領域に追従する必要がある場合に推奨されます。
1. `new PivotArea(pivotTable)` で `PivotArea` を作成します。このオブジェクトは対象のピボットテーブルに属する意味的領域を表します。
1. `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` を使用して、指定軸上のゼロベース位置でフィールドを選択します。
   - `PivotTableSelectionType.DataAndLabel` はラベルとデータの両方を選択します。
   - `PivotTableSelectionType.LabelOnly` はフィールドのラベルのみを選択します。
   - `PivotTableSelectionType.DataOnly` はフィールドのデータセルのみを選択します。
1. `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` で名前でフィールドを選択します。行フィールドを名前で選択した場合、領域はそのフィールドのアイテムが生成する値セルに解決されます。
1. `Workbook.CreateStyle()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定し、`PivotTable.Format(area, style)` に渡します。
1. `PivotArea` のオーバーロード呼び出しは、`PivotTable.PivotFormats` に `PivotTableFormat` エントリを 1 つ追加します。
1. フィールドに結び付けられた書式はピボットデータの計算時に描画されます。したがって、書式を適用した後に `PivotTable.CalculateData()` を呼び出し、スタイルが表示されるようにします。
以下の例は、小規模なフルーツ販売ピボットテーブルを作成し、`Fruit` 行ラベルを `PivotArea.Select` と `PivotTableSelectionType.LabelOnly` でスタイル付けし、同じ行フィールドが生成する値セルを `PivotArea.SelectField` でスタイル付けし、最後にピボットテーブルを再計算して両方のスタイルを描画します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **ピボットテーブルのセル領域のフォーマット**
関心領域が意味的なピボット領域ではなく単純なワークシート矩形である場合は、`PivotTable.Format(CellArea, Style)` を使用します。`CellArea` は `startRow`, `startColumn`, `endRow`, `endColumn` フィールドで記述され、値はゼロベースのワークシート座標です。終了座標は矩形に含まれる最終行・最終列を示すため、開始位置から終了位置までのセルすべてが対象となります。
フィールドに結び付けられた書式とは異なり、`CellArea` の書式は直ちにセルに適用されます。スタイルを表示させるために `CalculateData()` を再度呼び出す必要はありません。
`CellArea` 矩形にはラベルセルと値セルが混在することがあります。次のセクションでは、Aspose.Cells と Excel がその矩形を内部でどのように表現しているかを説明します。
以下の例は、ピボットテーブルの矩形 `E4:F5` にイタリック体・薄い青色のスタイルを適用し、再計算なしでワークブックを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Pivot Area と Cell Area のマッピング**
Excel はピボットテーブルの書式を普通のワークシートセルスタイルレコードではなく `pivotArea` レコードとして保存します。Aspose.Cells も同じモデルを使用しているため、書式要求は記録時にピボット領域に変換されます。
ユーザーが提供する `CellArea` と内部に保存されるピボット領域との関係は、多対多の双方向です。
- 1 つの `CellArea` が複数のピボット領域を生成することがあります。矩形がラベルセルと値セルの両方を含む場合、ラベル用とデータ用に別々の規則に分割されます。ピボットモデルはラベル書式とデータ書式を独立して扱うためです。
- 1 つのピボット領域が複数の分離した `CellArea` インスタンスに解決されることがあります。総計行や項目が連続していないフィールドなど、意味的領域は複数の矩形に跨ることがあります。そのため `PivotArea.GetCellAreas()` は単一の矩形ではなくコレクションを返します。
`PivotTable.Format` を通じて実行されたすべての書式操作は `PivotTable.PivotFormats` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を公開します。`PivotArea` オーバーロードは呼び出しごとに正確に 1 つのエントリを追加しますが、異なる意味的領域を含む `CellArea` は複数のエントリを追加する可能性があります。
保存された領域を区別するために、各 `PivotArea` は `OnlyLabel` と `OnlyData` フラグを提供します。以下の例は、ラベルと値の両方をカバーする単一矩形をフォーマットし、`PivotTable.PivotFormats` を調査して、各保存されたピボット領域が解決する `CellArea` 座標を出力します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
書式がピボット領域として保存されているため、普通のセルスタイルとしてではなく、再計算や更新時にも保持されます。`PivotTable.RefreshData`、`CalculateData`、または保存後の再読込のいずれでピボットテーブルが更新されても、すべての保存済みピボット領域は現在の位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトをフィールドや意味的領域に結び付けて更新に耐えさせたい場合は `Select` または `SelectField` で構築した `PivotArea` を使用し、現在のピボットテーブルレイアウト内の固定矩形に対してのみ書式設定すればよい場合は `CellArea` を使用してください。単一セルを対象とする `Format(int row, int column, Style)` オーバーロードも利用できます。ピボットテーブル全体を一括で再スタイル化したい場合は、親ページで説明されている `FormatAll` を使用します。

## **関連記事**
- [ピボットテーブルへのスタイル適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/javascript-cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}