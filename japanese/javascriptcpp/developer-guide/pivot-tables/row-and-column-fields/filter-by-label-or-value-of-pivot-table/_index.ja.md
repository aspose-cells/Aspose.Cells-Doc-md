---
title: ラベルまたは値によるピボットテーブルのフィルタリング
linktitle: ラベルまたは値によるピボットテーブルのフィルタリング
description: Aspose.Cells for JavaScript via C++ は、包括的なピボットテーブルのフィルター機能をサポートしています。このHDLでは、ラベルフィルター、日付フィルター、値フィルター、上位 10 件のフィルター、およびピボット項目の非表示または表示を使って、ピボットテーブルのデータを絞り込む方法を説明します。
keywords: Aspose.Cells, JavaScript via C++ ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位 10 件のフィルター, ピボット項目, ピボット項目の非表示
type: docs
weight: 10
url: /ja/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータを絞り込むための 5 つの実用的な戦略を提供します。テキストベースの行または列フィールドにはラベルフィルターを、日時セルまたは空白のみを含むフィールドには日付フィルターを、集約された数値には値フィルターを、値フィールドによる順位付けには上位 10 件のフィルターを適用できます。また、`isHidden` プロパティを使って、個別のピボット項目を手動で非表示または表示できます。各戦略は、`PivotField` および `PivotItem` クラスの専用 API を通じて利用できます。
{{% /alert %}}

## **はじめに**
ピボットテーブルは強力な分析ツールですが、集計結果には、レポートで提示する必要のある情報よりずっと多くの情報が含まれることがよくあります。フィルタリングは、特定のレポートで重要な行、列、または値にピボットテーブルを絞り込むための主な手段です。Aspose.Cells for JavaScript via C++ は、Microsoft Excel で利用できるフィルター機能を再現し、プログラムから利用できるようにすることで、レポート生成を完全に自動化できます。
このHDLでは、次のフィルター戦略について説明します。
1. **ラベルフィルター** — テキストラベルに基づいて行または列フィールドの項目をフィルタリングします。
2. **日付フィルター** — 日時値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルター** — データフィールドの集約値に基づいて項目をフィルタリングします。
4. **上位 10 件のフィルター** — 値フィールドによる順位付けで上位または下位 N 項目のみを表示します。
5. **ピボット項目の非表示 / 表示** — フィールド内の各項目を個別に表示制御します。
各手法では、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルターを適用した後は、新しいフィルター状態がキャッシュデータと計算値に反映されるように、ピボットテーブルで `pivotCache.refresh()` を呼び出す必要があります。

