---
title: DBF ファイルの読み取りと書き込み
linktitle: DBF ファイルの読み取りと書き込み
description: Aspose.Cells は、スプレッドシートファイルを操作するための Java ライブラリであり、dBASE III および dBASE IV (DBF) ファイルの読み取りと書き込みに対応しています。この記事では、ファイル形式の詳細、対応機能、段階的な例を含めて、Aspose.Cells を使用して DBF ファイルからデータをインポートし、DBF ファイルへデータをエクスポートする方法を説明します。
keywords: Aspose.Cells, Java ライブラリ, DBF, dBASE, DBF の読み取り, DBF の書き込み, DBF のインポート, DBF のエクスポート, ファイル形式, .dbf
type: docs
weight: 200
url: /ja/java/reading-and-writing-dbf-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートしています。既存の dBASE III および dBASE IV ファイルを `Workbook` オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、ワークブックを DBF 形式で保存して、レガシーデータベースアプリケーションで使用できます。
{{% /alert %}}

## **はじめに**
DBF (データベースファイル) は、1980 年代初頭に dBASE によって導入された従来のデータベースファイル形式です。古い形式にもかかわらず、DBF ファイルはいまだ多くの分野で構造化されたデータの保存に使用されており、特に会計、GIS などの特殊なアプリケーションで広く利用されています。Aspose.Cells を使用すると、これらのレガシーファイルを現代の Java ベースのスプレッドシートワークフローにシームレスに統合できます。
ライブラリは DBF ファイルの読み取りと書き込みの両方をサポートし、次の操作が可能です。
- 既存の DBF ファイルから Aspose.Cells の `Workbook` オブジェクトへデータをインポートし、引き続き処理を行ったり、他の形式に変換したりできます。
- 新規の DBF ファイルを作成したり、他のスプレッドシート形式のデータを変換して DBF ファイルを作成したりできます。
- DBF 形式とのデータ交換において、フィールド定義、データ型、レコード構造を維持できます。
DBF ファイルは Microsoft Excel などのスプレッドシートアプリケーションでも直接開くできるため、レガシーシステムと現代のスプレッドシートツールの間をつなぐ便利な手段になります。

## **対応する DBF バージョンと機能**
Aspose.Cells は、次の DBF 形式バージョンをサポートしています。
- **dBASE III** — DBF 形式の最初のバージョンであり、最も広くサポートされている種類です。
- **dBASE IV** — 追加のデータ型と大きなフィールドサイズに対応する拡張バージョンです。

### 対応機能
ライブラリは、次の操作を包括的にサポートしています。
- すべてのレコードとフィールド定義を保持したまま、DBF データを `Workbook` オブジェクトに読み込みます。
- ワークブックのデータを DBF 形式で保存し、dBASE 互換アプリケーション向けにエクスポートします。
- 文字、数値、日付、論理フィールドなど、DBF ファイルで使用される一般的なデータ型を処理します。
- 読み取りおよび書き込み操作中に、フィールド名、型、長さなどのフィールド定義を保持します。

### 制限事項と考慮点
DBF ファイルを扱う際は、次の制約に注意してください。
- 1 ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト**です。
- フィールド名は最大 **10 文字**とし、大文字である必要があります。また、スペースを含めることはできません。
- DBF ファイル内の日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングは、ファイルを作成したアプリケーションによって異なる場合があります。一般的には Windows-1252 または OEM コードページが使用されます。

## **DBF ファイルの読み取り**
Aspose.Cells を使用すると、DBF ファイルを `Workbook` オブジェクトに簡単に読み込めます。ライブラリは `LoadOptions` クラスを使用してソース形式を指定し、読み込み中にデータが正しく解釈されるようにします。

### Aspose.Cells を使用した DBF ファイルの読み取り
DBF ファイルを読み込むには、`LoadOptions` インスタンスを作成し、`LoadFormat` プロパティを `LoadFormat.Dbf` に設定して、ファイルパスとともに `Workbook` コンストラクターに渡します。読み込み後、データには `getWorksheets()` コレクションからアクセスできます。このコレクション内でセルを反復処理し、値を取得したり、必要に応じてデータを操作したりできます。
次の例では、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスして、セルの値を取得する方法を示します。

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
[開く] ダイアログでファイルを選択すると、DBF ファイルを Microsoft Excel で直接開けます。Excel は DBF ファイルをスプレッドシートとして扱い、そのレコードを表形式で表示します。Aspose.Cells でデータを読み書きした後に、データをすばやく確認するのに便利です。
{{% /alert %}}

## **DBF ファイルの書き込み**
Aspose.Cells で他のスプレッドシート形式を保存する場合と同じパターンで、DBF ファイルにデータを書き込みます。`Workbook` を作成または読み込み、ワークシートにデータを入力して、対象形式として `SaveFormat.Dbf` を指定し、`save` メソッドを呼び出します。

### Aspose.Cells を使用した DBF ファイルの書き込み
DBF ファイルを作成するには、次の手順に従います。
1. 新しい `Workbook` インスタンスを作成します。
2. `getWorksheets()` コレクションから最初のワークシートにアクセスします。
3. 1 行目にヘッダーを、後続の行にレコードを配置するなど、ワークシートにデータを入力します。
4. ファイルパスと `SaveFormat.Dbf` をパラメーターとして、`Workbook.save` メソッドを呼び出します。
次の例では、新規の DBF ファイルをゼロから作成する方法を示します。異なるデータ型（文字列、数値、日付）を含むサンプルデータでワークシートを入力し、DBF 形式へのエクスポート時にフィールド型がどのように処理されるかを示します。

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
DBF ファイルにデータを書き込む際は、データがその形式の制限事項に適合していることを確認してください。フィールド名は 10 文字以下、かつスペースを含めることはできません。合計で 4000 バイトを超えるレコードは正しく保存されません。日付は YYYYMMDD 形式で表現可能な有効な日付値である必要があります。
{{% /alert %}}

## **データ型と書式設定に関する考慮事項**
Aspose.Cells と DBF 形式の間でデータを転送する場合、2 つのシステム間でのデータ型のマッピングを理解することが、データの整合性を確保するために重要です。

### セル型から DBF フィールド型へのマッピング
Aspose.Cells のセル値は、保存時に適切な DBF フィールド型へ自動的に変換されます。
- **文字列**は文字 (C) フィールドにマッピングされます。
- **数値**（整数と小数）は数値 (N) フィールドにマッピングされます。
- **日付値**は `YYYYMMDD` 形式の日付 (D) フィールドにマッピングされます。
- **ブール値**は論理 (L) フィールドにマッピングされます。

### エンコーディング
DBF ファイルでは、ファイルを作成したアプリケーションによって異なる文字エンコーディングが使用されることがあります。Aspose.Cells はほとんどの場合、エンコーディングを透過的に処理しますが、文字化けが発生する場合は、ソースファイルのエンコーディングを確認する必要があります。

### フィールド名の規則
DBF のフィールド名は、次の規則に従う必要があります。
- 最大 10 文字です。
- 英字で始める必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時の大文字・小文字の区別にかかわらず、常に大文字で保存されます。

### 出力の検証
DBF ファイルを書き込んだ後、Microsoft Excel または dBASE 互換アプリケーションを開いて結果を確認できます。データは表形式で表示され、フィールド名が列見出しとして表示され、指定したデータに基づいてレコードが格納されます。

## **DBF とその他の形式間の変換**
Aspose.Cells を使用して DBF ファイルを読み書きする最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの現代のスプレッドシート形式との間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで別のサポートされている形式に保存し直したり、その逆の操作を行ったりできます。

{{< app/cells/assistant language="java" >}}