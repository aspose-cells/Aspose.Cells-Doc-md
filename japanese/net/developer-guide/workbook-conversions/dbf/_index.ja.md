---
title: DBF ファイルの読み取りと書き込み
linktitle: DBF ファイルの読み取りと書き込み
description: Aspose.Cells は、スプレッドシートファイルを扱う .NET ライブラリであり、dBASE III および dBASE IV (DBF) ファイルの読み書きに対応しています。この記事には、ファイル形式の詳細、対応機能、手順ごとの例を含め、Aspose.Cells を使用して DBF ファイルからデータをインポートし、DBF ファイルにデータをエクスポートする方法について説明します。
keywords: Aspose.Cells, .NET ライブラリ, DBF, dBASE, DBF の読み取り, DBF の書き込み, DBF のインポート, DBF のエクスポート, ファイル形式, .dbf
type: docs
weight: 200
url: /ja/net/reading-and-writing-dbf-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートしています。既存の dBASE III および dBASE IV ファイルを `Workbook` オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作できます。また、ワークブックを DBF 形式に保存して、レガシーデータベースアプリケーションで使用できます。
{{% /alert %}}

## **はじめに**
DBF (DataBase File) は、dBASE が 1980 年代初頭に導入したレガシーデータベースファイル形式です。形式は古いものの、DBF ファイルは今も、構造化データを保存するために多くの業界で広く使用されており、特に会計、GIS などの専門アプリケーションで利用されます。Aspose.Cells を使用すると、これらのレガシーファイルをモダンな .NET スプレッドシートワークフローにシームレスに統合できます。
このライブラリは DBF ファイルの読み取りと書き込みに対応しており、次のことができます。
- 既存の DBF ファイルを Aspose.Cells の `Workbook` オブジェクトにインポートし、引き続き処理を行ったり、他の形式に変換したりできます。
- 新しい DBF ファイルをゼロから作成できます。また、他のスプレッドシート形式から変換したデータを使って作成することもできます。
- DBF 形式との間でデータを転送する際に、フィールド定義、データ型、レコード構造を保持します。
DBF ファイルは Microsoft Excel などのスプレッドシートアプリケーションで直接開くこともできます。レガシーシステムとモダンなスプレッドシートツールを橋渡しする便利な手段となります。

## **サポートされている DBF のバージョンと機能**
Aspose.Cells は次の DBF 形式のバージョンをサポートしています。
- **dBASE III** — DBF 形式の原型であり、最も広くサポートされているバリアントです。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョンです。

### サポートされている機能
このライブラリは、次の操作を包括的にサポートしています。
- DBF データを `Workbook` オブジェクトに読み込み、すべてのレコードとフィールド定義を保持します。
- ワークブックのデータを DBF 形式に書き戻し、dBASE 互換アプリケーション向けにエクスポートします。
- 文字型、数値型、日付型、論理型など、DBF ファイルで使用される一般的なデータ型を処理します。
- 読み書き操作中に、フィールド名、型、長さなどのフィールド定義を保持します。

### 制限事項と考慮点
DBF ファイルを操作するときは、次の制約に注意してください。
- 1 ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト**です。
- フィールド名は **10 文字**以下で、大文字でなければならず、スペースを含めることはできません。
- DBF ファイル内の日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングは作成元アプリケーションによって異なる場合があります。通常は Windows-1252 または OEM コードページです。

## **DBF ファイルの読み取り**
Aspose.Cells を使用すると、DBF ファイルのデータを `Workbook` オブジェクトに簡単に読み込めます。ライブラリは `LoadOptions` クラスを使用してソース形式を指定し、読み込み処理中にデータが正しく解釈されるようにします。

