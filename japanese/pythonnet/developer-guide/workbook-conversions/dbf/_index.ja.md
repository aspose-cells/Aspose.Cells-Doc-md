---
title: DBF ファイルの読み取りと書き込み
linktitle: DBF ファイルの読み取りと書き込み
description: Aspose.Cells は、Python via .NET でスプレッドシートファイルを扱うためのライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みをサポートしています。この記事では、Aspose.Cells を使用して DBF ファイルからデータをインポートしたり、DBF ファイルにデータをエクスポートしたりする方法について、ファイル形式の詳細、サポートされる機能、ステップバイステップの例とともに説明します。
keywords: Aspose.Cells, Python via .NET library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /ja/python-net/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、ワークブックを DBF 形式に保存してレガシーデータベースアプリケーションで使用することができます。

{{% /alert %}}

## **はじめに**

DBF (DataBase File) は、1980 年代初頭に dBASE によって導入されたレガシーデータベースファイル形式です。この形式は古いものですが、DBF ファイルは多くの業界、特に会計、GIS、その他の専門的なアプリケーションで構造化データを保存するために現在でも広く使用されています。Aspose.Cells を使用すると、これらのレガシーファイルを最新の Python via .NET スプレッドシートワークフローにシームレスに統合できます。

このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートしており、以下のことが可能になります:

- 既存の DBF ファイルから Aspose.Cells Workbook オブジェクトにデータをインポートし、さらに処理したり他の形式に変換したりできます。
- 新しい DBF ファイルを最初から作成したり、他のスプレッドシート形式からデータを変換したりできます。
- DBF 形式内外にデータを転送する際に、フィールド定義、データ型、レコード構造を維持します。

DBF ファイルは Microsoft Excel やその他のスプレッドシートアプリケーションで直接開くこともできるため、レガシーシステムと最新のスプレッドシートツール間の便利な橋渡しとなります。

## **サポートされる DBF のバージョンと機能**

Aspose.Cells は以下の DBF 形式のバージョンをサポートしています:

- **dBASE III** — DBF 形式のオリジナルであり、最も広くサポートされているバリアントです。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョンです。

### サポートされる機能

このライブラリは、以下の操作を包括的にサポートします:

- すべてのレコードとフィールド定義を保持した DBF データの Workbook オブジェクトへの読み取り。
- dBASE 互換アプリケーションへのエクスポートのための、ワークブックデータの DBF 形式への書き戻し。
- 文字、数値、日付、論理フィールドなど、DBF ファイルで使用される一般的なデータ型の処理。
- 読み取り/書き込み操作中における、フィールド名、タイプ、長さなどのフィールド定義の保持。

### 制限事項と考慮事項

DBF ファイルを扱う際は、以下の制約事項を念頭に置いてください:

- ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト** です。
- フィールド名は **10 文字** までに制限され、大文字でなければならず、スペースを含めることはできません。
- DBF ファイルの日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングはソースアプリケーションによって異なる場合があります (一般的には Windows-1252 または OEM コードページ)。

## **DBF ファイルの読み取り**

Aspose.Cells を使用すると、DBF ファイルから Workbook オブジェクトへのデータ読み込みを簡単に行うことができます。このライブラリは `LoadOptions` クラスを使用してソース形式を指定し、読み込みプロセス中にデータが正しく解釈されるようにします。

### Aspose.Cells を使用した DBF ファイルの読み取り

DBF ファイルを読み取るには、`LoadOptions` インスタンスを作成し、その `load_format` プロパティを `LoadFormat.DBF` に設定して、ファイルパスとともに `Workbook` コンストラクタに渡す必要があります。読み込みが完了すると、データは `worksheets` コレクションを介してアクセス可能になり、セルを反復処理したり、値を抽出したり、必要に応じてデータを操作したりできます。

次の例は、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスしてセルの値を読み取る方法を示しています。

```python
import os
import aspose.cells as ac

data_dir = "Data/"
file_path = os.path.join(data_dir, "example.dbf")

load_options = ac.LoadOptions(ac.LoadFormat.DBF)

workbook = ac.Workbook(file_path, load_options)

worksheet = workbook.worksheets[0]

cells = worksheet.cells

lines = []

max_row = cells.max_data_row
max_col = cells.max_data_column

for i in range(max_row + 1):
    line_parts = []
    for j in range(max_col + 1):
        cell = cells[i, j]
        value = cell.string_value
        line_parts.append("|" + value)
    line_parts.append("|")
    lines.append("".join(line_parts))

result = "\n".join(lines) + ("\n" if lines else "")
print(result)

output_path = os.path.join(data_dir, "output.xlsx")
workbook.save(output_path, ac.SaveFormat.XLSX)

print("DBF file loaded successfully. Converted XLSX saved at: " + output_path)
```

{{% alert color="primary" %}}

[ファイルを開く] ダイアログでファイルを選択することで、Microsoft Excel で DBF ファイルを直接開くことができます。Excel は DBF ファイルをスプレッドシートとして扱い、そのレコードをテーブル形式で表示します。これは、Aspose.Cells で読み取りまたは書き込みを行った後にデータをすばやく確認するのに便利です。

{{% /alert %}}

## **DBF ファイルの書き込み**

DBF ファイルへのデータ書き込みは、Aspose.Cells での他のスプレッドシート形式の保存と同様のパターンに従います。Workbook を作成または読み込み、ワークシートにデータを入力し、ターゲット形式として `SaveFormat.DBF` を指定して `save` メソッドを呼び出します。

