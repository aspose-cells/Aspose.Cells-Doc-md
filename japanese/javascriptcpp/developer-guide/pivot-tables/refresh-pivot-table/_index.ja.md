---
title: Aspose.Cells for JavaScript via C++ の v26.7+ ピボット更新 API でピボットテーブルとピボットキャッシュを更新
linktitle: Aspose.Cells for JavaScript via C++ の v26.7+ ピボット更新 API でピボットテーブルとピボットキャッシュを更新
description: Aspose.Cells for JavaScript via C++ の v26.7+ ピボット更新 API を使用してピボットテーブルを更新する方法を学びます。workbook.refreshAll、worksheet.refreshPivotTables、pivotCache.refresh、pivotTable.calculateData、pivotCache.getPivotTables を使った実用的なコード例を示します。
keywords: Aspose.Cells, JavaScript via C++, ピボットテーブル, 更新, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /ja/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層型の更新 API を提供します。**Aspose.Cells for JavaScript via C++ v26.7** 以降では、旧来のメソッド `pivotTable.refreshData()` は非推奨としてマークされ、この記事介绍的効率的でキャッシュを考慮した API に置き換える必要があります。
{{% /alert %}}

## はじめに
ピボットテーブルの更新が、1 回の操作だけで済むことはほとんどありません。内部では、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリング済みの値を結ぶ、階層的なデータチェーンを管理しています。このチェーンを理解することが、さまざまな場面で適切な更新 API を選ぶ鍵となります。
4 層のデータチェーンは以下のとおりです。
1. **データソース** — 生データが格納されている元のワークシート範囲、データベースクエリ、または統合範囲です。
2. **PivotCache** — ソースデータのインメモリのスナップショットです。すべてのピボットテーブルは `PivotCache` の上に構築され、データはここで収集されて集計されます。
3. **PivotTable** — 行、列、値、フィルターの各フィールドを定義する表示オブジェクトです。`PivotTable` はデータソースから直接読み取るのではなく、`PivotCache` からのみ読み取ります。
4. **Cells** — `getCells()` によって返されるワークシートのセルであり、`PivotTable` は計算された値とスタイルをここにレンダリングします。

{{% alert color="primary" %}}
`pivotCache.getSourceType()`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 では、`pivotCache.refresh()` は **`SHEET`** と **`CONSOLIDATION`** のソースタイプのみをサポートしています。つまり、ワークシート範囲に格納されているデータのみが対象です。外部ソース（データベース、外部接続など）は、現時点ではキャッシュ API 経由で更新できません。
このチェーン構成により、Aspose.Cells には 2 つの基本的な更新経路があります。
- **`pivotTable.calculateData()`** — キャッシュ済みのデータから 1 つの `PivotTable` の表示を再計算します。データソースへの往復アクセスは行いません。
この記事のすべての例ではワークシートのセルがソースデータとして使用されるため、ソースタイプは `SHEET` となり、更新操作は説明どおりに動作します。
{{% /alert %}}

## クイックスタート
ワークブック内のすべてのピボットテーブルを更新するための最小限のコードだけが必要な場合は、1 回の呼び出しで十分です。

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
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

他のセクションでは、より限定的な API を選ぶべき場合について説明します。

## 必要なインポート
この記事のすべての JavaScript サンプルは、次のモジュールインポートで始まります。これは、ピボット関連の型が `Aspose.Cells.Pivot` namespace で公開されているためです。
- `const Aspose = require('aspose.cells');`

## ワークブック内のすべてのピボットテーブルを更新
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映していることを確認する必要がある場合、最も簡単かつ包括的な API は `workbook.refreshAll()` です。1 回の呼び出しでワークブック全体を処理し、各 `PivotCache` をソースから更新してから、そのキャッシュに依存するすべての `PivotTable` を再計算します。パフォーマンスを懸念する必要のない、ワークブック全体に対する一般的な更新では、このアプローチを推奨します。
次の例では、`Fruit`/`Year`/`Amount` のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成して、一部のソース値を変更します。その後、`refreshAll()` を呼び出すことで、すべての内容を 1 回で最新の状態に更新します。

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
            // 新しいワークブックを作成
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // ヘッダー行をセル A1:C1 に書き込み
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // データ行をセル A2:C9 に書き込み（2020年および2021年にわたるフルーツデータの8行）
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // ピボットテーブルを追加: ソース範囲 "A1:C9"、宛先セル "E3"
            const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
            // ピボットフィールドを割り当て: Fruit を行、Year を列、Amount をデータ領域に設定
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 変更をシミュレートするため、ソースデータ内の複数の Amount 値を変更
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // ワークブック内のすべてのピボットテーブル／ピボットキャッシュを更新
            workbook.refreshAll();
            // ワークブックを保存
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## 単一のワークシート上のすべてのピボットテーブルを更新
特定のワークシートにあるピボットテーブルだけを更新する必要がある場合があります。たとえば、他のワークシートのピボットテーブルは関連しておらず、更新してはならないことが分かっている場合です。この場合、Aspose.Cells は対象範囲を単一の `Worksheet` インスタンスに限定する `worksheet.refreshPivotTables()` を提供します。

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
            const { Workbook, SaveFormat } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## 単一のピボットテーブルを更新
単一のピボットテーブルを細粒に制御する場合、キャッシュベースの API には 2 つの選択肢があります。どちらを選ぶかは、変更対象が元のソースデータなのか、それともピボットテーブル自体の表示やレイアウト設定だけなのかによって決まります。

