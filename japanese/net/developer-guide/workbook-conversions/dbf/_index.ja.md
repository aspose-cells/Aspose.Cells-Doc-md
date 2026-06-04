---
title: DBF ファイルの読み取りと書き込み
description: Aspose.Cells はスプレッドシートファイルを扱うための .NET ライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みをサポートしています。この記事では、ファイルフォーマットの詳細、サポートされている機能、ステップごとの例を含めて、Aspose.Cells を使用して DBF ファイルからデータをインポートし、データをエクスポートする方法を説明します。
keywords: Aspose.Cells, .NET library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /ja/net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells は、DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、ワークブックを DBF 形式に保存してレガシーデータベースアプリケーションで使用することができます。

{{% /alert %}}

## **はじめに**

DBF (DataBase File) は、1980 年代初頭に dBASE によって導入されたレガシーデータベースファイル形式です。この形式は古いものですが、DBF ファイルは構造化データの保存、特に会計、GIS、その他の特殊なアプリケーションにおいて、多くの業界で今でも広く使用されています。Aspose.Cells を使用すると、これらのレガシーファイルを最新の .NET スプレッドシートワークフローにシームレスに統合できます。

このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートしており、以下の機能を提供します。

- 既存の DBF ファイルから Aspose.Cells の Workbook オブジェクトにデータをインポートし、さらなる処理や他の形式への変換を行う。
- 新規に、または他のスプレッドシート形式からデータを変換して、新しい DBF ファイルを作成する。
- DBF 形式内外へのデータ転送時に、フィールド定義、データ型、レコード構造を維持する。

DBF ファイルは Microsoft Excel や他のスプレッドシートアプリケーションでも直接開くことができるため、レガシーシステムと最新のスプレッドシートツール間の便利な橋渡しとなります。

## **サポートされている DBF バージョンと機能**

Aspose.Cells は以下の DBF フォーマットのバージョンをサポートしています。

- **dBASE III** — DBF 形式のオリジナルかつ最も広くサポートされているバリアント。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョン。

### サポートされている機能

このライブラリは、以下の操作を包括的にサポートします。

- すべてのレコードとフィールド定義を保持して、DBF データを Workbook オブジェクトに読み取る。
- ワークブックデータを DBF 形式に書き戻し、dBASE 互換アプリケーションにエクスポートする。
- 文字、数値、日付、論理フィールドなど、DBF ファイルで使用される一般的なデータ型を処理する。
- 読み取り/書き込み操作時に、フィールド名、型、長さなどのフィールド定義を保持する。

### 制限事項と考慮事項

DBF ファイルを扱う際は、以下の制約事項に注意してください。

- ファイルあたりのフィールド数の最大は **128** です。
- 最大レコードサイズは **4000 バイト**です。
- フィールド名は **10 文字**以下に制限され、大文字である必要があり、スペースを含めることはできません。
- DBF ファイルの日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングはソースアプリケーションによって異なる場合があります (一般的には Windows-1252 または OEM コードページ)。

## **DBF ファイルの読み取り**

Aspose.Cells を使用すると、DBF ファイルから Workbook オブジェクトへのデータの読み込みが簡単に行えます。このライブラリは `LoadOptions` クラスを使用してソース形式を指定し、読み込みプロセス中にデータが正しく解釈されることを保証します。

### Aspose.Cells を使用して DBF ファイルを読み取る

DBF ファイルを読み取るには、`LoadOptions` インスタンスを作成し、その `LoadFormat` プロパティを `LoadFormat.Dbf` に設定して、ファイルパスと共に `Workbook` コンストラクタに渡す必要があります。読み込みが完了すると、データは `Worksheets` コレクションを介してアクセス可能になり、セルを反復処理したり、値を抽出したり、必要に応じてデータを操作したりすることができます。

次の例は、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスしてセルの値を読み取る方法を示しています。

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

