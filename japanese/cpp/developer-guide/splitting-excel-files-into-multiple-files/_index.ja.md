---
title: Excel ファイルを複数のファイルに分割する
linktitle: Excel ファイルを複数のファイルに分割する
description: Aspose.Cells はスプレッドシートファイルを扱うための C++ ライブラリであり、単一の Excel ファイルを複数のファイルに分割することをサポートしています。この記事では、各ワークシートを別のワークブックにコピーする方法と、特定のセル範囲を他のワークブックにコピーする方法によって Excel ファイルを分割する方法を紹介します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, Excel ファイルの分割, ワークシートのコピー, 範囲のコピー, 複数のワークブック, 個別のファイルとして保存
type: docs
weight: 195
url: /ja/cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、単一の Excel ファイルを複数のファイルに分割することをサポートしています。これを行うには主に 2 つの方法があります。(1) ソースワークブックの各ワークシートを新しいワークブックにコピーし、それぞれを別のファイルとして保存する方法、および (2) ワークシートから特定のセル範囲を新しいワークブックにコピーする方法です。どちらのアプローチも、データのサブセットを配布したり、受取人ごとに小さなレポートを作成したり、個別の処理のためにデータを分離したりする場合に役立ちます。

{{% /alert %}}

## **はじめに**

開発者が単一の Excel ファイルを複数の小さなファイルに分割する必要が生じる現実のシナリオは数多くあります。例えば、ワークブックには部門ごとに 1 つのワークシートが含まれており、各部門長は自分のシートのみを受け取る必要がある場合があります。他にも、ワークシートから特定のテーブルやデータブロックを抽出して、ワークブックの残りの部分を公開せずにスタンドアロンファイルとして電子メールで送信したい場合もあります。また、大規模な統合ワークブックは、取り扱いを容易にし、読み込みを高速化し、他のシステムによる後続処理を行うために、より小さなピースに分割する必要が生じる場合もあります。

Aspose.Cells は、このタスクに対して 2 つの柔軟なアプローチを提供します。最初のアプローチは、ソースワークブック内のすべてのワークシートを反復処理し、その内容を新しい `Workbook` インスタンスにコピーして、それぞれを別のファイルとして保存します。2 番目のアプローチは、ワークシート内の特定のセル範囲に焦点を当て、その範囲のみを新しいワークブックにコピーします。どちらの場合も、一般的な流れは同じです。`Workbook` クラスを使用してソースワークブックを読み込み、`Worksheet` および `Cells` オブジェクトを介して関連データにアクセスし、内容を宛先 `Workbook` に転送してから、宛先をディスクに保存します。

## **各ワークシートを新しいワークブックにコピーして Excel ファイルを分割する**

### **アプローチの概要**

このアプローチでは、ソースワークブックを 1 回開き、その `Worksheets` コレクション内のすべての `Worksheet` について、新しい宛先 `Workbook` を作成します。次に、ソースワークシートの内容を宛先ワークブックの最初のワークシートにコピーし、ソースワークシートの名前に基づいて名前を付けたファイルとして宛先ワークブックを保存します。結果はワークシートごとに 1 つの出力ファイルとなり、各出力ファイルには単一のソースシートのデータが含まれます。

この方法は、ソースワークブック内の各ワークシートが論理的に独立した情報単位 (部門、地域、月、製品ラインなど) を表しており、各単位を個別に配信または処理したい場合に最適な選択肢です。

### **手順**

以下の手順は、各ワークシートを新しいワークブックにコピーして Excel ファイルを分割する方法を説明しています。

1. `Workbook` オブジェクトをインスタンス化し、ファイルパスをコンストラクタに渡すことで、ソース Excel ファイルを開きます。
2. `for` ループまたは `foreach` ループを使用して `Workbook.Worksheets` コレクションを反復処理し、ソースファイル内のすべての `Worksheet` が処理されるようにします。
3. ループ内で、現在のワークシート用の新しい宛先 `Workbook` インスタンス (空のワークブック) を作成します。
4. 宛先ワークブックに新しい `Worksheet` を追加し (またはデフォルトの最初のワークシートを使用して)、意味のある名前を割り当てます。理想的にはソースワークシートの `Name` プロパティと同じ名前にします。
5. ソースワークシートの内容を宛先ワークシートにコピーします。これは、ソースワークシートの `Cells` コレクション内のセルを反復処理し、その値を宛先ワークシートの対応するセルに書き込むか、`Cells.Copy` メソッドを使用して範囲全体を一度に転送することによって行うことができます。
6. ソースワークシートの名前を組み込んだ出力ファイルパス (例: `dataDir + worksheet.Name + ".xls"`) を作成して、生成される各ファイルが固有の名前を持つようにします。
7. 宛先の `Workbook.Save` メソッドを呼び出して、ファイルをディスクに書き込みます。
8. 次のワークシートについて、手順 3 から 7 をすべてのワークシートが処理されるまで繰り返します。