### ソースデータが変更された場合 — `pivotCache.refresh()` を使用
元のソースデータが変更された場合は、`pivotTable.getPivotCache().refresh()` が適切なエントリーポイントです。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### 表示やレイアウトのみが変更された場合 — `pivotTable.calculateData()` を使用
ソースデータは変更されておらず、ピボットテーブルの表示またはレイアウト設定だけが変更された場合（たとえば、フィールドを別の領域に移動した場合や、ファイルを開くときに更新する設定を切り替えた場合）、データソースへの往復アクセスは必要ありません。キャッシュにはすでに正しいデータが格納されているため、レンダリングされた `PivotTable` だけを再計算すれば十分です。この場合は `pivotTable.calculateData()` が適切です。
次の例では、ピボットテーブルのソースデータ以外のプロパティを変更し、既存のキャッシュから再レンダリングするために `calculateData()` を呼び出します。

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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // 果物／年／金額のヘッダー行を書き込みます
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // 8行のデータ（2～9行、ソース範囲 A1:C9 に収まる）を書き込みます
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // 宛先セル E3 に配置し、A1:C9 をデータ元とするピボットテーブルを追加します
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                // フィールドを割り当てます：Fruit を Row、Year を Column、Amount を Data に設定
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // 表示／レイアウトのプロパティを変更します。これは表示のみの変更であり、
                // PivotCache.Refresh() を通じてソースデータを再読み込む必要はありません。
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() は、PivotCache に保持されているデータから、このピボットテーブルの
                // 表示（データとスタイル）を再描画します。ソースデータが変更されていないため、
                // ソースへの往復処理は行われず、キャッシュされた値が再計算されるだけです。
                // 計算結果はワークシートのセルに書き込まれます。
                pivotTable.calculateData();
                // ワークブックをディスクに保存します
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

複数のピボットテーブルが 1 つのキャッシュを共有しているケースがよくあります。たとえば、一括更新の前にこれらを列挙する場合や、共有キャッシュの影響を診断する場合には、`pivotCache.getPivotTables()` を使用します。このメソッドは、指定したキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 非推奨の `pivotTable.refreshData()` からの移行
Aspose.Cells for JavaScript via C++ v26.7 より前、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルで `pivotTable.refreshData()` を個別に呼び出すことでした。v26.7 では、このメソッドは**非推奨**としてマークされ、上で説明したキャッシュを考慮した API に置き換える必要があります。
実際のワークブックでは、テーブルごとの `refreshData()` の使用に問題が生じる理由は次の 2 つです。
- ソースが変更されていない場合でも、呼び出しのたびにソースからデータを再取得します。
推奨される置き換え方法は次のとおりです。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを含むワークブックで、新しい効率的方法を示します。

## どの更新 API を使用すべきか
以下の表は、利用可能な更新 API と、それぞれを選ぶ場面をまとめたものです。
| 目的 | 推奨 API | 備考 |
|------|-----------------|-------|
| ワークブック内のすべてを更新 | `workbook.refreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを処理します。 |
| 単一シート上のピボットテーブルのみ更新 | `worksheet.refreshPivotTables()` | 対象を 1 つのワークシートに限定します。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | その共有キャッシュに基づくすべてのピボットテーブルを更新します。 |
| 表示やレイアウトの設定のみが変更された | `pivotTable.calculateData()` | 不要なソースへの往復を省略します。 |
| 共有キャッシュにあるすべてのピボットテーブルを列挙する | `pivotCache.getPivotTables()` | 一括更新前に列挙するために使用します。 |
実際には、非推奨のテーブルごとの `refreshData()` ではなく、キャッシュベースの API の使用を推奨します。これらの API は共有キャッシュを考慮し、冗長なソース取得を避け、更新要件を満たす最小のスコープを選択できます。

## よくある落とし穴
- **保存前に更新することを忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみワークシートにレンダリング済みの値を書き込みます。ソースセルを変更した場合は、`workbook.save()` の前に `pivotCache.refresh()`（または `workbook.refreshAll()`）を呼び出してください。そうしないと、保存されたファイルには依然として古い集計値が含まれます。
- **テーブルごとに非推奨の `refreshData()` を呼び出す。** v26.7 では、`pivotTable.refreshData()` は非推奨としてマークされ、呼び出しごとにソースを再取得します。複数のピボットテーブルが 1 つのキャッシュを共有している場合、N 回の冗長なソース取得が発生します。1 回の `pivotCache.refresh()` に置き換え、テーブルごとに `pivotTable.calculateData()` を呼び出します。
- **レイアウトだけを変更したのに更新してしまう。** ソースデータに手を触れずにピボットテーブルの表示（列の順序、`getConsolidationFunction()` など）のみ変更した場合、`pivotCache.refresh()` は不要で低速です。既存キャッシュから再レンダリングするには `pivotTable.calculateData()` を呼び出してください。
- **外部ソースは `pivotCache.refresh()` でサポートされていない。** ピボットテーブルのソースが外部接続（データベース、OLAP キューブなど）にある場合、v26.7 では `pivotCache.refresh()` で更新できません。現時点でサポートされるのは `SHEET` と `CONSOLIDATION` のソースタイプのみです。外部ソースの場合は、ワークブックを再度開くか、ソースからキャッシュを再構築してください。

{{< app/cells/assistant language="javascript-cpp" >}}