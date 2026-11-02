---
title: 範囲の転置
linktitle: 範囲の転置
description: この記事では、Aspose.Cells for JavaScript via C++ を使用して、Excel ファイルの行と列を相互に転置または回転する 3 つの異なるアプローチについて説明します。
keywords: Aspose.Cells, JavaScript via C++, スプレッドシート, 範囲の転置, データの回転, 転置関数, 動的配列式, 配列式, Excel TRANSPOSE, 行から列へ
type: docs
weight: 80
url: /ja/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ は、行と列を入れ替えてデータを回転させる 3 つの方法をサポートします。最初のアプローチはインプレースの `range.transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 番目は `cell.setDynamicArrayFormula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルする最新の動的配列 `=TRANSPOSE(...)` 数式を書き込みます。3 番目は `cell.setArrayFormula()` を使用して、古い Excel バージョンでも互換性のある従来の Ctrl+Shift+Enter (CSE) 配列数式を書き込みます。本記事では、各アプローチを手順ごとに解説し、完全なコード例を示します。
{{% /alert %}}

## **導入**
範囲を転置するとは、行が列になり、列が行になるように回転させ、データを主対角線に沿って反転させることです。Microsoft Excel ではワークシート関数 `TRANSPOSE` がこの操作を実行し、概念的なリファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) に記載されています。この概念はプログラムからセルの範囲に対して適用でき、さまざまな業務やレポートシナリオで有用です。
- 四半期ごとの売上レポートや年間レポートで、通常は横方向に四半期、縦方向に地域が配置されているものを入れ替える場合。
- ダッシュボードやグラフで軸の向きを変更し、時間系列を横ではなく縦に表示したい場合。
- 外部システムからインポートしたデータのレイアウトを、下流の分析やレポートテンプレートが期待する形に合わせる場合。
この記事では、以下の小規模な「地域別・四半期別売上」テーブルを例として使用します。このサンプル ワークブックではテーブルが範囲 **A1:D5** に配置され、**A1** は左上隅として空白、**B1:D1** に地域ヘッダー、**A2:A5** に四半期ヘッダーが設定されています。
| 地域            | ヨーロッパ | アジア   | 北米          |
|----------------|------------|----------|---------------|
| Qtr 1          | 21704714   | 8774099  | 12094215      |
| Qtr 2          | 17987034   | 12214447 | 10873099      |
| Qtr 3          | 19485029   | 14356879 | 15689543      |
| Qtr 4          | 22567894   | 15763492 | 17456723      |
以下では、Aspose.Cells for JavaScript via C++ を使用してこのデータを転置する 3 つの方法を紹介します。各方法は対象となる Excel バージョンとユースケースに合わせて選択できます。

## **アプローチ 1 — インプレースで範囲を転置 (Range.transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータを転置したい場合に使用します。**すべての Excel バージョン**で動作し、動的配列に依存しないため、最も安全なクロスバージョン互換オプションです。最終的な転置結果だけが必要で、元の `TRANSPOSE` 数式をブックに残す必要がない場合に最適です。

### **使用 API**
`Range.transpose()` は `Aspose.Cells.Range` クラスのインスタンス メソッドです。呼び出すと範囲内の行と列が交換され、行が列に、列が行に入れ替わります。このメソッドは数式を書き込まず、基になるセルの値を直接変更します。

### **手順**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` で `.xlsx` 形式のソース ワークブックを開きます。  
2. `workbook.getWorksheets().get(0)` で最初のワークシートを取得します。  
3. `worksheet.getCells()` でワークシートのセル コレクションにアクセスします。  
4. `cells.createRange("A1:D5")` で **A1:D5** のソース範囲を作成します。  
5. `source.transpose()` を呼び出してインプレースで範囲を回転させ、行と列を入れ替えます。  
6. `workbook.save(outputFile)` でワークブックを保存します。
転置後、このアンカー範囲には回転したデータが保持されます。最初の行は (空白, **ヨーロッパ**, **アジア**, **北米**) となり、最初の列は (空白, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**) となります。元の各販売列が転置後の行に変換されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **アプローチ 2 — 動的配列数式で転置 (Excel 365 / 2021)**
`=TRANSPOSE(A1:D5)` 数式を出力ブックにライブ数式として残し、ソース データが変更されたときに結果が自動的に更新されるようにしたい場合に使用します。対象の Excel ファイルは **Excel 365 / Excel 2021 以降**で、動的配列とスピル演算子がサポートされている必要があります。

