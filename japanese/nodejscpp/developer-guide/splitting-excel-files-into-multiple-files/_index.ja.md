---
title: Excel ファイルを複数のファイルに分割する
linktitle: Excel ファイルを複数のファイルに分割する
description: Aspose.Cells はスプレッドシートファイルを扱うための Node.js ライブラリで、単一の Excel ファイルを複数のファイルに分割することをサポートします。この記事では、各ワークシートを別のワークブックにコピーする方法と、特定のセル範囲を他のワークブックにコピーする方法によって Excel ファイルを分割する方法を紹介します。
keywords: Aspose.Cells, Node.js library, spreadsheet, split Excel file, copy worksheet, copy range, multiple workbooks, save as separate files
type: docs
weight: 195
url: /ja/nodejs-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、単一の Excel ファイルを複数のファイルに分割することをサポートします。これを行うには主に 2 つの方法があります。(1) ソースワークブックの各ワークシートを新しいワークブックにコピーし、それぞれを別のファイルとして保存する方法、および (2) ワークシートから特定のセル範囲を新しいワークブックにコピーする方法です。データの一部を配布したり、受信者ごとに小さなレポートを作成したり、個別の処理のためにデータを分離したりする必要がある場合、どちらのアプローチも役立ちます。

{{% /alert %}}

## **はじめに**

開発者が単一の Excel ファイルを複数の小さなファイルに分割する必要のある実世界のシナリオは多数あります。たとえば、ワークブックには部署ごとに 1 つのワークシートが含まれており、各部署の責任者は自分のシートのみを受け取る必要があります。場合によっては、ワークシートから特定のテーブルまたはデータブロックを抽出し、ワークブックの他の部分を公開せずにスタンドアロンのファイルとして電子メールで送信したい場合もあります。大規模な統合ワークブックは、取り扱いを容易にし、読み込みを高速化し、他のシステムによる下流処理を行うために、小さなピースに分割する必要がある場合もあります。

Aspose.Cells は、このタスクに対して 2 つの柔軟なアプローチを提供します。最初のアプローチでは、ソースワークブック内のすべてのワークシートを反復処理し、その内容をまったく新しい `Workbook` インスタンスにコピーして、それぞれを別のファイルとして保存します。2 番目のアプローチでは、ワークシート内の特定のセル範囲に注目し、その範囲のみを新しいワークブックにコピーします。いずれの場合も、一般的なフローは同じです。`Workbook` クラスを使用してソースワークブックを読み込み、`Worksheet` および `Cells` オブジェクトを介して関連データにアクセスし、内容を宛先の `Workbook` に転送してから、宛先をディスクに保存します。

## **各ワークシートを新しいワークブックにコピーして Excel ファイルを分割する**

### **アプローチの概要**

このアプローチでは、ソースワークブックを 1 回開き、その `Worksheets` コレクション内のすべての `Worksheet` について、新しい宛先 `Workbook` を作成します。次に、ソースワークシートの内容を宛先ワークブックの最初のワークシートにコピーし、ソースワークシート名から派生した名前のファイルとして宛先ワークブックを保存します。その結果、ワークシートごとに 1 つの出力ファイルが生成され、各出力ファイルには単一のソースシートのデータが含まれます。

この方法は、ソースワークブック内の各ワークシートが (部署、地域、月、製品ラインなど) 論理的に独立した情報の単位を表しており、それぞれの単位を個別に配信または処理したい場合に適しています。

### **手順**

次の手順では、各ワークシートを新しいワークブックにコピーして Excel ファイルを分割する方法について説明します。

1. `Workbook` オブジェクトをインスタンス化し、ファイルパスをコンストラクターに渡してソースの Excel ファイルを開きます。
2. `for` ループまたは `forEach` ループを使用して `Workbook.Worksheets` コレクションを反復処理し、ソースファイル内のすべての `Worksheet` が処理されるようにします。
3. ループ内で、現在のワークシート用の新しい宛先 `Workbook` インスタンス(空のワークブック)を作成します。
4. 宛先ワークブックに新しい `Worksheet` を追加し(またはデフォルトの最初のワークシートを使用し)、意味のある名前を割り当てます。理想的にはソースワークシートの `Name` プロパティと同じにします。
5. ソースワークシートの内容を宛先ワークシートにコピーします。これは、ソースワークシートの `Cells` コレクション内のセルを反復処理し、その値を宛先ワークシートの対応するセルに書き込むか、`Cells.copy` メソッドを使用して範囲全体を一度に転送することによって行うことができます。
6. ソースワークシート名(たとえば `dataDir + worksheet.Name + ".xls"`)を組み込んだ出力ファイルパスを作成して、生成された各ファイルに一意の名前を付けます。
7. 宛先の `Workbook.save` メソッドを呼び出して、ファイルをディスクに書き込みます。
8. すべてのワークシートが処理されるまで、ステップ 3 から 7 を次のワークシートに対して繰り返します。

