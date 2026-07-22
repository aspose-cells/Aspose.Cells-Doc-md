---
title: DBFファイルの読み取りと書き込み
linktitle: DBFファイルの読み取りと書き込み
description: Aspose.Cells はスプレッドシートファイルを扱う Java ライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みをサポートしています。この記事では、ファイル形式の詳細、対応機能、段階的な例を含めて、Aspose.Cells を使用して DBF ファイルからデータをインポートしたり、データをエクスポートしたりする方法について説明します。
keywords: Aspose.Cells, Java library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /ja/java/reading-and-writing-dbf-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、ワークブックを DBF 形式に保存してレガシーデータベースアプリケーションで使用することができます。

{{% /alert %}}

## **はじめに**

DBF (DataBase File) は、1980年代初頭に dBASE によって導入されたレガシーデータベースファイル形式です。この形式は古いものですが、DBF ファイルは構造化データの保存、特に会計、GIS、その他の専門用途において、多くの業界で今でも広く使用されています。Aspose.Cells を使用すると、これらのレガシーファイルを最新の Java スプレッドシートワークフローにシームレスに統合できます。

このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートしており、以下の機能を提供します。

- 既存の DBF ファイルから Aspose.Cells Workbook オブジェクトにデータをインポートし、さらに処理したり他の形式に変換したりできます。
- 新しい DBF ファイルを最初から作成したり、他のスプレッドシート形式からデータを変換して作成したりできます。
- データの入出力時にフィールド定義、データ型、レコード構造を維持します。

DBF ファイルは Microsoft Excel およびその他のスプレッドシートアプリケーションでも直接開くことができるため、レガシーシステムと最新のスプレッドシートツールとの間の便利な橋渡しとなります。

## **サポートされている DBF バージョンと機能**

Aspose.Cells は以下の DBF 形式のバージョンをサポートしています。

- **dBASE III** — DBF 形式のオリジナルかつ最も広くサポートされているバリアント。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョン。

### サポートされている機能

このライブラリは、以下の操作を包括的にサポートします。

- すべてのレコードとフィールド定義を保持したまま、DBF データを Workbook オブジェクトに読み取ります。
- dBASE 互換アプリケーションへのエクスポートのために、ワークブックデータを DBF 形式に書き戻します。
- 文字、数値、日付、論理フィールドなど、DBF ファイルで使用される一般的なデータ型を処理します。
- 読み取り/書き込み操作中に、フィールド名、型、長さなどのフィールド定義を保持します。

### 制限事項と考慮事項

DBF ファイルを扱う際は、以下の制約に留意してください。

- ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト**です。
- フィールド名は **10 文字**までに制限され、大文字である必要があり、スペースを含めることはできません。
- DBF ファイルの日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングは、ソースアプリケーションによって異なる場合があります (一般的には Windows-1252 または OEM コードページ)。

## **DBF ファイルの読み取り**

Aspose.Cells を使用すると、DBF ファイルから Workbook オブジェクトへのデータの読み込みが簡単に行えます。このライブラリは `LoadOptions` クラスを使用してソース形式を指定し、読み込みプロセス中にデータが正しく解釈されるようにします。

### Aspose.Cells を使用した DBF ファイルの読み取り

DBF ファイルを読み取るには、`LoadOptions` インスタンスを作成し、その `LoadFormat` プロパティを `LoadFormat.Dbf` に設定して、ファイルパスとともに `Workbook` コンストラクタに渡す必要があります。読み込みが完了すると、データは `getWorksheets()` コレクションを介してアクセス可能になり、セルの反復処理、値の抽出、必要に応じたデータの操作を行うことができます。

次の例は、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスしてセルの値を読み取る方法を示しています。