### **使用 API**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` は `Aspose.Cells.Cell` クラスのメソッドで、セルの数式を **動的配列数式** として設定します。Excel は数式を一度評価し、結果を自動的に周囲のセルにスピルします。第 3 パラメーターを `true` に設定すると、Aspose.Cells は書き込み時に結果の値も計算します。

### **手順**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` でソース ワークブックをロードします。  
2. 最初のワークシートを取得し、セル コレクションにアクセスします。  
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)` を呼び出し、ソース範囲のすぐ下のセル **A6** に動的配列数式を設定します。  
4. `new FormulaParseOptions()` 引数はデフォルト設定を使用し、 `true` が数式を動的配列として扱い、スピル結果をワークブックに書き込むよう指示します。  
5. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** には数式 `=TRANSPOSE(A1:D5)` が保持され、Excel は自動的に **A6:E9** の領域（4 行 × 5 列）に結果をスピルします。

{{% alert color="primary" %}}
このアプローチは **Excel 365 / 2021 以降**でのみ動作します。古い Excel バージョンでは動的配列数式が正しくスピルされません。
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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **アプローチ 3 — 従来の配列数式 (CSE) で転置**
`TRANSPOSE` 数式をブックに残したまま、対象の Excel ファイルが **古い Excel バージョン（2021 以前、2019、2016、2013 など）**で開かれる可能性がある場合に使用します。従来の CSE（Ctrl+Shift+Enter）配列数式は、すべての Excel バージョンで評価できるレガシー互換代替手段です。

### **使用 API**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` は `Aspose.Cells.Cell` クラスのメソッドで、**クラシック配列（CSE）数式** をアンカー セルに割り当て、結果配列のサイズを宣言します。Aspose.Cells はマルチセル配列数式マーカーを書き込み、Excel が単一の配列式として評価し、宣言された範囲に結果を展開します。

### **手順**
1. 前述のアプローチと同様にソース ワークブックをロードします。  
2. 最初のワークシートを取得し、セル コレクションにアクセスします。  
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。第 2 引数 `4` は結果配列の行数、第 3 引数 `5` は列数です。  
4. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** が配列数式のアンカーとなり、評価された配列は A6 から始まる 4 行 × 5 列の範囲に展開され、A1:D5 の転置サイズと一致します。Excel は結果範囲全体に単一の配列数式マーカーを書き込み、古いバージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価する従来の Excel 手法であり、このアプローチはすべての Excel バージョンで汎用的に互換性があります。
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // xlsx の LoadOptions を使用してソースワークブックを読み込む
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // 最初のワークシートとその Cells コレクションにアクセスする
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // セル A6 に古典的な CSE 配列数式を設定する。
                // 数式 =TRANSPOSE(A1:D5) は、5 行 x 4 列のソース範囲を回転させる
                // 4 行 x 5 列の配列に変換する。第2引数 (4) は行数です
                // 第3引数 (5) は結果配列の列数です。
                // Aspose.Cells は CSE 配列数式マーカーを書き込み、Excel が以下のように評価するようにする
                // 単一の複数セル配列数式として、古い Excel バージョンと互換性がある
                // (2019、2016、2013 など) のような、動的配列スピルをサポートしないバージョンでも
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // 配列数式マーカーが永続化されるようにワークブックを保存する
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **比較 — 各アプローチの使用タイミング**
| アプローチ | API / メソッド | Excel バージョン | 元の数式は保持されますか？ | 出力範囲 |
|-----------|----------------|-------------------|----------------------------|----------|
| アプローチ 1 — インプレース転置 | `range.transpose()` | すべての Excel バージョン | いいえ（値のみ） | 初期アンカー範囲、5×4 |
| アプローチ 2 — 動的配列数式 | `cell.setDynamicArrayFormula()` | Excel 365 / 2021 以降 | はい（動的にスピル） | アンカーからスピル |
| アプローチ 3 — 従来の配列数式 (CSE) | `cell.setArrayFormula()` | すべての Excel バージョン | はい（マルチセル配列数式） | 明示的サイズ、4×5 |
**アプローチ 1** は、迅速でクロスバージョン対応の変換が必要で、転置された値だけを書き込みたい場合に適しています。**アプローチ 2** は、最新の Excel が保証され、数式をライブに保ちソースが変更されたときに自動更新させたい場合に適しています。**アプローチ 3** は、すべての Excel バージョンで数式を保持したまま最も広い互換性が必要な場合に使用します。

{{< app/cells/assistant language="javascript-cpp" >}}