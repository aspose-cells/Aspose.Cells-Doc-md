---
title: DBF ファイルの読み取りと書き込み
linktitle: DBF ファイルの読み取りと書き込み
description: Aspose.Cells は、スプレッドシートファイルを操作するための Java 経由の Python ライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みに対応しています。この_nullable에서는、Aspose.Cells を使用して DBF ファイルからデータをインポートしたり、DBF ファイルにデータをエクスポートしたりする方法について、ファイル形式の詳細、対応機能、段階的な例を説明します。
keywords: Aspose.Cells, Java 経由の Python ライブラリ, DBF, dBASE, DBF の読み取り, DBF の書き込み, DBF のインポート, DBF のエクスポート, ファイル形式, .dbf
type: docs
weight: 200
url: /ja/python-java/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、DBF (dBASE) ファイルの読み取りと書き込みをフルサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、リッチな Aspose.Cells API を使用してデータを操作し、Workbook を DBF 形式で保存してレガシーデータベースアプリケーションで使用できます。
{{% /alert %}}

## **Introduction**
DBF (DataBase File) は、1980 年代初頭に dBASE が導入したレガシーデータベースファイル形式です。形式が古いにもかかわらず、DBF ファイルは現在も多くの業界で広く使用されており、特に会計、GIS、その他の専門アプリケーションで構造化データを保存するために使用されています。Aspose.Cells を使用すると、これらのレガシーファイルを現代の Java 経由の Python スプレッドシートワークフローにシームレスに統合できます。
このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートしており、次の操作が可能です。
- 既存の DBF ファイルから Aspose.Cells の Workbook オブジェクトにデータをインポートし、さらに処理したり、他の形式に変換できます。
- 新しい DBF ファイルを最初から作成したり、他のスプレッドシート形式から変換したデータから作成したりできます。
- DBF 形式との間でデータを転送する際に、フィールド定義、データ型、レコード構造を維持できます。
DBF ファイルは Microsoft Excel などのスプレッドシートアプリケーションでも直接開けるため、レガシーシステムと現代のスプレッドシートツールをつなぐための便利な手段となります。

## **Supported DBF Versions and Features**
Aspose.Cells は次の DBF 形式バージョンをサポートしています。
- **dBASE III** — DBF 形式のオリジナルであり、最も広くサポートされているバリアントです。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョンです。

### **Supported Features**
このライブラリは、次の操作を包括的にサポートします。
- すべてのレコードとフィールド定義を維持しながら、DBF データを Workbook オブジェクトに読み込みます。
- dBASE 互換アプリケーションでエクスポート 있도록、ワークブックのデータを DBF 形式に書き戻します。
- 文字、数値、日付、論理フィールドなど、DBF ファイルで使用される一般的なデータ型を処理します。
- 読み取り・書き込み操作中に、フィールド名、型、長さなどのフィールド定義を保持します。

### **Limitations and Considerations**
DBF ファイルを扱うときは、次の制限事項に注意してください。
- 1 ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト**です。
- フィールド名は **10 文字**までとし、大文字である必要があり、スペースを含めることはできません。
- DBF ファイル内の日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングは、ソースアプリケーションによって異なる場合があります（通常は Windows-1252 または OEM コードページです）。

## **Reading a DBF File**
Aspose.Cells を使用すると、DBF ファイルのデータを Workbook オブジェクトに簡単に読み込めます。このライブラリでは、`LoadOptions` クラスを使用してソース形式を指定し、読み込み中にデータが正しく解釈されるようにします。