### Aspose.Cells を使用した DBF ファイルの書き込み

DBF ファイルを作成するには、以下の手順に従います:

1. 新しい `Workbook` インスタンスを作成します。
2. `worksheets` コレクションから最初のワークシートにアクセスします。
3. ワークシートにデータを入力します (最初の行にヘッダー、以降の行にレコードを含めます)。
4. ファイルパスと `SaveFormat.DBF` をパラメータとして渡し、`Workbook.save` メソッドを呼び出します。

次の例は、新しい DBF ファイルを最初から作成する方法を示しています。異なるデータ型 (文字列、数値、日付) を含むサンプルデータをワークシートに入力し、DBF 形式へのエクスポート時にフィールド型がどのように処理されるかを説明します。

```python
from datetime import datetime

outputDir = r"C:\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# 列ヘッダー
cells[0, 0].put_value("ID")
cells[0, 1].put_value("Name")
cells[0, 2].put_value("Department")
cells[0, 3].put_value("Salary")
cells[0, 4].put_value("HireDate")

# データ行 1
cells[1, 0].put_value(101)
cells[1, 1].put_value("John Smith")
cells[1, 2].put_value("Engineering")
cells[1, 3].put_value(75000.50)
cells[1, 4].put_value(datetime(2020, 3, 15))

# データ行 2
cells[2, 0].put_value(102)
cells[2, 1].put_value("Jane Doe")
cells[2, 2].put_value("Marketing")
cells[2, 3].put_value(68000.75)
cells[2, 4].put_value(datetime(2019, 7, 22))

# データ行 3
cells[3, 0].put_value(103)
cells[3, 1].put_value("Bob Johnson")
cells[3, 2].put_value("Finance")
cells[3, 3].put_value(82000.00)
cells[3, 4].put_value(datetime(2021, 1, 10))

# データ行 4
cells[4, 0].put_value(104)
cells[4, 1].put_value("Alice Brown")
cells[4, 2].put_value("Human Resources")
cells[4, 3].put_value(71000.25)
cells[4, 4].put_value(datetime(2018, 11, 5))

# データ行 5
cells[5, 0].put_value(105)
cells[5, 1].put_value("Charlie Wilson")
cells[5, 2].put_value("Operations")
cells[5, 3].put_value(79500.80)
cells[5, 4].put_value(datetime(2022, 5, 30))

# 可読性を向上させるために列幅を設定
worksheet.cells.set_column_width(0, 8)
worksheet.cells.set_column_width(1, 20)
worksheet.cells.set_column_width(2, 20)
worksheet.cells.set_column_width(3, 12)
worksheet.cells.set_column_width(4, 14)

workbook.save(filePath, ac.SaveFormat.Dbf)
```

{{% alert color="primary" %}}

DBF ファイルにデータを書き込む際は、データがこの形式の制限事項に準拠していることを確認してください。フィールド名は 10 文字以下とし、スペースを含めないでください。合計で 4000 バイトを超えるレコードは正しく保存されません。日付は YYYYMMDD 形式で表現できる有効な日付値である必要があります。

{{% /alert %}}

## **データ型と書式設定の考慮事項**

Aspose.Cells と DBF 形式の間でデータを転送する場合、データの整合性を確保するために、2 つのシステム間でデータ型がどのようにマッピングされるかを理解することが重要です。

### セルタイプから DBF フィールドタイプへ

Aspose.Cells のセル値は、保存時に自動的に適切な DBF フィールドタイプに変換されます:

- **文字列** は文字 (C) フィールドにマッピングされます。
- **数値** (整数と小数) は数値 (N) フィールドにマッピングされます。
- **日付値** は `YYYYMMDD` 形式の日付 (D) フィールドにマッピングされます。
- **ブール値** は論理 (L) フィールドにマッピングされます。

### エンコーディング

DBF ファイルは、作成したアプリケーションによって異なる文字エンコーディングを使用する場合があります。Aspose.Cells はほとんどの場合エンコーディングを透過的に処理しますが、文字の表示に関する問題が発生した場合は、ソースファイルのエンコーディングを確認する必要がある場合があります。

### フィールド名のルール

DBF フィールド名は以下のルールに従う必要があります:

- 最大 10 文字まで。
- 文字で始まる必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時に使用された大文字小文字に関係なく、大文字として保存されます。

### 出力の検証

DBF ファイルを書き込んだ後、Microsoft Excel または任意の dBASE 互換アプリケーションで開くことで結果を検証できます。データは、フィールド名を列ヘッダーとして、ユーザーが提供したデータに従ってレコードが入力された表形式で表示されます。

## **DBF と他の形式間の変換**

Aspose.Cells で DBF ファイルを読み書きする最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの最新のスプレッドシート形式との間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで他のサポートされる任意の形式で再保存したり、その逆を行ったりすることが簡単にできます。

たとえば、DBF ファイルを読み取り、Aspose.Cells API を使用して書式設定や計算を適用し、結果を XLSX ファイルとして保存して、最新のスプレッドシートアプリケーションを使用するユーザーに配布することができます。逆に、XLSX または CSV ファイルからデータを取得して DBF 形式にエクスポートし、レガシーシステムと統合することもできます。



{{< app/cells/assistant language="python" >}}