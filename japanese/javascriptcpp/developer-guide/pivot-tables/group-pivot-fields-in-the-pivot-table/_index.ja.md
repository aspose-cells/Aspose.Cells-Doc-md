---
title: ピボットテーブルでピボットフィールドをグループ化
linktitle: ピボットテーブルでピボットフィールドをグループ化
description: Aspose.Cells for JavaScript via C++ で PivotField.group と PivotFieldGroupOptions を使用して、ピボットテーブルの行および列のピボットフィールドを月や四半期などの日付期間や数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, JavaScript via C++
type: docs
weight: 80
url: /ja/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行または列フィールドに多数の異なる項目が含まれる場合に便利です。たとえば、数百件の日時が格納された日付フィールドや、散在する多数の数値が格納された数値フィールドです。グループ化により、これらの項目を意味のあるセクションにまとめることができます。日付は月、四半期、年に、数値は 0‑1、2‑3、4‑5 などの範囲にグループ化され、巨大なピボットテーブルがコンパクトになり、分析が容易になります。Aspose.Cells は `PivotField.group()` メソッド（データ型による自動グループ化）と `PivotField.group(PivotFieldGroupOptions)`（カスタムオプション）を通じてこの機能を提供します。
- 日付のグループ化は、個々の日付を日、月、四半期、年といった大きな期間にまとめ、時間階層（例: 年 → 四半期 → 月）を構築します。時間のトレンドが一目で確認でき、各期間レベルがピボットテーブルの行または列エリアに独立したピボットフィールドとして表示されます。
- グループ化は、ピボットテーブルの **ROW** または **COLUMN** エリアに配置されたフィールドに対してのみ利用可能です。データ（値）フィールドは直接グループ化できません。そのようなフィールドをグループ化するには、まずピボットテーブルの行または列エリアに配置する必要があります。

## **ピボットフィールドを自動的にグループ化**
パラメータなしの `PivotField.group()` オーバーロードは、フィールドのデータ型を検査して自動的にグループ化します。日付（および空白）のみを含むフィールドは月単位でグループ化され、数値（および空白）のみを含むフィールドは自動的に間隔を算出して数値範囲にグループ化されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **カスタムオプションでピボットフィールドをグループ化**
`PivotFieldGroupOptions` クラスはカスタムグループ化設定を提供します。日付フィールドの場合は `startDate`、`endDate`、`groupTypes` を設定し、数値フィールドの場合は `startNumber`、`endNumber`、`interval` を設定します。`newPivotField` プロパティは、グループ化が元のフィールドと一緒に新しいピボットフィールドを作成するかどうかを制御します（本記事末尾の「注」セクションを参照）。

### **日付フィールドを月と四半期でグループ化**
次の例は、サンプルピボットテーブルの日時行フィールドを開始日と終了日の間で月と四半期にグループ化します。コードは [sample Excel file](sampleGroupPivotFieldsInPivotTable.xlsx) をロードし、グループ化を実行し、ピボットテーブルデータを再計算して、グループ化された結果を保存します。スクリーンショットは、日時行フィールドが四半期と月でグループ化された様子を示しています。  
`options.groupTypes` の順序は無視されます。グループタイプの列挙順に関係なく、フィールドは常に最も大きな期間から最も小さな期間へと表示されます（年、四半期、月、日、時間、分、秒）。この例では `options.groupTypes` に月が四半期より先に列挙されていますが、四半期が外側レベル、月が内側レベルとして表示されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![月と四半期でグループ化されたピボットテーブル](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化**
サンプルピボットテーブルの `FieldTwo` は最初はデータ（値）フィールドです。行または列フィールドのみがグループ化できるため、コードは最初に `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` を呼び出して `FieldTwo` を行エリアに移動し、ピボットテーブルを更新した後、`startNumber = 0`、`endNumber = 5`、`interval = 2` を使用して数値フィールドを 0‑1、2‑3、4‑5 の範囲にグループ化します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **注**

{{% alert color="primary" %}}
- `PivotField.groupBy()` メソッドのオーバーロードは非推奨となり、API から削除されました。代わりに `PivotField.group()` と `PivotField.group(PivotFieldGroupOptions)` を使用してください。
- Microsoft Excel では、数値フィールドのグループ化は元のピボットフィールドをグループ化された範囲で置き換えますが、日付フィールドのグループ化は元のフィールドの横に新しいピボットフィールド（例: 四半期、月）を作成します。Aspose.Cells 26.10 以降、`PivotField.group()` メソッドは Excel と同様の動作をします。`PivotFieldGroupOptions.newPivotField` プロパティは旧バージョンとの互換性のために存在し、数値グループ化ではデフォルトが `false`、日付時系列のグループ化ではデフォルトが `true` です。元のピボットフィールドを置き換えて日付をグループ化したい場合は `false` に設定してください。
- `PivotFieldGroupOptions.interval` プロパティは数値グループ化および日付を日単位でグループ化する場合（例: 7 日間隔）にのみ有効です。月、四半期、年で日付をグループ化する場合は無視されます。
{{% /alert %}}

## **関連項目**
- [ピボットテーブルに行と列のフィールドを追加](/cells/ja/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/javascript-cpp/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルを更新](/cells/ja/javascript-cpp/refresh-pivot-table/)
- [ピボットフィールド項目の離散グループ化](/cells/ja/javascript-cpp/discrete-group-pivot-fields/)

{{< app/cells/assistant language="javascript-cpp" >}}