[ファイルを開く] ダイアログでファイルを選択することで、DBF ファイルを Microsoft Excel で直接開くことができます。Excel は DBF ファイルをスプレッドシートとして扱い、そのレコードを表形式で表示します。これは、Aspose.Cells で読み取りまたは書き込みを行った後にデータを素早く確認するのに便利です。

{{% /alert %}}

## **DBF ファイルの書き込み**

DBF ファイルへのデータの書き込みは、Aspose.Cells を使用して他のスプレッドシート形式を保存する場合と同様のパターンに従います。Workbook を作成または読み込み、ワークシートにデータを入力してから、`Save` メソッドを呼び出す際にターゲット形式として `SaveFormat.Dbf` を指定します。

### Aspose.Cells を使用して DBF ファイルを書き込む

DBF ファイルを作成するには、以下の手順に従います。

1. 新しい `Workbook` インスタンスを作成します。
2. `Worksheets` コレクションから最初のワークシートにアクセスします。
3. 最初の行にヘッダー、以降の行にレコードを含めて、ワークシートにデータを入力します。
4. `Workbook.Save` メソッドを呼び出し、ファイルパスと `SaveFormat.Dbf` をパラメータとして渡します。

次の例は、新規に DBF ファイルを作成する方法を示しています。異なるデータ型 (文字列、数値、日付) を含むサンプルデータでワークシートを入力し、DBF 形式にエクスポートする際にフィールド型がどのように処理されるかを説明します。

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

// カラムヘッダー
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

// 可読性のために列幅を設定
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

DBF ファイルにデータを書き込む際は、データがこの形式の制限に準拠していることを確認してください。フィールド名は 10 文字以下とし、スペースを含めることはできません。合計 4000 バイトを超えるレコードは正しく保存されません。日付は YYYYMMDD 形式で表現できる有効な日付値である必要があります。

{{% /alert %}}

## **データ型と書式設定の考慮事項**

Aspose.Cells と DBF 形式の間でデータを転送する場合、2 つのシステム間でデータ型がどのようにマッピングされるかを理解することは、データの整合性を確保するために重要です。

### セルタイプから DBF フィールドタイプへのマッピング

Aspose.Cells のセル値は、保存時に自動的に適切な DBF フィールドタイプに変換されます。

- **文字列** は文字 (C) フィールドにマッピングされます。
- **数値** (整数と小数) は数値 (N) フィールドにマッピングされます。
- **日付値** は `YYYYMMDD` 形式の日付 (D) フィールドにマッピングされます。
- **ブール値** は論理 (L) フィールドにマッピングされます。

### エンコーディング

DBF ファイルは、作成したアプリケーションによって異なる文字エンコーディングを使用する場合があります。Aspose.Cells はほとんどの場合、エンコーディングを透過的に処理しますが、文字の表示に問題が発生した場合は、ソースファイルのエンコーディングを確認する必要があるかもしれません。

### フィールド名のルール

DBF フィールド名は以下のルールに従う必要があります。

- 最大長は 10 文字です。
- 文字で始まる必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時に使用された大文字小文字に関係なく、大文字として保存されます。

### 出力の検証

DBF ファイルを書き込んだ後、Microsoft Excel または dBASE 互換アプリケーションで開くことで結果を検証できます。データは、フィールド名を列ヘッダーとする表形式で表示され、提供したデータに従ってレコードが入力されます。

## **DBF と他の形式間の変換**

Aspose.Cells で DBF ファイルを読み書きする最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの最新のスプレッドシート形式の間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで、サポートされている他の任意の形式で再保存したり、その逆を行ったりすることが簡単にできます。

たとえば、DBF ファイルを読み込み、Aspose.Cells API を使用して書式設定や計算を適用し、結果を XLSX ファイルとして保存して、最新のスプレッドシートアプリケーションを使用するユーザーに配布することができます。逆に、XLSX や CSV ファイルからデータを取得して、DBF 形式にエクスポートし、レガシーシステムと統合することもできます。



{{< app/cells/assistant language="csharp" >}}