### Aspose.Cells を使用して DBF ファイルを読み取る
DBF ファイルを読み取るには、`LoadOptions` のインスタンスを作成し、`LoadFormat` プロパティを `LoadFormat.Dbf` に設定して、ファイルパスとともに `Workbook` コンストラクターに渡します。読み込み後、データには `Worksheets` コレクションからアクセスできます。セルを反復処理して値を取得したり、必要に応じてデータを操作したりできます。
次の例では、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスして、セル値を取得する方法を示します。

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;
string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");
LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);
Workbook workbook = new Workbook(filePath, loadOptions);
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
StringBuilder sb = new StringBuilder();
int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;
for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}
Console.WriteLine(sb.ToString());
string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);
Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}
Microsoft Excel の [開く] ダイアログでファイルを選択すると、DBF ファイルを直接開くことができます。Excel は DBF ファイルをスプレッドシートとして扱い、レコードを表形式で表示します。Aspose.Cells で読み書きした後にデータをすばやく確認する場合に便利です。
{{% /alert %}}

## **DBF ファイルの書き込み**
DBF ファイルへのデータ書き込みは、Aspose.Cells でその他のスプレッドシート形式を保存する場合と同様のパターンに従います。`Workbook` を作成または読み込み、ワークシートにデータを入力してから、対象形式として `SaveFormat.Dbf` を指定して `Save` メソッドを呼び出します。

### Aspose.Cells を使用して DBF ファイルを書き込む
DBF ファイルを作成するには、次の手順に従います。
1. 新しい `Workbook` インスタンスを作成します。
2. `Worksheets` コレクションから最初のワークシートにアクセスします。
3. 1 行目にヘッダー、以降の行にレコードを含むデータをワークシートに入力します。
4. `Workbook.Save` メソッドを呼び出し、ファイルパスと `SaveFormat.Dbf` をパラメーターとして渡します。
次の例では、新しい DBF ファイルをゼロから作成する方法を説明します。文字列、数値、日付など、異なるデータ型を含むサンプルデータでワークシートにデータを入力し、DBF 形式へのエクスポート時にフィールド型がどのように処理されるかを示します。

```csharp
using System;
using System.IO;
using Aspose.Cells;
string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");
if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// 列ヘッダー
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");
// データ行 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));
// データ行 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));
// データ行 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));
// データ行 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));
// データ行 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));
// 可読性を高めるために列幅を設定
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);
workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}
DBF ファイルにデータを書き込む際は、データが形式の制限に適合していることを確認してください。フィールド名は 10 文字以下で、スペースを含めることはできません。合計で 4000 バイトを超えるレコードは正しく保存されません。日付は、YYYYMMDD 形式で表現可能な有効な日付値である必要があります。
{{% /alert %}}

## **データ型と書式設定に関する考慮点**
Aspose.Cells と DBF 形式の間でデータを転送する場合は、両方のシステム間でデータ型がどのようにマッピングされるかを理解することが、データの整合性を確保するために重要です。

### セルの型から DBF フィールド型への対応
保存時、Aspose.Cells のセル値は、適切な DBF フィールド型に自動的に変換されます。
- **文字列**は文字型 (C) フィールドにマッピングされます。
- **数値**（整数と小数）は数値型 (N) フィールドにマッピングされます。
- **日付値**は `YYYYMMDD` 形式の日付型 (D) フィールドにマッピングされます。
- **ブール値**は論理型 (L) フィールドにマッピングされます。

### エンコーディング
DBF ファイルでは、作成元アプリケーションによって異なる文字エンコーディングが使用される場合があります。Aspose.Cells は大多数の場合、エンコーディングを透過的に処理します。ただし、文字の表示に問題が発生した場合は、必要に応じてソースファイルのエンコーディングを確認してください。

### フィールド名の規則
DBF のフィールド名は、次の規則に従う必要があります。
- 最大長は 10 文字です。
- 英字で始める必要があります。
- スペースや特殊文字を含めることはできません。
- 入力で使用した大文字小文字の区別にかかわらず、大文字として保存されます。

### 出力の検証
DBF ファイルを書き込んだ後、Microsoft Excel または dBASE 互換アプリケーションで開くことで、結果を検証できます。データは表形式で表示され、フィールド名が列ヘッダーとして表示され、入力したデータに基づいてレコードが格納されます。

## **DBF とその他の形式間の変換**
Aspose.Cells で DBF ファイルを読み書きするための特に実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などのモダンなスプレッドシート形式との間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んでサポートされているその他の形式として再保存することも、その逆も簡単に実行できます。

{{< app/cells/assistant language="csharp" >}}