## **ラベルフィルター**
ラベルフィルターでは、行または列フィールドの項目を、テキストキャプションとパターンを比較してフィルタリングできます。製品名が特定の文字で始まる、特定の語を含む、またはキャプションに基づくその他の条件に一致する製品だけを表示したい場合に便利です。
Aspose.Cells は、`pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` メソッドを通じてラベルフィルタリングを提供します。`filterType` 引数は比較モード（`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` など）を選択します。`label1` と `label2` 引数は比較対象のテキストを指定します。1 つの値との比較だけが必要な場合は、`label2` に `""` を渡します（例: 前方一致または部分一致）。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定した接頭辞で始まる項目だけが表示されるようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。

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
                    // ピボットテーブルを含む既存のワークブックを読み込む
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // インデックスでワークシートにアクセスする（最初のワークシート）
                    const worksheet = workbook.worksheets.get(0);
                    // インデックスでピボットテーブルにアクセスする
                    const pivotTable = worksheet.pivotTables.get(0);
                    // 最初の行 PivotField を取得する
                    const rowField = pivotTable.rowFields.get(0);
                    // ラベルフィルターを適用する — 指定された接頭辞で始まるラベルの行項目のみを表示する
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // フィルターが反映されるように、ピボットテーブルのデータを更新して再計算する
                    pivotTable.refreshData();
                    // ワークブックをディスクに保存する
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
日付フィルターでは、今日、先週、今月、来四半期、または特定の日付範囲など、日付に基づく条件でピボットテーブルを絞り込めます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行または列領域に日時セルまたは空白値のみが含まれる場合にのみ機能します。対象のフィールドに数値やテキストなど他のデータ型が含まれている場合、日付フィルターは期待どおりの結果を生成しません。フィルターを適用する前に、フィールドが日付として書式設定され、すべての値が有効な `DateTime` インスタンスまたは空セルであることを確認してください。
Aspose.Cells は、`pivotField.filterByDate(PivotFilterType, DateTime[] values)` メソッドを通じて日付フィルタリングを提供します。`PivotFilterType` 列挙型には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの日付フィルターに専用の値が含まれます。選択したフィルターの種類に応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを持つピボットテーブルを含むワークブックを読み込み、表示される項目を特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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
                // ピボットテーブルを含む既存のワークブックを読み込む
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // ピボットテーブルを保持するワークシートにアクセスする（インデックス指定）
                const worksheet = workbook.worksheets.get(0);
                // インデックスを指定してピボットテーブルにアクセスする
                const pivotTable = worksheet.pivotTables.get(0);
                // 行エリアから日付 PivotField を取得する
                // （日付フィルターは、行/列エリアに日時セルまたは空白のみが含まれる場合にのみ機能します）
                const dateField = pivotTable.rowFields.get(0);
                // Between フィルターの日付条件を定義する
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // ピボットフィールドに日付フィルターを適用する
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // フィルターを反映させるため、ピボットテーブルを更新して再計算する
                pivotTable.refreshData();
                // ワークブックを保存する
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
値フィルターは、ピボットテーブルがデータ領域で計算する集約値に対して作用します。テキストラベルを照合するのではなく、数値の合計値をしきい値と比較します。代表的なユースケースには次のような例があります。販売額の合計が目標金額を超える製品だけを表示する、または取引件数が特定の範囲内に入る地域だけを表示する。
Aspose.Cells は、`pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` メソッドを通じて値フィルタリングを提供します。`valueFieldIndex` パラメータは評価対象のデータフィールドを指定します（`pivotTable.getDataFields().indexOf(dataField)` を使用するか、コレクションを反復して位置を見つけます）。`filterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を取ります。2 つの `double` 引数でしきい値を指定します。
次の例では、ピボットテーブルを含むワークブックを読み込み、販売額の集約値が数値のしきい値を超える項目だけを残す値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。

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
                // PivotFieldCollection に IndexOf がないため、データフィールドのインデックスを手動で查找する
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
                pivotTable.refreshData();
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

## **上位 10 件のフィルター**
上位 10 件のフィルターは、選択した値フィールドに基づいて、最高または最低 N 項目だけを残す値フィルターの特殊な形式です。「売上上位 10 製品」や「販売件数下位 5 地域」などのランキングレポートで広く使用されます。

{{% alert color="primary" %}}
上位 10 件のフィルターは、ピボットテーブルのデータ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。値フィールドが 1 つもない場合、項目を順位付けする基準となる集約値が存在せず、フィルターを適用できません。
Aspose.Cells は、`pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` メソッドを通じて上位 10 件のフィルタリングを提供します。`valueFieldIndex` パラメータは、項目の順位付けに集約値を使用するデータフィールドのインデックスです。`filterType` は `itemCount` の単位を指定します。`Count` は固定数の項目を残し、`Percent` は項目の割合を残すため、`itemCount` には割合を指定します。`isTop` は、上位項目を残すか（`true`）、下位項目を残すか（`false`）を示します。`itemCount` は、残す項目数または割合を指定します。
次の例では、値フィールドを持つピボットテーブルを含むワークブックを読み込み、販売額の合計に基づいて上位 10 項目だけを残す上位 10 件のフィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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
                // ピボットテーブルを含む既存のワークブックを読み込む
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // ピボットテーブルを保持するワークシートにアクセスする（インデックス 0）
                const worksheet = workbook.worksheets.get(0);
                // インデックスを指定してピボットテーブルにアクセスする
                const pivotTable = worksheet.pivotTables.get(0);
                // データ領域に少なくとも1つの値 PivotField があることを確認する
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // 対象行 PivotField（Top 10 を適用するフィールド）を取得する
                const rowField = pivotTable.rowFields.get(0);
                // 最初の（唯一の）データフィールドはインデックス 0 にあり、Top 10 はそれで項目を順位付けする
                const valueFieldIndex = 0;
                // 行フィールドに Top 10 フィルターを適用する:
                //   - valueFieldIndex = 0 — 項目を順位付けするために使用されるデータフィールド
                //   - filterType  = PivotFilterType.Count（項目数を固定して保持する;
                //     PivotFilterType.Percent の場合、10 は「上位10%」として解釈される）
                //   - isTop       = true（上位N件; false の場合は下位N件を意味する）
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // ピボットテーブルのデータを更新して再計算し、フィルターを反映させる
                pivotTable.refreshData();
                // ワークブックを保存する
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

## **ピボット項目の非表示または表示によるフィルタリング**
構造化されたフィルター API に加え、Aspose.Cells では各ピボット項目の表示状態を直接制御できます。`PivotField` の `pivotField.getPivotItems()` コレクションを反復し、`isHidden` プロパティを切り替えることで、数式ベースのフィルターを適用せずに、特定の項目だけを選択的に非表示にできます。`pivotItem.isHidden = true` を設定すると、その項目はピボットテーブルから非表示になります。`pivotItem.isHidden = false` を設定すると非表示が解除され、再び表示されます。
このアプローチは、フィルター条件が規則的でない場合や項目ごとに異なる場合（特定のレポートに表示すべきでない少数のカテゴリを名前で指定して非表示にする場合など）に便利です。次の例では、ピボットテーブルを含むワークブックを読み込み、名前を指定して特定の項目を非表示にし、その非表示を解除する方法も示します。ピボットテーブルを更新してワークブックを保存します。

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
                // ピボットテーブルを含む既存のブックを読み込む
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // ピボットテーブルを含む最初のワークシートにアクセスする
                const sheet = workbook.worksheets.get(0);
                // インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
                const pivotTable = sheet.pivotTables.get(0);
                // 対象のPivotFieldを取得する（項目を非表示/再表示する最初の行ラベルフィールド）
                const pivotField = pivotTable.rowFields.get(0);
                // 選択したPivotFieldのPivotItemsコレクションを反復する
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // 特定の名前/基準に一致するピボット項目を非表示にする
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // 非表示の解除を実演する：以前に非表示にしたピボット項目を再び表示する
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // 変更を反映するためにピボットテーブルを更新して再計算する
                pivotTable.refreshData();
                // ブックを保存する — 非表示の項目は基礎データには残るが、表示されるピボットテーブル出力からは除外される
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
Aspose.Cells for JavaScript via C++ は、Microsoft Excel と一致する一連のピボットテーブルフィルター機能を提供します。ラベル、日付、および値のフィルターは最も一般的な分析シナリオに対応し、上位 10 件のフィルターはランキングレポートを処理します。フィルター条件が規則的でない場合は、`pivotItem.isHidden` プロパティが、項目単位の柔軟な代替手段となります。これらの戦略を組み合わせると（たとえば、ラベルフィルターを適用した後に特定の項目を非表示にする）、コードのみを使用して、対象を的確に絞り込んだピボットテーブルレポートを作成できます。

{{< app/cells/assistant language="javascript-cpp" >}}