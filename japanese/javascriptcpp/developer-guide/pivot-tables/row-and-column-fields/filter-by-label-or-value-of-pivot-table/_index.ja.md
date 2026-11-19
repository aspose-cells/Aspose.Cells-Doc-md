---
title: ラベルまたは値によるピボットテーブルのフィルター
linktitle: ラベルまたは値によるピボットテーブルのフィルター
description: Aspose.Cells for JavaScript via C++ は、包括的なピボットテーブルのフィルター機能をサポートします。この Playing では、ラベルフィルター、日付フィルター、値フィルター、上位 10 フィルター、およびピボット項目の非表示または表示を使用して、ピボットテーブルのデータをフィルターする方法を説明します。
keywords: Aspose.Cells, JavaScript via C++ ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位 10 フィルター, ピボット項目, ピボット項目を非表示
type: docs
weight: 10
url: /ja/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータを絞り込むための実用的な戦略を 5 つ提供します。テキストベースの行または列フィールドにはラベルフィルターを、フィールドに日時セルまたは空セルだけが含まれる場合は日付フィルターを、集計された数値には値フィルターを、値フィールドに基づいて順位付けする上位 10 フィルターを、また `isHidden` プロパティを使用して個々のピボット項目を手動で非表示にしたり表示したりできます。各戦略には、`PivotField` クラスおよび `PivotItem` クラスの専用 API が用意されています。
{{% /alert %}}

## **はじめに**
ピボットテーブルは強力な分析ツールですが、集計結果をそのまま表示すると、レポートに必要な情報より多くの情報が含まれることがよくあります。フィルターは、特定のレポートで必要な行、列、または値のみを表示するためにピボットテーブルを絞り込む主な手段です。Aspose.Cells for JavaScript via C++ は、Microsoft Excel で利用できるのと同等のフィルター機能をプログラムから利用できるようにし、レポート生成の自動化を完全に実現します。
以下のフィルター戦略について説明します。
1. **ラベルフィルター** — テキストラベルに基づいて行または列フィールドの項目を絞り込みます。
2. **日付フィルター** — 日時値（または空セル）のみを含む行または列フィールドを絞り込みます。
3. **値フィルター** — データフィールドの集計値に基づいて項目を絞り込みます。
4. **上位 10 フィルター** — 値フィールドによる順位付けに基づいて、上位または下位 N 項目のみを表示します。
5. **ピボット項目の非表示/表示** — フィールド内の個々の項目の表示を手動で制御します。
各方法では、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスの異なるプロパティを使用します。いずれかのフィルターを適用した後は、新しいフィルター状態をキャッシュされたデータと計算結果に反映するため、ピボットテーブルの `pivotCache.refresh()` を呼び出す必要があります。

