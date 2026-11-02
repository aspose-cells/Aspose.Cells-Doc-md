---
title: DBF ファイルの読み取りと書き込み
description: Aspose.Cells は、スプレッドシートファイルを操作するための JavaScript via C++ ライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みに対応しています。この기사では、ファイル形式の詳細、対応機能、手順付き例を含めて、Aspose.Cells を使用して DBF ファイルからデータをインポートし、DBF ファイルへエクスポートする方法を説明します。
linktitle: DBF の読み取りと書き込み
url: /ja/javascript-cpp/reading-and-writing-dbf-files/
keywords: Aspose.Cells, JavaScript via C++ ライブラリ, DBF, dBASE, DBF 読み取り, DBF 書き込み, DBF インポート, DBF エクスポート, ファイル形式, .dbf
type: docs
weight: 200
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、そのワークブックを DBF 形式に戻して保存することで、レガシーデータベースアプリケーションで使用できます。
{{% /alert %}}

## **導入**
DBF (DataBase File) は、1980 年代初頭に dBASE が発表したレガシーデータベースファイル形式です。形式は古いものの、DBF ファイルは、会計、GIS などの専門アプリケーションで構造化データを保存する用途に依然として広く使用されています。Aspose.Cells を使えば、これらのレガシーファイルを現代のスプレッドシートワークフローにシームレスに統合できます。
このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートしており、次を実行できます。
- 既存の DBF ファイルから Aspose.Cells の Workbook オブジェクトにデータをインポートし、さらに処理したり、他の形式に変換したりできます。
- 新しい DBF ファイルを最初から作成したり、他のスプレッドシート形式からデータを変換して作成したりできます。
- DBF 形式との間でデータを出し入れする際に、フィールド定義、データ型、レコード構造を維持できます。
DBF ファイルは Microsoft Excel などのスプレッドシートアプリケーションで直接開くできるため、レガシーシステムと現代のスプレッドシートツールを結ぶ便利な手段になっています。

## **サポートされる DBF のバージョンと機能**
Aspose.Cells は次の DBF 形式バージョンをサポートしています。
- **dBASE III** — DBF 形式の最も初期版であり、最も広くサポートされているバリアントです。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョンです。

### サポートされる機能
このライブラリは、次の操作を網羅的にサポートします。
- DBF データを Workbook オブジェクトに読み込み、すべてのレコードとフィールド定義を保持します。
- ワークブックのデータを DBF 形式に書き戻し、dBASE 互換アプリケーション向けにエクスポートします。
- DBF ファイルで使用される一般的なデータ型（文字、数値、日付、論理フィールド）を処理します。
- 読み取り/書き込み操作中に、フィールド名、型、長さなどのフィールド定義を保持します。

### 制限事項と考慮点
DBF ファイルを操作するときは、次の制約に注意してください。
- ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト** です。
- フィールド名は **10 文字**までで、大文字である必要があり、スペースを含めることはできません。
- DBF ファイルの日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングはソースアプリケーションによって異なる場合があります（通常は Windows-1252 または OEM コードページ）。

## **DBF ファイルの読み取り**
Aspose.Cells を使えば、DBF ファイルのデータを Workbook オブジェクトに簡単に読み込めます。ライブラリでは `LoadOptions` クラスを使用してソース形式を指定し、読み込み処理中にデータが正しく解釈されるようにします。

### Aspose.Cells による DBF ファイルの読み取り
DBF ファイルを読み取るには、`LoadOptions` のインスタンスを作成し、その `loadFormat` プロパティを `LoadFormat.Dbf` に設定して、ファイルパスとともに `Workbook` コンストラクターに渡します。読み込み後、データには `Worksheets` コレクションからアクセスできます。このコレクション内でセルを反復処理し、値を抽出したり、必要に応じてデータを操作したりできます。
次の例では、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスして、セルの値を読む方法を示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
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
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
［開く］ダイアログでファイルを選択すると、Microsoft Excel で DBF ファイルを直接開くことができます。Excel は DBF ファイルを表計算シートとして扱い、そのレコードを表形式で表示します。これは、Aspose.Cells で読み書きしたデータをすばやく検証するのに便利です。
{{% /alert %}}

## **DBF ファイルの書き込み**
DBF ファイルへのデータ書き込みは、Aspose.Cells でその他のスプレッドシート形式を保存する場合とほぼ同じパターンです。Workbook を作成または読み込み、ワークシートにデータを入力し、ターゲットの形式として `SaveFormat.Dbf` を指定して `save` メソッドを呼び出します。

### Aspose.Cells による DBF ファイルの書き込み
DBF ファイルを作成するには、次の手順を実行します。
1. 新しい `Workbook` インスタンスを作成します。
2. `Worksheets` コレクションから最初のワークシートにアクセスします。
3. 先頭行にヘッダーを、後続行にレコードを配置するなどして、ワークシートにデータを入力します。
4. ファイルパスと `SaveFormat.Dbf` をパラメーターとして `Workbook.save` メソッドを呼び出します。
次の例では、新しい DBF ファイルを最初から作成する方法を示します。サンプルのデータ（文字列、数値、日付）を含むワークシートを作成し、DBF 形式へのエクスポート時にフィールド型がどのように処理されるかを説明します。

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // 列ヘッダー
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // データ行 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // データ行 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // データ行 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // データ行 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // データ行 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // 可読性を高めるために列幅を設定
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
DBF ファイルにデータを書き込むときは、データがその形式の制限に適合していることを確認してください。フィールド名は 10 文字以下とし、スペースを含めることはできません。合計が 4000 バイトを超えるレコードは正しく保存されません。日付は YYYYMMDD 形式で表現できる有効な日付値にしてください。
{{% /alert %}}

## **データ型と書式設定に関する考慮点**
Aspose.Cells と DBF 形式の間でデータを転送するときは、2 つのシステム間でデータ型がどのように対応付けられるかを理解することが、データ整合性を確保するために重要です。

### セル型から DBF フィールド型への対応
保存時に、Aspose.Cells のセル値は適切な DBF フィールド型に自動的に変換されます。
- **文字列**は文字 (C) フィールドに対応付けられます。
- **数値**（整数と小数）は数値 (N) フィールドに対応付けられます。
- **日付値**は `YYYYMMDD` 形式の日付 (D) フィールドに対応付けられます。
- **ブール値**は論理 (L) フィールドに対応付けられます。

### エンコーディング
DBF ファイルでは、作成元アプリケーションによって異なる文字エンコーディングが使用されることがあります。Aspose.Cells はほとんどの場合エンコーディングを透過的に処理しますが、文字の表示に問題が発生した場合は、ソースファイルのエンコーディングを確認する必要があるかもしれません。

### フィールド名のルール
DBF のフィールド名は次のルールに従う必要があります。
- 最大 10 文字です。
- 英字で始める必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時の大文字小文字にかかわらず、大文字で保存されます。

### 出力の確認
DBF ファイルを書き込んだ後、Microsoft Excel または dBASE 互換アプリケーションでファイルを開くと、結果を確認できます。データはフィールド名が列ヘッダーとなる表形式で表示され、入力したデータに基づいてレコードが格納されます。

## **DBF と他の形式間の変換**
Aspose.Cells を使用して DBF ファイルを読み書きする、最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの現代のスプレッドシート形式との間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで他のサポートされている形式で再保存したり、その逆を行ったりすることができます。

{{< app/cells/assistant language="javascript-cpp" >}}