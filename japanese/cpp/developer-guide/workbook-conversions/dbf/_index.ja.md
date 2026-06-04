---
title: DBF ファイルの読み取りと書き込み
description: Aspose.Cells はスプレッドシートファイルを扱うための C++ ライブラリであり、dBASE III および IV (DBF) ファイルの読み取りと書き込みをサポートします。この記事では、ファイル形式の詳細、サポートされている機能、ステップごとの例を含め、Aspose.Cells を使用して DBF ファイルからデータをインポートしたり、データをエクスポートしたりする方法について説明します。
keywords: Aspose.Cells, C++ ライブラリ, DBF, dBASE, DBF の読み取り, DBF の書き込み, DBF のインポート, DBF のエクスポート, ファイル形式, .dbf
type: docs
weight: 200
url: /ja/cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells は DBF (dBASE) ファイルの読み取りと書き込みを完全にサポートします。既存の dBASE III および dBASE IV ファイルを Workbook オブジェクトに読み込み、豊富な Aspose.Cells API を使用してデータを操作し、ワークブックを DBF 形式に保存してレガシーデータベースアプリケーションで使用することができます。

{{% /alert %}}

## **はじめに**

DBF (DataBase File) は、1980 年代初頭に dBASE によって導入されたレガシーなデータベースファイル形式です。古い形式ではありますが、DBF ファイルは、特に会計、GIS、その他の専門的なアプリケーションで構造化データを保存するために、多くの業界で現在も広く使用されています。Aspose.Cells を使用すると、これらのレガシーファイルを最新の C++ スプレッドシートワークフローにシームレスに統合できます。

このライブラリは DBF ファイルの読み取りと書き込みの両方をサポートしており、以下のことが可能になります。

- 既存の DBF ファイルから Aspose.Cells の Workbook オブジェクトにデータをインポートし、さらに処理したり他の形式に変換したりする。
- 他のスプレッドシート形式のデータを変換して使用したり、新規作成したりして、新しい DBF ファイルを作成する。
- データの DBF 形式への入出力時に、フィールド定義、データ型、レコード構造を維持する。

DBF ファイルは Microsoft Excel などのスプレッドシートアプリケーションで直接開くこともできるため、レガシーシステムと最新のスプレッドシートツール間の便利な橋渡しとなります。

## **サポートされている DBF のバージョンと機能**

Aspose.Cells は以下の DBF 形式のバージョンをサポートしています。

- **dBASE III** — DBF 形式のオリジナルかつ最も広くサポートされているバリアントです。
- **dBASE IV** — 追加のデータ型とより大きなフィールドサイズをサポートする拡張バージョンです。

### サポートされている機能

このライブラリは、以下の操作に対して包括的なサポートを提供します。

- すべてのレコードとフィールド定義を保持したまま、DBF データを Workbook オブジェクトに読み取る。
- ワークブックデータを DBF 形式に書き戻し、dBASE 互換アプリケーションにエクスポートする。
- 文字、数値、日付、論理フィールドなど、DBF ファイルで使用される一般的なデータ型を処理する。
- 読み取り/書き込み操作中に、フィールド名、型、長さなどのフィールド定義を保持する。

### 制限事項と考慮事項

DBF ファイルを扱う際は、以下の制約事項に注意してください。

- ファイルあたりの最大フィールド数は **128** です。
- 最大レコードサイズは **4000 バイト**です。
- フィールド名は **10 文字**以内に制限され、大文字である必要があり、スペースを含めることはできません。
- DBF ファイルの日付値は `YYYYMMDD` 形式で保存されます。
- 文字エンコーディングはソースアプリケーションによって異なる場合があります (一般的には Windows-1252 または OEM コードページ)。

## **DBF ファイルの読み取り**

Aspose.Cells を使用すると、DBF ファイルから Workbook オブジェクトへのデータ読み込みを簡単に行うことができます。このライブラリは `LoadOptions` クラスを使用してソース形式を指定し、読み込みプロセス中にデータが正しく解釈されるようにします。

### Aspose.Cells を使用して DBF ファイルを読み取る

DBF ファイルを読み取るには、`LoadOptions` インスタンスを作成し、その `LoadFormat` プロパティを `LoadFormat.Dbf` に設定して、ファイルパスとともに `Workbook` コンストラクタに渡す必要があります。一度読み込まれると、データは `Worksheets` コレクションを介してアクセス可能になり、セルを反復処理したり、値を抽出したり、必要に応じてデータを操作したりできます。

