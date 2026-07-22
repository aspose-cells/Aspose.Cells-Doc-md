---
title: DBF ファイルの読み取りと書き込み
linktitle: DBF ファイルの読み取りと書き込み
description: Aspose.Cells はスプレッドシートファイルを操作するための Node.js ライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みをサポートします。この記事では、ファイル形式の詳細、サポートされている機能、段階的な例を含む、Aspose.Cells を使用して DBF ファイルからデータをインポートし、データをエクスポートする方法について説明します。
keywords: Aspose.Cells, Node.js ライブラリ, DBF, dBASE, DBF 読み取り, DBF 書き込み, DBF インポート, DBF エクスポート, ファイル形式, .dbf, Java
type: docs
weight: 200
url: /ja/nodejs-java/reading-and-writing-dbf-files/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、ワークブックを DBF 形式に保存してレガシーデータベースアプリケーションで使用することができます。

{{% /alert %}}

## **はじめに**

DBF (DataBase File) は、1980年代初頭に dBASE によって導入されたレガシーデータベースファイル形式です。この形式は古いものですが、DBF ファイルは構造化データの保存、特に会計、GIS、その他の特殊なアプリケーションにおいて、多くの業界で現在も広く使用されています。Aspose.Cells を使用すると、これらのレガシーファイルを最新の Node.js スプレッドシートワークフローにシームレスに統合できます。

このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートしており、以下のことが可能になります:

- 既存の DBF ファイルから Aspose.Cells Workbook オブジェクトにデータをインポートし、さらに処理したり他の形式に変換したりできます。
- 新しい DBF ファイルを最初から作成したり、他のスプレッドシート形式からデータを変換して作成したりできます。
- DBF 形式との間でデータを転送する際に、フィールド定義、データ型、レコード構造を維持します。

DBF ファイルは Microsoft Excel や他のスプレッドシートアプリケーションで直接開くこともできるため、レガシーシステムと最新のスプレッドシートツール間の便利な橋渡しとなります。

## **サポートされている DBF バージョンと機能**

Aspose.Cells は以下の DBF 形式バージョンをサポートしています:

- **dBASE III** — DBF 形式の元祖であり、最も広くサポートされているバリアントです。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョンです。

### サポートされている機能

このライブラリは、以下の操作を包括的にサポートします:

- すべてのレコードとフィールド定義を保持して、DBF データを Workbook オブジェクトに読み取ります。
- dBASE 互換アプリケーションへのエクスポートのために、ワークブックデータを DBF 形式に書き戻します。
- 文字、数値、日付、論理フィールドなど、DBF ファイルで使用される一般的なデータ型を処理します。
- 読み取り/書き込み操作中に、フィールド名、型、長さなどのフィールド定義を保持します。

### 制限事項と考慮事項

DBF ファイルを扱う際は、以下の制約事項に留意してください:

- ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト** です。
- フィールド名は **10 文字** までに制限され、大文字でなければならず、スペースを含めることはできません。
- DBF ファイルの日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングはソースアプリケーションによって異なる場合があります (一般的には Windows-1252 または OEM コードページ)。

## **DBF ファイルの読み取り**

Aspose.Cells を使用すると、DBF ファイルから Workbook オブジェクトへのデータの読み込みが簡単に行えます。このライブラリは `LoadOptions` クラスを使用してソース形式を指定し、読み込みプロセス中にデータが正しく解釈されるようにします。

### Aspose.Cells を使用した DBF ファイルの読み取り

DBF ファイルを読み取るには、`LoadFormat.Dbf` で設定された `LoadOptions` インスタンスを作成し、それをファイルパスとともに `Workbook` コンストラクタに渡す必要があります。一度読み込まれると、データは `Worksheets` コレクションを介してアクセス可能になり、セルを反復処理したり、値を抽出したり、必要に応じてデータを操作したりできます。

次の例は、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスしてセルの値を読み取る方法を示しています。

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "path/to/data";
const filePath = path.join(dataDir, "input.dbf");

// DBFファイルを読み込む
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

