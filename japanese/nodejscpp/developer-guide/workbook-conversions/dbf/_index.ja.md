---
title: DBFファイルの読み取りと書き込み
description: Aspose.Cellsはスプレッドシートファイルを操作するためのAspose.Cells for Node.js via C++ライブラリで、dBASE IIIおよびIV (DBF)ファイルの読み取りと書き込みをサポートしています。この記事では、ファイル形式の詳細、サポートされている機能、ステップバイステップの例を含め、Aspose.Cellsを使用してDBFファイルからデータをインポートしたりDBFファイルにデータをエクスポートしたりする方法を説明します。
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++ library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /ja/nodejs-cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cellsは、DBF (dBASE)ファイルの読み取りと書き込みを完全にサポートします。既存のdBASE IIIおよびdBASE IVファイルをWorkbookオブジェクトに読み込み、豊富なAspose.Cells APIを使用してデータを操作し、レガシーデータベースアプリケーションで使用するためにワークブックをDBF形式で保存できます。

{{% /alert %}}

## **はじめに**

DBF (DataBase File)は、1980年代初頭にdBASEによって導入されたレガシーデータベースファイル形式です。形式の古さにもかかわらず、DBFファイルは構造化データの保存のために多くの業界で今も広く使用されており、特に会計、GIS、その他の特殊なアプリケーションで使用されています。Aspose.Cellsを使用すると、これらのレガシーファイルを最新のAspose.Cells for Node.js via C++スプレッドシートワークフローにシームレスに統合できます。

このライブラリはDBFファイルの読み取りと書き込みの両方をサポートしており、以下の機能を提供します:

- 既存のDBFファイルからAspose.Cells Workbookオブジェクトにデータをインポートし、さらに処理したり他の形式に変換したりする。
- 他のスプレッドシート形式からデータを変換して、新しいDBFファイルを最初から作成する。
- DBF形式との間でデータを転送する際に、フィールド定義、データ型、レコード構造を維持する。

DBFファイルはMicrosoft Excelや他のスプレッドシートアプリケーションで直接開くこともできるため、レガシーシステムと最新のスプレッドシートツール間の便利なブリッジとなっています。

## **サポートされているDBFバージョンと機能**

Aspose.Cellsは以下のDBF形式バージョンをサポートしています:

- **dBASE III** — DBF形式のオリジナルで、最も広くサポートされているバリアント。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョン。

### サポートされている機能

このライブラリは、以下の操作の包括的なサポートを提供します:

- すべてのレコードとフィールド定義を保持したまま、DBFデータをWorkbookオブジェクトに読み取る。
- ワークブックデータをDBF形式に書き戻して、dBASE互換アプリケーションにエクスポートする。
- 文字、数値、日付、論理フィールドを含む、DBFファイルで使用される一般的なデータ型の処理。
- 読み取り/書き込み操作中に、フィールド名、型、長さなどのフィールド定義を保持する。

### 制限事項と考慮事項

DBFファイルを扱う際は、以下の制約事項に留意してください:

- ファイルあたりのフィールド数の最大は**128**です。
- レコードサイズの最大は**4000バイト**です。
- フィールド名は**10文字**以内に制限され、大文字である必要があり、スペースを含めることはできません。
- DBFファイルの日付値は`YYYYMMDD`形式で保存されます。
- 文字エンコーディングはソースアプリケーションによって異なる場合があります(一般的にはWindows-1252またはOEMコードページ)。

## **DBFファイルの読み取り**

Aspose.Cellsを使用すると、DBFファイルからWorkbookオブジェクトにデータを簡単に読み込むことができます。このライブラリは`LoadOptions`クラスを使用してソース形式を指定し、読み込みプロセス中にデータが正しく解釈されるようにします。

### Aspose.CellsでDBFファイルを読み取る

DBFファイルを読み取るには、`LoadOptions`インスタンスを作成し、その`LoadFormat`プロパティを`LoadFormat.Dbf`に設定して、ファイルパスと一緒に`Workbook`コンストラクタに渡す必要があります。読み込まれたら、データは`Worksheets`コレクションを介してアクセス可能になり、セルの反復処理、値の抽出、必要に応じたデータの操作を行うことができます。

次の例は、既存のDBFファイルをAspose.Cellsに読み込み、最初のワークシートにアクセスして、セルの値を読み取る方法を示しています。

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "Data/";
const filePath = path.join(dataDir, "example.dbf");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Dbf);

const workbook = new AsposeCells.Workbook(filePath, loadOptions);

const worksheet = workbook.getWorksheets().get(0);

const cells = worksheet.getCells();

const sb = [];

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