## **ラベルフィルター**
ラベルフィルターを使用すると、行または列フィールドの項目を、そのテキストのキャプションとパターンと比較することで絞り込めます。特定の文字で始まる製品名、特定の語を含む製品名、またはその他のキャプションに基づく条件に一致する製品だけを表示したい場合に便利です。
Aspose.Cells は、`pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` メソッドを通じてラベルフィルター機能を提供します。`filterType` 引数は、比較モード (`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` など) を指定します。`label1` と `label2` 引数には、比較対象のテキストを指定します。1 つの値との照合のみが必要な場合（例：前方一致や部分一致）は、`label2` に `""` を渡します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、指定した接頭辞で始まるキャプションを持つ項目だけが表示されるようラベルフィルターを適用して、ピボットテーブルを更新し、結果を保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **日付フィルター**
日付フィルターにより、今日、先週、今月、次の四半期、特定の日付範囲などの日付条件に基づいてピボットテーブルを絞り込めます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行または列エリアに日時セルまたは空セルだけが含まれる場合にのみ機能します。元のフィールドに数値やテキストなど他のデータ型が含まれている場合、日付フィルターは期待どおりの結果を生みません。このフィルターを適用する前に、フィールドが日付として書式設定されていること、およびすべての値が有効な `DateTime` インスタンスまたは空セルであることを確認してください。
Aspose.Cells は、`pivotField.filterByDate(PivotFilterType, DateTime[] values)` メソッドを通じて日付フィルター機能を提供します。`PivotFilterType` 列挙体には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` のような専用の日付フィルター値が含まれます。選択したフィルタータイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行エリアに日付フィールドを持つピボットテーブルを含むワークブックを読み込み、表示される項目を特定の日付範囲に制限する日付フィルターを適用して、ピボットテーブルを更新し、ワークブックを保存します。
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **値フィルター**
値フィルターは、ピボットテーブルがデータエリアで計算する集計値に対して作用します。テキストラベルを照合するのではなく、数値の合計値をしきい値と比較します。売上の合計が目標金額を超える製品だけを表示する、あるいは取引件数が特定の範囲内に収まる地域だけを表示する、といった使用例が典型的です。
Aspose.Cells は、`pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` メソッドを通じて値フィルター機能を提供します。`valueFieldIndex` パラメーターは、評価するデータフィールドを指定します（`pivotTable.getDataFields().indexOf(dataField)` を使用するか、コレクションを反復処理して位置を探してください）。`filterType` パラメーターでは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値が使用されます。2 つの `double` 引数には、しきい値を指定します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超える項目だけを残す値フィルターを適用して、ピボットテーブルを更新し、ワークブックを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **上位 10 フィルター**
上位 10 フィルターは、選択した値フィールドに基づいて上位または下位 N 項目だけを残す、値フィルターの特殊な形式です。「収益上位 10 製品」や「販売件数下位 5 地域」などのランキングレポートで広く使用されます。

{{% alert color="primary" %}}
上位 10 フィルターは、ピボットテーブルのデータエリアに 1 つ以上の値ピボットフィールドがある場合のみ有効です。値フィールドが 1 つ以上なければ、項目を順位付けするための集計指標が存在しないため、フィルターを適用できません。
Aspose.Cells は、`pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` メソッドを通じて上位 10 フィルター機能を提供します。`valueFieldIndex` パラメーターは、集計値に基づいて項目を順位付けするデータフィールドのインデックスです。`filterType` は `itemCount` の単位を選択します（`Count` は固定数の項目を残し、`Percent` は項目の割合を残すため、`itemCount` 自体が割合になります）。`isTop` は上位項目（`true`）を残すか下位項目（`false`）を残すかを指定し、`itemCount` は残す項目数または割合を指定します。
次の例では、値フィールドを含むピボットテーブルを持つワークブックを読み込み、売上の合計が上位の 10 項目だけを残す上位 10 フィルターを適用して、ピボットテーブルを更新し、ワークブックを保存します。
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **ピボット項目の非表示/表示によるフィルター**
構造化されたフィルター API に加えて、Aspose.Cells では個々のピボット項目の表示を直接制御できます。`PivotField` の `pivotField.getPivotItems()` コレクションを反復処理し、`isHidden` プロパティを切り替えることで、数式に基づくフィルターを適用せずに、特定の項目を選択的に非表示にできます。`pivotItem.isHidden = true` を設定すると、その項目がピボットテーブルから非表示になります。`pivotItem.isHidden = false` を設定すると、その項目が再び表示されます。
この方法は、フィルター条件が不規則または項目ごとに異なる場合、または特定のレポートに表示しない少数のカテゴリを非表示にする場合などに便利です。以下の例では、ピボットテーブルを含むワークブックを読み込み、名前で指定した特定の項目を非表示にし、その項目を表示する方法をデモして、ピボットテーブルを更新し、ワークブックを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **まとめ**
Aspose.Cells for JavaScript via C++ は、Microsoft Excel で利用できるピボットテーブルのフィルター機能をすべて備えています。ラベル、日付、値のフィルターは最も一般的な分析シナリオに対応し、上位 10 フィルターはランキングレポートを処理します。フィルター条件が不規則な場合、`pivotItem.isHidden` プロパティは、項目単位の柔軟な代替手段を提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定の項目を非表示にする）と、レポートに必要な内容にピボットテーブルを正確に絞り込み、コードのみでレポートを作成できます。

{{< app/cells/assistant language="javascript-cpp" >}}