const lines = [];
for (let i = 0; i <= maxRow; i++) {
    let row = "";
    for (let j = 0; j <= maxCol; j++) {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        row += "|" + value;
    }
    row += "|" + "\n";
    lines.push(row);
}

console.log(lines.join(""));

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

[ファイルを開く] ダイアログでファイルを選択することで、DBF ファイルを Microsoft Excel で直接開くことができます。Excel は DBF ファイルをスプレッドシートとして扱い、そのレコードを表形式レイアウトで表示します。これは、Aspose.Cells で DBF ファイルを読み取ったり書き込んだりした後に、データをすばやく確認するのに便利です。

{{% /alert %}}

## **DBF ファイルの書き込み**

DBF ファイルへのデータの書き込みは、Aspose.Cells で他のスプレッドシート形式を保存するのと類似したパターンに従います。Workbook を作成または読み込み、ワークシートにデータを入力し、`save` メソッドを呼び出す際に `SaveFormat.Dbf` をターゲット形式として指定します。

### Aspose.Cells を使用した DBF ファイルの書き込み

DBF ファイルを作成するには、以下の手順に従います:

1. 新しい `Workbook` インスタンスを作成します。
2. `Worksheets` コレクションから最初のワークシートにアクセスします。
3. 最初の行にヘッダー、その後の行にレコードを含めて、ワークシートにデータを入力します。
4. `Workbook.save` メソッドを呼び出し、ファイルパスと `SaveFormat.Dbf` をパラメータとして渡します。

次の例は、ゼロから新しい DBF ファイルを作成する方法を示しています。異なるデータ型 (文字列、数値、日付) を含むサンプルデータでワークシートを入力し、DBF 形式にエクスポートする際にフィールド型がどのように処理されるかを説明します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

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

DBF ファイルにデータを書き込む際は、データが形式の制限に準拠していることを確認してください。フィールド名は 10 文字以下とし、スペースを含めることはできません。合計で 4000 バイトを超えるレコードは正しく保存されません。日付は YYYYMMDD 形式で表現できる有効な日付値である必要があります。

{{% /alert %}}

## **データ型と書式設定の考慮事項**

Aspose.Cells と DBF 形式の間でデータを転送する場合、データの整合性を確保するために、2 つのシステム間でデータ型がどのように対応するかを理解することが重要です。

### セル型から DBF フィールド型へのマッピング

Aspose.Cells のセル値は、保存時に適切な DBF フィールド型に自動的に変換されます:

- **文字列** は文字 (C) フィールドにマッピングされます。
- **数値** (整数と小数) は数値 (N) フィールドにマッピングされます。
- **日付値** は `YYYYMMDD` 形式の日付 (D) フィールドにマッピングされます。
- **ブール値** は論理 (L) フィールドにマッピングされます。

### エンコーディング

DBF ファイルは、作成したアプリケーションによって異なる文字エンコーディングを使用する場合があります。Aspose.Cells はほとんどの場合、エンコーディングを透過的に処理しますが、文字の表示問題が発生した場合は、ソースファイルのエンコーディングを確認する必要があるかもしれません。

### フィールド名のルール

DBF フィールド名は以下のルールに従う必要があります:

- 最大 10 文字まで。
- 文字で始まる必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時に使用された大文字小文字に関係なく、大文字として保存されます。

### 出力の検証

DBF ファイルを書き込んだ後、Microsoft Excel または任意の dBASE 互換アプリケーションでファイルを開いて結果を検証できます。データは、フィールド名を列ヘッダーとする表形式のレイアウトで、提供したデータに従ってレコードが入力された状態で表示されるはずです。

## **DBF と他の形式の間の変換**

Aspose.Cells で DBF ファイルを読み書きする最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの最新のスプレッドシート形式の間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで他のサポートされている形式で再保存したり、その逆を行ったりすることが簡単にできます。

たとえば、DBF ファイルを読み込み、Aspose.Cells API を使用して書式設定や計算を適用し、その結果を最新のスプレッドシートアプリケーションを使用するユーザーに配布するために XLSX ファイルとして保存できます。逆に、XLSX や CSV ファイルからデータを取得し、レガシーシステムとの統合のために DBF 形式にエクスポートすることもできます。



{{< app/cells/assistant language="javascript" >}}