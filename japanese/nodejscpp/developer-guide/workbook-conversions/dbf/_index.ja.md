---
title: DBF ファイルの読み取りと書き込み
linktitle: DBF ファイルの読み取りと書き込み
description: Aspose.Cells for Node.js via C++ は、スプレッドシートファイルを操作するためのライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みに対応しています。この CPP では、Aspose.Cells を使用して DBF ファイルからデータをインポートしたり、DBF ファイルにデータをエクスポートしたりする方法について、ファイル形式の詳細、対応機能、手順付きの例を説明します。
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++ ライブラリ, DBF, dBASE, DBF の読み取り, DBF の書き込み, DBF のインポート, DBF のエクスポート, ファイル形式, .dbf
type: docs
weight: 200
url: /ja/nodejs-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、ワークブックを DBF 形式で保存して、レガシーデータベースアプリケーションで使用できます。
{{% /alert %}}

## **はじめに**
DBF (DataBase File) は、1980 年代初期に dBASE が公開したレガシーデータベースファイル形式です。この形式は古いものの、DBF ファイルは、会計、GIS、およびその他の専門アプリケーションで構造化データを保存するために、現在も多くの業界で広く使用されています。Aspose.Cells を使用すると、これらのレガシーファイルを、モダンな Aspose.Cells for Node.js via C++ スプレッドシートワークフローにシームレスに統合できます。
このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートするため、次の操作が可能です。
- 既存の DBF ファイルのデータを Aspose.Cells の Workbook オブジェクトにインポートし、さらに処理したり、他の形式に変換したりできます。
- ゼロから、または他のスプレッドシート形式のデータを変換して、新しい DBF ファイルを作成できます。
- DBF 形式からデータをインポートまたはエクスポートするときに、フィールド定義、データ型、レコード構造を維持できます。
DBF ファイルは Microsoft Excel などのスプレッドシートアプリケーションで直接開くこともできるため、レガシーシステムとモダンなスプレッドシートツールをつなぐ便利な形式です。

## **対応している DBF バージョンと機能**
Aspose.Cells は、DBF 形式の次のバージョンをサポートしています。
- **dBASE III** — DBF 形式における最初のバリアントであり、最も広くサポートされているバリアントです。
- **dBASE IV** — 追加のデータ型と大きなフィールドサイズをサポートする拡張バージョンです。

### 対応機能
このライブラリは、次の操作を幅広く 지원します。
- すべてのレコードとフィールド定義を保持したまま、DBF データを Workbook オブジェクトに読み込みます。
- ワークブックのデータを DBF 形式に書き戻し、dBASE 互換アプリケーション向けにエクスポートします。
- 文字、数値、日付、論理値など、DBF ファイルで一般的に使用されるデータ型を処理します。
- フィールド名、型、長さなどのフィールド定義を読み書き時に保持します。

### 制限事項と考慮点
DBF ファイルを処理する場合は、次の制約に注意してください。
- 1 ファイルあたりのフィールド数の最大値は **128** です。
- レコードサイズの最大値は **4000 バイト**です。
- フィールド名は **10 文字**以下とし、大文字で綴る必要があり、スペースを含めることはできません。
- DBF ファイル内の日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングは、作成元アプリケーションによって異なる場合があります（通常は Windows-1252 または OEM コードページです）。

## **DBF ファイルの読み取り**
Aspose.Cells を使用すると、DBF ファイルのデータを Workbook オブジェクトに簡単に読み込めます。このライブラリでは、`LoadOptions` クラスを使用してソース形式を指定し、読み込み中にデータが正しく解釈されるようにします。

### Aspose.Cells による DBF ファイルの読み取り
DBF ファイルを読み取るには、`LoadOptions` インスタンスを作成し、その `LoadFormat` プロパティを `LoadFormat.Dbf` に設定して、ファイルパスとともに `Workbook` コンストラクターに渡します。読み込み後、データには `Worksheets` コレクションからアクセスできます。その後は、セルを反復処理して値を取得したり、必要に応じてデータを操作したりできます。
次の例では、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスしてセルの値を取得する方法を示します。