```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "Data/";
String filePath = new File(new File(dataDir), "example.dbf").getPath();

LoadOptions loadOptions = new LoadOptions(LoadFormat.DBF);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

StringBuilder sb = new StringBuilder();

int maxRow = cells.getMaxDataRow();
int maxCol = cells.getMaxDataColumn();

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells.get(i, j);
        String value = cell.getStringValue();
        sb.append("|").append(value);
    }
    sb.append("|").append(System.lineSeparator());
}

System.out.println(sb.toString());

String outputPath = new File(new File(dataDir), "output.xlsx").getPath();
workbook.save(outputPath, SaveFormat.XLSX);

System.out.println("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

[ファイルを開く] ダイアログでファイルを選択することで、Microsoft Excel で DBF ファイルを直接開くことができます。Excel は DBF ファイルをスプレッドシートとして扱い、そのレコードをテーブルレイアウトで表示します。これは、Aspose.Cells で読み取りまたは書き込みを行った後にデータをすばやく確認する場合に便利です。

{{% /alert %}}

## **DBF ファイルの書き込み**

DBF ファイルへのデータの書き込みは、Aspose.Cells での他のスプレッドシート形式の保存と同様のパターンに従います。Workbook を作成または読み込み、ワークシートにデータを入力してから、ターゲット形式として `SaveFormat.Dbf` を指定して `save` メソッドを呼び出します。

### Aspose.Cells を使用した DBF ファイルの書き込み

DBF ファイルを作成するには、次の手順に従います。

1. 新しい `Workbook` インスタンスを作成します。
2. `getWorksheets()` コレクションから最初のワークシートにアクセスします。
3. ワークシートにデータを入力します (最初の行にヘッダー、後続の行にレコードを含めます)。
4. ファイルパスと `SaveFormat.Dbf` をパラメータとして `Workbook.save` メソッドを呼び出します。

次の例は、新しい DBF ファイルを最初から作成する方法を示しています。DBF 形式にエクスポートする際にフィールド型がどのように処理されるかを示すため、文字列、数値、日付など、さまざまなデータ型を含むサンプルデータがワークシートに入力されます。

```java
import com.aspose.cells.*;
import java.io.File;
import java.util.GregorianCalendar;

String outputDir = "C:\\Output\\";
String filePath = new File(new File(outputDir), "output.dbf").getPath();

if (!new File(outputDir).exists())
{
    new File(outputDir).mkdirs();
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();

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
cells.get(1, 4).putValue(new GregorianCalendar(2020, 2, 15).getTime());

// データ行 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new GregorianCalendar(2019, 6, 22).getTime());

// データ行 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new GregorianCalendar(2021, 0, 10).getTime());

// データ行 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new GregorianCalendar(2018, 10, 5).getTime());

// データ行 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new GregorianCalendar(2022, 4, 30).getTime());

// 可読性を向上させるために列幅を設定
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, SaveFormat.DBF);
```

{{% alert color="primary" %}}

DBF ファイルにデータを書き込む際は、データが形式の制限に準拠していることを確認してください。フィールド名は 10 文字以内とし、スペースを含めないでください。合計で 4000 バイトを超えるレコードは正しく保存されません。日付は YYYYMMDD 形式で表現できる有効な日付値である必要があります。

{{% /alert %}}

## **データ型と書式設定の考慮事項**

Aspose.Cells と DBF 形式の間でデータを転送する場合、2 つのシステム間でデータ型がどのようにマッピングされるかを理解することは、データの整合性を確保するために重要です。

### セル型から DBF フィールド型へのマッピング

Aspose.Cells のセル値は、保存時に適切な DBF フィールド型に自動的に変換されます。

- **文字列** は文字 (C) フィールドにマッピングされます。
- **数値** (整数と小数) は数値 (N) フィールドにマッピングされます。
- **日付値** は `YYYYMMDD` 形式の日付 (D) フィールドにマッピングされます。
- **ブール値** は論理 (L) フィールドにマッピングされます。

### エンコーディング

DBF ファイルは、作成元のアプリケーションによって異なる文字エンコーディングを使用する場合があります。Aspose.Cells はほとんどの場合エンコーディングを透過的に処理しますが、文字の表示に関する問題が発生した場合は、ソースファイルのエンコーディングを確認する必要があるかもしれません。

### フィールド名の規則

DBF フィールド名は次の規則に従う必要があります。

- 最大 10 文字。
- 文字で始まる必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時に使用された大文字小文字にかかわらず、大文字として保存されます。

### 出力の検証

DBF ファイルを書き込んだ後、Microsoft Excel または任意の dBASE 互換アプリケーションで開くことで結果を検証できます。データは、列ヘッダーとしてフィールド名が配置され、提供したデータに従ってレコードが入力された表形式で表示されるはずです。

## **DBF と他の形式の間の変換**

Aspose.Cells を使用して DBF ファイルを読み書きする最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの最新のスプレッドシート形式の間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで他のサポートされている任意の形式で再保存したり、その逆を行ったりすることが簡単にできます。

たとえば、DBF ファイルを読み取り、Aspose.Cells API を使用して書式設定や計算を適用してから、結果を XLSX ファイルとして保存することで、最新のスプレッドシートアプリケーションを使用するユーザーに配布できます。逆に、XLSX または CSV ファイルからデータを取得して DBF 形式にエクスポートし、レガシーシステムと統合することもできます。



{{< app/cells/assistant language="java" >}}