### **Reading a DBF File with Aspose.Cells**
DBF ファイルを読み取るには、`LoadOptions` インスタンスを作成し、その `LoadFormat` プロパティを `LoadFormat.DBF` に設定して、ファイルパスとともに `Workbook` コンストラクターに渡します。読み込み後、データには `Worksheets` コレクションからアクセスできます。セルを反復処理して値を取得したり、必要なようにデータを操作したりできます。
次の例では、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスして、セル値を取得します。

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat
dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")
loadOptions = LoadOptions(LoadFormat.DBF)
workbook = Workbook(filePath, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
sb = []
maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()
for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")
print("".join(sb))
outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.XLSX)
print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
［開く］ダイアログでファイルを選択すると、DBF ファイルを Microsoft Excel で直接開けます。Excel は DBF ファイルをスプレッドシートとして扱い、レコードを表形式で表示します。Aspose.Cells で読み書きした後にデータを迅速に確認する場合に便利です。
{{% /alert %}}

## **Writing a DBF File**
DBF ファイルへのデータ書き込みは、Aspose.Cells で他のスプレッドシート形式を保存する場合と同じパターンで行います。Workbook を作成または読み込み、ワークシートにデータを入力して、対象形式として `SaveFormat.DBF` を指定し、`Save` メソッドを呼び出します。

### **Writing a DBF File with Aspose.Cells**
DBF ファイルを作成するには、次の手順に従います。
1. 新しい `Workbook` インスタンスを作成します。
2. `Worksheets` コレクションから最初のワークシートにアクセスします。
3. 最初の行にヘッダーを含め、後続の行にレコードを配置して、ワークシートにデータを入力します。
4. `Workbook.save` メソッドを呼び出し、ファイルパスと `SaveFormat.DBF` をパラメーターとして渡します。
次の例では、新しい DBF ファイルを最初から作成します。異なるデータ型（文字列、数値、日付）を含むサンプルデータでワークシートを入力し、DBF 形式へのエクスポート時にフィールド型がどのように処理されるかを示します。

```python
import jpype
import os
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju
outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")
if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Column headers
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")
# Data row 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))
# Data row 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))
# Data row 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))
# Data row 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))
# Data row 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))
# Set column widths for better readability
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)
workbook.save(filePath, SaveFormat.DBF)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
DBF ファイルにデータを書き込む際は、データがその形式の制限事項を満たしていることを確認してください。フィールド名は 10 文字以下とし、スペースを含めないでください。合計で 4000 バイトを超えるレコードは正しく保存されません。日付は、YYYYMMDD 形式で表せる有効な日付値にする必要があります。
{{% /alert %}}

## **Data Type and Formatting Considerations**
Aspose.Cells と DBF 形式の間でデータを転送する場合、2 つのシステム間のデータ型のマッピングを理解することが、データ整合性を確保するために重要です。

### **Cell Types to DBF Field Types**
保存すると、Aspose.Cells のセル値は適切な DBF フィールド型に自動的に変換されます。
- **文字列**は文字 (C) フィールドに対応します。
- **数値**（整数と小数）は数値 (N) フィールドに対応します。
- **日付値**は `YYYYMMDD` 形式の日付 (D) フィールドに対応します。
- **ブール値**は論理 (L) フィールドに対応します。

### **Encoding**
DBF ファイルは、作成したアプリケーションによって異なる文字エンコーディングを使用することがあります。Aspose.Cells はほとんどの場合、エンコーディングを自動的に処理しますが、文字が正しく表示されない場合は、ソースファイルのエンコーディングを確認する必要があります。

### **Field Name Rules**
DBF のフィールド名は、次の規則に従う必要があります。
- 最大 10 文字。
- 文字で始める必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時の大文字と小文字の指定にかかわらず、大文字として保存されます。

### **Verifying the Output**
DBF ファイルを書き込んだ後、Microsoft Excel または dBASE 互換アプリケーションで開くことで、結果を確認できます。データは、列ヘッダーとしてフィールド名が配置され、入力したデータに基づいてレコードが設定された表形式で表示されるはずです。

## **Converting Between DBF and Other Formats**
Aspose.Cells を使用して DBF ファイルを読み書きする最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの現代のスプレッドシート形式間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んでサポートされている他の形式で再保存したり、その逆も簡単に実行できます。

{{< app/cells/assistant language="python" >}}