### **コード例**

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "data/";
const workbook = new AsposeCells.Workbook(dataDir + "book1.xls");

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
    const sourceSheet = workbook.getWorksheets().get(i);
    const sheetName = sourceSheet.getName();
    
    const destWorkbook = new AsposeCells.Workbook();
    const destIndex = destWorkbook.getWorksheets().add();
    const destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    const destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, AsposeCells.SaveFormat.Excel97To2003);
}
```

予想される出力は、データディレクトリ内の一連の新しいファイルです。ワークシートごとに 1 つのファイルが生成されます。各ファイルは対応するソースシートにちなんで名前が付けられ、その単一シートのデータ(およびオプションで書式設定)が含まれます。

## **範囲を新しいワークブックにコピーして Excel ファイルを分割する**

### **アプローチの概要**

場合によっては、分割する必要のあるデータがワークシート全体ではなく、`A1:D10` や特定のテーブルを表す名前付き範囲など、ワークシートの特定の矩形領域に対応することがあります。このような場合、ワークシート全体をコピーするのは無駄であり、より正確なアプローチが必要です。ソース範囲を識別し、その範囲のみを新しいワークブックにコピーして、新しいファイルを保存します。

このアプローチは、関連のないすべてのコンテンツを破棄しながら、大きなワークシートから単一のテーブル、レポートブロック、またはデータ領域を抽出する場合に最適です。シートのユーザーが選択した領域をスタンドアロンファイルとしてエクスポートする場合にも役立ちます。

### **手順**

次の手順では、特定の範囲を新しいワークブックにコピーして Excel ファイルを分割する方法について説明します。

1. ファイルパスを指定して `Workbook` オブジェクトをインスタンス化し、ソースの Excel ファイルを開きます。
2. コピーする範囲を含むターゲットの `Worksheet` を、インデックス(たとえば最初のシート)または `Worksheets` コレクションから名前で取得します。
3. コピーする範囲を識別します。これは、`A1:C10` のようなハードコードされたセル範囲、`Worksheet.Cells` コレクションから取得した名前付き範囲、または `Worksheet.Cells.createRange` によって作成された範囲のいずれかになります。
4. 新しい宛先 `Workbook` インスタンスを作成します。
5. 宛先ワークブックの最初の `Worksheet`(デフォルトのシート)にアクセスします。
6. ソース範囲を宛先ワークシートにコピーします。通常、セル `A1` から開始します。宛先の `Cells` コレクションの `Cells.copy` メソッドを使用して範囲全体をコピーするか、ソース範囲のセルを反復処理して `putValue` で宛先セルにその値を書き込むことができます。オプションの `CopyOptions` を指定して、転送されるもの(値のみ、値とスタイル、数式など)を制御できます。
7. `Workbook.save` メソッドを使用して、宛先ワークブックをディスク上の新しいファイルパスに保存します。

### **コード例**

```javascript
const AsposeCells = require("aspose.cells");

// データディレクトリとファイルパスを定義する
const dataDir = "data/";
const sourcePath = dataDir + "book1.xls";
const outputPath = dataDir + "outputrange.xls";

// ソースのExcelファイルを開く
const sourceWorkbook = new AsposeCells.Workbook(sourcePath);

// ソースワークブックから最初のワークシートを取得する
const sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// ソースセル範囲A1:C10を定義する（10行3列、行0列0から開始）
const sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// 新しい宛先ワークブックを作成する
const destWorkbook = new AsposeCells.Workbook();

// 宛先ワークブックの最初のワークシートにアクセスする
const destWorksheet = destWorkbook.getWorksheets().get(0);

// ソース範囲と同じ寸法の宛先範囲をA1に作成する
const destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// ソース範囲を宛先範囲にコピーする
destRange.copy(sourceRange);

// 宛先ワークブックを新しい.xlsファイルに保存する
destWorkbook.save(outputPath, AsposeCells.SaveFormat.Excel97To2003);
```

予想される出力は、データディレクトリ内の単一の新しいファイルで、ソースワークブックから抽出された指定された範囲の値(およびオプションで書式設定)のみが含まれます。宛先ファイルはソースファイル内の他のデータとは関係ありません。抽出された範囲のみが含まれ、最初のワークシートのセル `A1` から始まります。

## **関連記事**

- [行と列のコピー](/cells/ja/nodejs-cpp/copying-rows-and-columns/)
- [セルの結合と結合解除](/cells/ja/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}