### **コード例**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "data/";
    Workbook wb(U16String((dataDir + "book1.xls").c_str()));

    int sheetCount = wb.GetWorksheets().GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet sourceSheet = wb.GetWorksheets().Get(i);
        U16String sheetName = sourceSheet.GetName();

        Workbook destWorkbook;
        int destIndex = destWorkbook.GetWorksheets().Add();
        Worksheet destSheet = destWorkbook.GetWorksheets().Get(destIndex);
        destSheet.SetName(sheetName);

        destSheet.Copy(sourceSheet);

        std::string destFile = dataDir + sheetName.ToUtf8() + ".xls";
        destWorkbook.Save(U16String(destFile.c_str()), SaveFormat::Excel97To2003);
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

期待される出力は、データディレクトリ内の一連の新しいファイルであり、ソースワークブックのワークシートごとに 1 つのファイルがあります。各ファイルは対応するソースシートにちなんで名前が付けられ、その単一シートのデータ (および必要に応じて書式設定) が含まれています。

## **範囲を新しいワークブックにコピーして Excel ファイルを分割する**

### **アプローチの概要**

場合によっては、分割する必要のあるデータがワークシート全体ではなく、`A1:D10` や特定のテーブルを表す名前付き範囲など、ワークシートの特定の長方形領域に対応していることがあります。このような場合、ワークシート全体をコピーするのは無駄であり、より正確なアプローチが必要です。ソース範囲を識別し、その範囲のみを新しいワークブックにコピーして、新しいファイルを保存します。

このアプローチは、ワークシートから単一のテーブル、レポートブロック、データ領域を抽出して、関連のないすべてのコンテンツを破棄したい場合に最適です。また、シートのユーザーが選択した領域をスタンドアロンファイルとしてエクスポートする場合にも役立ちます。

### **手順**

以下の手順は、特定の範囲を新しいワークブックにコピーして Excel ファイルを分割する方法を説明しています。

1. ファイルパスを指定して `Workbook` オブジェクトをインスタンス化し、ソース Excel ファイルを開きます。
2. コピーしたい範囲を含むターゲットの `Worksheet` を、インデックス (たとえば最初のシート) または `Worksheets` コレクションから名前で取得します。
3. コピーする範囲を識別します。これは、`A1:C10` のようなハードコードされたセル範囲、`Worksheet.Cells` コレクションを介して取得された名前付き範囲、または `Worksheet.Cells.CreateRange` によって作成された範囲のいずれかです。
4. 新しい宛先 `Workbook` インスタンスを作成します。
5. 宛先ワークブックの最初の `Worksheet` (デフォルトのシート) にアクセスします。
6. ソース範囲を宛先ワークシートにコピーします。通常はセル `A1` から開始します。宛先の `Cells` コレクションの `Cells.Copy` メソッドを使用して範囲全体をコピーするか、ソース範囲のセルを反復処理してその値を `PutValue` で宛先セルに書き込むことができます。オプションの `CopyOptions` を指定して、転送される内容を制御できます (値のみ、値とスタイル、数式など)。
7. `Workbook.Save` メソッドを使用して、宛先ワークブックをディスク上の新しいファイルパスに保存します。

### **コード例**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // データディレクトリとファイルパスを定義する
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // ソースExcelファイルを開く
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // ソースワークブックから最初のワークシートを取得する
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // ソースセル範囲 A1:C10 を定義する (10行、3列、開始位置は行0、列0)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // 新しい宛先ワークブックを作成する
    Workbook destWorkbook;

    // 宛先ワークブックの最初のワークシートにアクセスする
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // ソース範囲と同じ寸法で A1 に宛先範囲を作成する
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // ソース範囲を宛先範囲にコピーする
    destRange.Copy(sourceRange);

    // 宛先ワークブックを新しい .xls ファイルに保存する
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}
```

期待される出力は、データディレクトリ内の単一の新しいファイルであり、ソースワークブックから抽出された指定された範囲の値 (および必要に応じて書式設定) のみが含まれています。宛先ファイルはソースファイル内の他のデータとは何の関係もありません。最初のワークシートのセル `A1` で始まる、抽出された範囲のみが含まれています。

## **関連記事**

- [行と列のコピー](/ja/cells/cpp/copying-rows-and-columns/)
- [セルの結合と結合解除](/ja/cells/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}