for (let i = 0; i <= maxRow; i++)
{
    for (let j = 0; j <= maxCol; j++)
    {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        sb.push("|");
        sb.push(value);
    }
    sb.push("|");
    sb.push("\n");
}

console.log(sb.join(""));

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

[ファイルを開く]ダイアログでファイルを選択することで、Microsoft ExcelでDBFファイルを直接開くことができます。ExcelはDBFファイルをスプレッドシートとして扱い、レコードを表形式のレイアウトで表示します。これは、Aspose.Cellsで読み取りまたは書き込み後にデータをすばやく確認する場合に便利です。

{{% /alert %}}

## **DBFファイルの書き込み**

DBFファイルへのデータの書き込みは、Aspose.Cellsで他のスプレッドシート形式を保存する場合と同様のパターンに従います。Workbookを作成または読み込み、ワークシートにデータを入力し、ターゲット形式として`SaveFormat.Dbf`を指定して`Save`メソッドを呼び出します。

### Aspose.CellsでDBFファイルを書き込む

DBFファイルを作成するには、以下の手順に従います:

1. 新しい`Workbook`インスタンスを作成します。
2. `Worksheets`コレクションから最初のワークシートにアクセスします。
3. ワークシートにデータを入力します。最初の行にヘッダーを含め、後続の行にレコードを含めます。
4. ファイルパスと`SaveFormat.Dbf`をパラメータとして渡して、`Workbook.Save`メソッドを呼び出します。

次の例は、新しいDBFファイルを最初から作成する方法を示しています。フィールド型がDBF形式へのエクスポート時にどのように処理されるかを示すために、異なるデータ型(文字列、数値、日付)を含むサンプルデータがワークシートに入力されます。

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");
const fs = require("fs");

const outputDir = "C:\\Output\\";
const filePath = path.join(outputDir, "output.dbf");

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// 列ヘッダー
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// データ行 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));

// データ行 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));

// データ行 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));

// データ行 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));

// データ行 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));

// 可読性のために列幅を設定
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}

DBFファイルにデータを書き込む際は、データが形式の制限に準拠していることを確認してください。フィールド名は10文字以下であるべきで、スペースを含めることはできません。合計で4000バイトを超えるレコードは正しく保存されません。日付はYYYYMMDD形式で表現できる有効な日付値である必要があります。

{{% /alert %}}

## **データ型と書式設定の考慮事項**

Aspose.CellsとDBF形式の間でデータを転送する場合、データの整合性を確保するために、2つのシステム間でデータ型がどのようにマッピングされるかを理解することが重要です。

### セル型からDBFフィールド型へのマッピング

Aspose.Cellsのセル値は、保存時に適切なDBFフィールド型に自動的に変換されます:

- **文字列**は文字 (C) フィールドにマッピングされます。
- **数値** (整数と小数)は数値 (N) フィールドにマッピングされます。
- **日付値**は`YYYYMMDD`形式の日付 (D) フィールドにマッピングされます。
- **ブール値**は論理 (L) フィールドにマッピングされます。

### エンコーディング

DBFファイルは、作成元のアプリケーションによって異なる文字エンコーディングを使用する場合があります。Aspose.Cellsはほとんどの場合、エンコーディングを透過的に処理しますが、文字表示の問題が発生した場合は、ソースファイルのエンコーディングを確認する必要がある場合があります。

### フィールド名のルール

DBFフィールド名は以下のルールに従う必要があります:

- 最大10文字まで。
- 文字で始まる必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時に使用された大文字小文字に関係なく、大文字として保存されます。

### 出力の検証

DBFファイルを書き込んだ後、Microsoft Excelまたは任意のdBASE互換アプリケーションで開くことで結果を検証できます。データは、列ヘッダーとしてのフィールド名と、提供したデータに応じて入力されたレコードを含む表形式のレイアウトで表示されます。

## **DBFと他の形式間の変換**

Aspose.CellsでDBFファイルを読み書きする最も実用的な使用例の1つは、DBF形式とXLSX、XLS、CSVなどの最新のスプレッドシート形式間でデータを変換することです。Aspose.Cellsは幅広い形式をサポートしているため、DBFファイルを読み込んで他のサポートされている形式で再保存したり、その逆を行ったりすることが簡単にできます。

たとえば、DBFファイルを読み込み、Aspose.Cells APIを使用して書式設定や計算を適用し、最新のスプレッドシートアプリケーションで作業するユーザーに配布するために、結果をXLSXファイルとして保存できます。逆に、XLSXまたはCSVファイルからデータを取得して、レガシーシステムとの統合のためにDBF形式にエクスポートすることもできます。



{{< app/cells/assistant language="javascript" >}}