```javascript
const AsposeCells = require("aspose.cells.node");
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
Excel の [開く] ダイアログで DBF ファイルを選択すると、Microsoft Excel で直接開けます。Excel は DBF ファイルをスプレッドシートとして扱い、レコードを表形式で表示します。Aspose.Cells で読み書きした後にデータをすばやく確認する場合に便利です。
{{% /alert %}}

## **DBF ファイルの書き込み**
DBF ファイルへのデータ書き込みは、Aspose.Cells で他のスプレッドシート形式を保存する場合と同様の手順で行います。Workbook を作成または読み込み、ワークシートにデータを入力してから、対象形式として `SaveFormat.Dbf` を指定して `Save` メソッドを呼び出します。

### Aspose.Cells による DBF ファイルの書き込み
DBF ファイルを作成するには、次の手順に従います。
1. 新しい `Workbook` インスタンスを作成します。
2. `Worksheets` コレクションから最初のワークシートにアクセスします。
3. 1 行目にヘッダーを、2 行目以降にレコードを配置して、ワークシートにデータを入力します。
4. ファイルパスと `SaveFormat.Dbf` を引数として `Workbook.Save` メソッドを呼び出します。
次の例では、新しい DBF ファイルをゼロから作成する方法を示します。異なるデータ型（文字列、数値、日付）を含むサンプルデータでワークシートを入力し、DBF 形式へのエクスポート時にフィールド型がどのように処理されるかを説明します。

```javascript
const AsposeCells = require("aspose.cells.node");
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
// データ行1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));
// データ行2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));
// データ行3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));
// データ行4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));
// データ行5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));
// 可読性を高めるために列幅を設定
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);
workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}
DBF ファイルにデータを書き込むときは、データが形式の制限事項に準拠していることを確認してください。フィールド名は 10 文字以下で、スペースを含めることはできません。合計 4000 バイトを超えるレコードは、正しく保存されません。日付は、YYYYMMDD 形式で表現できる有効な日付値である必要があります。
{{% /alert %}}

## **データ型と書式設定に関する考慮事項**
Aspose.Cells と DBF 形式との間でデータを転送する場合、2 つのシステムでデータ型がどのようにマッピングされるかを理解することは、データの整合性を確保するために重要です。

### セル型と DBF フィールド型のマッピング
Aspose.Cells のセル値は、保存時に適切な DBF フィールド型に自動的に変換されます。
- **文字列**は文字型 (C) フィールドにマッピングされます。
- **数値**（整数と小数）は数値型 (N) フィールドにマッピングされます。
- **日付値**は `YYYYMMDD` 形式の日付型 (D) フィールドにマッピングされます。
- **ブール値**は論理型 (L) フィールドにマッピングされます。

### エンコーディング
DBF ファイルでは、作成元アプリケーションによって文字エンコーディングが異なる場合があります。Aspose.Cells はほとんどの場合、エンコーディングを自動的に処理します。ただし、文字が正しく表示されない場合は、ソースファイルのエンコーディングを確認する必要があります。

### フィールド名の規則
DBF フィールド名は、次の規則に従う必要があります。
- 最大長は 10 文字です。
- 文字で始める必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時の大文字・小文字にかかわらず、大文字で保存されます。

### 出力の確認
DBF ファイルの書き込み後、Microsoft Excel または dBASE 互換アプリケーションで開き、結果を確認できます。データは表形式で表示され、フィールド名が列ヘッダーとして使用されます。また、レコードには指定したデータに基づく値が格納されます。

## **DBF と他の形式間の変換**
Aspose.Cells で DBF ファイルを読み書きする場合の最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などのモダンなスプレッドシート形式との間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで対応している他の形式に再保存したり、逆に他の形式を DBF に変換したりできます。

{{< app/cells/assistant language="nodejs-cpp" >}}