次の例は、既存の DBF ファイルを Aspose.Cells に読み込み、最初のワークシートにアクセスしてセルの値を読み取る方法を示しています。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

[ファイルを開く] ダイアログでファイルを選択することで、Microsoft Excel で DBF ファイルを直接開くことができます。Excel は DBF ファイルをスプレッドシートとして扱い、そのレコードをテーブル形式で表示します。これは、Aspose.Cells で読み取りまたは書き込みを行った後にデータをすばやく検証するのに役立ちます。

{{% /alert %}}

## **DBF ファイルの書き込み**

DBF ファイルへのデータ書き込みは、Aspose.Cells を使用して他のスプレッドシート形式を保存する場合と同様のパターンに従います。Workbook を作成または読み込み、ワークシートにデータを入力し、ターゲット形式として `SaveFormat.Dbf` を指定して `Save` メソッドを呼び出します。

### Aspose.Cells を使用して DBF ファイルを作成する

DBF ファイルを作成するには、以下の手順に従います。

1. 新しい `Workbook` インスタンスを作成します。
2. `Worksheets` コレクションから最初のワークシートにアクセスします。
3. 最初の行にヘッダーを含め、後続の行にレコードを含めて、ワークシートにデータを入力します。
4. ファイルパスと `SaveFormat.Dbf` をパラメータとして渡して `Workbook.Save` メソッドを呼び出します。

次の例は、新しい DBF ファイルを作成する方法を示しています。さまざまなデータ型 (文字列、数値、日付) を含むサンプルデータをワークシートに入力し、DBF 形式へのエクスポート時にフィールド型がどのように処理されるかを示しています。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // 列ヘッダー
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // データ行 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // データ行 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // データ行 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // データ行 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // データ行 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // 可読性のために列幅を設定
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

DBF ファイルにデータを書き込む際は、データがその形式の制限事項に準拠していることを確認してください。フィールド名は 10 文字以内とし、スペースを含めないでください。合計 4000 バイトを超えるレコードは正しく保存されません。日付は YYYYMMDD 形式で表現できる有効な日付値である必要があります。

{{% /alert %}}

## **データ型と書式設定の考慮事項**

Aspose.Cells と DBF 形式の間でデータを転送する場合、データの整合性を確保するために、2 つのシステム間でデータ型がどのようにマップされるかを理解することが重要です。

### セルの種類から DBF フィールドタイプへのマッピング

Aspose.Cells のセル値は、保存時に適切な DBF フィールドタイプに自動的に変換されます。

- **文字列** は文字 (C) フィールドにマッピングされます。
- **数値** (整数と小数) は数値 (N) フィールドにマッピングされます。
- **日付値** は `YYYYMMDD` 形式の日付 (D) フィールドにマッピングされます。
- **ブール値** は論理 (L) フィールドにマッピングされます。

### エンコーディング

DBF ファイルは、作成元のアプリケーションに応じて異なる文字エンコーディングを使用する場合もあります。Aspose.Cells はほとんどの場合、エンコーディングを透過的に処理しますが、文字表示の問題が発生した場合は、ソースファイルのエンコーディングを確認する必要があるかもしれません。

### フィールド名のルール

DBF のフィールド名は以下のルールに従う必要があります。

- 最大 10 文字まで。
- 文字で始まる必要があります。
- スペースや特殊文字を含めることはできません。
- 入力時に使用された大文字小文字に関係なく、大文字として保存されます。

### 出力の検証

DBF ファイルを書き込んだ後、Microsoft Excel または任意の dBASE 互換アプリケーションでファイルを開いて結果を検証できます。データは、フィールド名が列ヘッダーとなり、提供したデータに応じてレコードが入力された表形式で表示されるはずです。

## **DBF と他の形式間の変換**

Aspose.Cells で DBF ファイルを読み書きする最も実用的なユースケースの 1 つは、DBF 形式と XLSX、XLS、CSV などの最新のスプレッドシート形式との間でデータを変換することです。Aspose.Cells は幅広い形式をサポートしているため、DBF ファイルを読み込んで、サポートされている他の任意の形式で再保存したり、その逆を行うことも簡単にできます。

たとえば、DBF ファイルを読み取り、Aspose.Cells API を使用して書式設定や計算を適用し、最新のスプレッドシートアプリケーションを使用するユーザーに配布するために、結果を XLSX ファイルとして保存できます。逆に、XLSX または CSV ファイルからデータを取得して DBF 形式にエクスポートし、レガシーシステムと統合することもできます。



{{< app/cells/assistant language="cpp" >}}