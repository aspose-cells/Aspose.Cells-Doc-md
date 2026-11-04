---
title: Aspose.Cells for JavaScript via C++ でピボットテーブルにフィルターフィールドを追加する
linktitle: Aspose.Cells for JavaScript via C++ でピボットテーブルにフィルターフィールドを追加する
description: Aspose.Cells for JavaScript via C++ を使用して、ピボットテーブルにフィルターフィールドを追加して設定する方法を学びます。フィルターフィールドの追加、単一選択のフィルター、複数選択のフィルターについても説明します。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, ピボットテーブル, フィルターフィールド, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルター
type: docs
weight: 250
url: /ja/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルのフィルターフィールドに関するライフサイクル全体を支持しています。高レベルの簡易 API または低レベルの `getPageFields()` コレクションからフィルターフィールドを追加できます。また、フィルターを単一選択モードで操作したり、フィルターを解除してすべてのフィルター項目を表示したり、フィールドを複数選択モードに切り替えて、Excel のチェックボックス式ユーザーインターフェースで複数のフィルター項目を一度に選択したりできます。
{{% /alert %}}

## **はじめに**
フィルターフィールドは、ソースデータの*どの部分集合*をピボットボディに表示するかを制御するピボットフィールドです。Excel でレンダリングされたピボットテーブルの上部にあるドロップダウンから、エンドユーザーがこのフィールドを確認できます。利用可能なフィルター項目を選択すると、そのフィルター項目に属するレコードのみが集計されるようにピボットボディが再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` ではなく、`PivotFieldType.Page` として登録されるとフィルターフィールドになります。

## **フィルターフィールドの追加**

### `addFieldToArea` を使用してフィルターフィールドを追加する
次の例では、小さな Fruit / Year / Amount データセットを作成し、`Fruit` を行領域、`Amount` をデータ領域、`Year` をフィルター領域に配置して E3 セルにピボットテーブルを作成し、ピボットテーブルを更新してワークブックを保存します。

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
            // 新しいワークブックを作成する
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            // ヘッダー行を設定する
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9行のサンプルデータ（Fruit、Year、Amount）を入力する
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // E3セルを基準位置とするピボットテーブルを追加する
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // フィールドを各領域に追加する：FruitをRow、AmountをData、YearをPageフィールドとして設定
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // ピボットテーブルのデータを更新して計算する
            pivotTable.calculateData();
            // ワークブックを保存する
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### `getPageFields().add` を使用してフィルターフィールドを追加する
既存の `PivotField` インスタンスがある場合は、`pivotTable.getPageFields().add(pivotField)` に直接渡すことができます。ピボットテーブルとフィルターフィールドの構築は直前の例と同じです。フィルター領域への最終的な登録だけが、低レベルの API 呼び出しに置き換えられます。

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
            // — ピボットテーブルとページフィールドは、次のように
            //   シナリオ 1a とまったく同じ構成にしています
            //   （Fruit/Year/Amount データ、E3 にピボット、Fruit→Row、
            //   Amount→Data）。以下では、BaseFields コレクションから
            //   Year PivotField を取得し、PageFields.Add に渡します。これは
            //   AddFieldToArea の低レベルの代替手段です。結果は
            //   シナリオ 1a と機能的に同一です。
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // ヘッダー
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // サンプルデータ（9行）
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // A1:C10 をカバーし、E3 にピボットテーブルを追加
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Fruit -> Row、Amount -> Data（Year は後で Page に配置）
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 低レベルの方法：BaseFields から既存の Year PivotField を取得し、
            // PageFields.Add(PivotField) を使用して Page 領域に登録します。
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // 新しいページフィールドが保存されるワークブックに反映されるように更新
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **単一選択フィルター（1 つのフィルター項目を表示）**
デフォルトの単一選択モードでは、フィルターフィールドは 1 つのドロップダウンとして表示され、`pivotField.currentPageItem` の整数値が、どのフィルター項目でピボットボディを制御するかを指定します。特定のインデックスを設定すると、その項目だけが選択されます。特殊なセンチネル値 `0x7FFD`（10 進数 32765）を設定すると、フィルターが解除され、すべてのフィルター項目が一括して集計されます。単一選択は既定の動作であるため、明示的に有効にする必要はありません。

### すべての項目を表示する
`currentPageItem` をマジック値 `0x7FFD` に設定すると、フィルターを解除した場合と同じ結果になります。ピボットボディは、フィルターが適用されていないかのように、すべてのフィルター項目をまとめて集計します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // 新しいワークブックを作成します
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // 果物／年度／金額のデータを入力します
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // E3にピボットテーブルを作成します
            const pivotTables = sheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:C7", 2, 4);
            // ピボットフィールドを構成します：果物→行、金額→データ、年→ページ
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // ページフィルターをクリアして、ページフィールド内のすべての項目を表示できるようにします。
            // 0x7FFD（10進数で32765）は「すべての項目」を表す特殊なセンチネル値です —
            // Excelのページフィールドのドロップダウンで「(すべて)」を選択した場合と同等です。
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
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

### 特定の 1 つの項目を表示する
`currentPageItem` に実際のインデックスを設定すると、そのフィルター項目が 1 つだけ選択されます。このインデックスは、フィルターフィールドの項目を並べ替えたリスト内での位置です。したがって、たとえば `1` を指定すると、並べ替え後の 2 番目の項目が選択されます。

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
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // ワークブックを作成
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // サンプルデータ（Fruit/Year/Amount）を追加
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // E3にピボットテーブルを追加
                const pivotTables = sheet.pivotTables;
                const pivotTable = pivotTables.add("=A1:C5", 2, 4);
                // フィールドを追加: Fruit→行、Amount→データ、Year→ページ
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // ページフィールド固有の操作
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = 並べ替え順での2番目の項目（例: "2021"）
                // ピボットテーブルを更新して計算
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **複数選択フィルター**
複数選択フィルターでは、フィルターのドロップダウンがチェックボックスリストに変わり、エンドユーザーが複数のフィルター項目を同時に選択できます。Aspose.Cells には、組み合わせて使用する 2 つのプロパティがあります。複数選択ユーザーインターフェースを有効にするには、まず `pivotField.isMultipleItemSelectionAllowed` を `true` に設定する必要があります。有効化後、`pivotItem.isHidden` によってチェックボックスリストに表示する項目を制御できます。そのため、すべての項目を表示することも、特定の項目だけを許可リストに含めることもできます。

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
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — ピボットテーブルとページフィールドは、次のように構築します。
                //   シナリオ 1a（Fruit/Year/Amount データ、E3 にピボット、Fruit→Row、
                //   Amount→Data、Year→AddFieldToArea 経由で Page）。
                //   以下では、ページフィールドに複数選択フィルターを適用します。
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // サンプルデータ: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTable = pivots.add("=A1:C10", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — ページフィールドで複数選択を有効化
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // パート A — すべての項目を選択（すべての項目を表示可能にする）
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // パート B — ソース値に基づいて特定の項目のみを選択
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **注:** `pivotItem.isHidden` を使用して複数選択フィルターを設定する場合、**少なくとも 1 つの `PivotItem` を表示状態 (`isHidden === false`) に保つ必要があります**。すべての項目を非表示にすると、Excel でファイルを開いたときにクラッシュするか、空のピボットテーブルが表示されます。必ず、ソースデータに基づいて複数選択用の許可リストを作成し、少なくとも 1 つの項目が含まれていることを確認してください。

## **どの API とどのモードを使用しますか？**
以下の表は、各 API とモードをいつ使用するかについてまとめたものです。詳細をすべて読まずに適切な組み合わせを選べます。
| シナリオ／ユースケース | 推奨 API | 使用するプロパティ | 備考 |
|---|---|---|---|
| ソース列名に基づいてフィルターフィールドを追加（最も一般的） | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | 該当なし | 高レベルの 1 行の処理です。`PivotField` の参照が必要な場合を除き、これを使用します。 |
| すでに `PivotField` オブジェクトを保持している場合 | `pivotTable.getPageFields().add(pivotField)` | 該当なし | フィールドオブジェクトを他の場所で取得した場合、または再利用する必要がある場合に使用します。 |
| 単一のフィルター項目に絞り込む（既定モード） | `pivotField.currentPageItem` | 特定のインデックスに設定 | たとえば、`1` は並べ替えられたリストの 2 番目の項目を表示します。 |
| すべての項目を表示してフィルターを解除する | `pivotField.currentPageItem` | `0x7FFD` に設定 | マジック値 `0x7FFD`（10 進数 32765）は「すべての項目」を表すセンチネル値です。 |
| Excel で複数選択ユーザーインターフェースを有効にする | `pivotField.isMultipleItemSelectionAllowed` | `true` に設定 | 複数選択を有効にするには、すべての `isHidden` の割り当てを適用する前に、この設定を行う必要があります。 |
| 複数選択リストで個別の項目を非表示または表示する | `pivotItem.isHidden` | 項目ごとに設定 | 少なくとも 1 つの項目を表示状態 (`isHidden === false`) に保つ必要があります。 |

{{% alert color="primary" %}}
複数選択フィルターを設定する際は、必ず可視性の制約に注意してください。複数選択フィルターフィールド内のすべての `PivotItem` が非表示になっている場合、Excel でファイルを開いたときにクラッシュするか、空のピボットテーブルが表示されます。ソースデータに基づいて許可リストを作成し、少なくとも 1 つの項目を表示状態にしてください。これにより、保存したワークブックをどの環境でも確実に開けるようになります。
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}