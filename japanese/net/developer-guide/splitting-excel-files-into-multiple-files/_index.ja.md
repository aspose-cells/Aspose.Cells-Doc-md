---
title: Excel ファイルを複数のファイルに分割する
description: Aspose.Cells はスプレッドシートファイルを扱うための .NET ライブラリであり、単一の Excel ファイルを複数のファイルに分割することをサポートします。この記事では、各ワークシートを別のワークブックにコピーする方法、および特定のセル範囲を他のワークブックにコピーする方法によって Excel ファイルを分割する方法を紹介します。
keywords: Aspose.Cells, .NET library, spreadsheet, split Excel file, copy worksheet, copy range, multiple workbooks, save as separate files
type: docs
weight: 195
url: /ja/net/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells は、単一の Excel ファイルを複数のファイルに分割することをサポートします。これを行うには主に 2 つの方法があります。(1) ソースワークブックの各ワークシートを新しいワークブックにコピーし、それぞれを個別のファイルとして保存する方法、および (2) ワークシートから特定のセル範囲を新しいワークブックにコピーする方法です。どちらのアプローチも、データのサブセットを配布したり、異なる受信者向けの小さなレポートを作成したり、個別の処理のためにデータを分離したりする必要がある場合に役立ちます。

{{% /alert %}}

## **はじめに**

開発者が単一の Excel ファイルを複数の小さなファイルに分割する必要のある現実的なシナリオは多数あります。たとえば、ワークブックには部門ごとに 1 つのワークシートが含まれており、各部門長は自分のシートのみを受け取る必要があります。その他のケースでは、ワークシートから特定のテーブルやデータブロックを抽出し、ワークブックの他の部分を公開せずに、スタンドアロンのファイルとして電子メールで送信したい場合があります。また、大規模な統合ワークブックは、扱いやすくしたり、読み込みを高速化したり、他のシステムによる後続処理のために小さなピースに分割する必要がある場合もあります。

Aspose.Cells は、このタスクに対して 2 つの柔軟なアプローチを提供します。最初のアプローチは、ソースワークブック内のすべてのワークシートを反復処理し、そのコンテンツを新しい `Workbook` インスタンスにコピーして、それぞれを個別のファイルとして保存します。2 番目のアプローチは、ワークシート内の特定のセル範囲に焦点を当て、その範囲のみを新しいワークブックにコピーします。どちらの場合も、一般的な流れは同じです。`Workbook` クラスを使用してソースワークブックを読み込み、`Worksheet` および `Cells` オブジェクトを介して関連データにアクセスし、コンテンツをコピー先の `Workbook` に転送してから、コピー先をディスクに保存します。

## **各ワークシートを新しいワークブックにコピーして Excel ファイルを分割する**

### **アプローチの概要**

このアプローチでは、ソースワークブックを 1 回開き、その `Worksheets` コレクション内のすべての `Worksheet` に対して、新しいコピー先の `Workbook` を作成します。次に、ソースワークシートのコンテンツをコピー先ワークブックの最初のワークシートにコピーし、コピー先ワークブックをソースワークシートの名前に基づいたファイル名で保存します。結果は、ワークシートごとに 1 つの出力ファイルとなり、各出力ファイルには単一のソースシートのデータが含まれます。

この方法は、ソースワークブック内の各ワークシートが論理的に独立した情報単位（部門、地域、月、製品ラインなど）を表しており、それぞれの単位を個別に配信または処理したい場合に適した選択肢です。

### **手順**

次の手順は、各ワークシートを新しいワークブックにコピーして Excel ファイルを分割する方法を示しています。

1. `Workbook` オブジェクトをインスタンス化し、ファイルパスをコンストラクタに渡して、ソース Excel ファイルを開きます。
2. `for` ループまたは `foreach` ループを使用して `Workbook.Worksheets` コレクションを反復処理し、ソースファイル内のすべての `Worksheet` が処理されるようにします。
3. ループ内で、現在のワークシート用に新しいコピー先の `Workbook` インスタンス（空のワークブック）を作成します。
4. コピー先ワークブックに新しい `Worksheet` を追加し（またはデフォルトの最初のワークシートを使用し）、意味のある名前を割り当てます。理想的には、ソースワークシートの `Name` プロパティと同じ名前にします。
5. ソースワークシートのコンテンツをコピー先ワークシートにコピーします。これは、ソースワークシートの `Cells` コレクションのセルを反復処理し、その値をコピー先ワークシートの対応するセルに書き込むことによって行うことも、`Cells.Copy` メソッドを使用して範囲全体を一度に転送することもできます。
6. ソースワークシートの名前を組み込んだ出力ファイルパス（たとえば、`dataDir + worksheet.Name + ".xls"`）を構築し、生成された各ファイルが一意の名前を持つようにします。
7. コピー先の `Workbook.Save` メソッドを呼び出して、ファイルをディスクに書き込みます。
8. すべてのワークシートが処理されるまで、次のワークシートについて手順 3 から 7 を繰り返します。

### **コード例**

```csharp
using System;
using System.IO;
using Aspose.Cells;

string dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet sourceSheet = workbook.Worksheets[i];
    string sheetName = sourceSheet.Name;
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.Worksheets.Add();
    Worksheet destSheet = destWorkbook.Worksheets[destIndex];
    destSheet.Name = sheetName;
    
    destSheet.Copy(sourceSheet);
    
    string destFile = dataDir + sheetName + ".xls";
    destWorkbook.Save(destFile, SaveFormat.Excel97To2003);
}
```

予想される出力は、データディレクトリ内の新しいファイルのセットであり、ソースワークブックからのワークシートごとに 1 つのファイルがあります。各ファイルは対応するソースシートにちなんで名前が付けられ、そのファイルにはその単一シートのデータ（およびオプションで書式設定）が含まれています。

## **範囲を新しいワークブックにコピーして Excel ファイルを分割する**

### **アプローチの概要**

時には、分割する必要のあるデータはあるワークシートの全体ではなく、`A1:D10` のような特定の矩形領域や、特定のテーブルを表す名前付き範囲に対応しています。これらの場合、ワークシート全体をコピーするのは無駄であり、より正確なアプローチが必要です。ソース範囲を特定し、その範囲のみを新しいワークブックにコピーして、新しいファイルを保存します。

このアプローチは、より大きなワークシートから単一のテーブル、レポートブロック、またはデータ領域を抽出し、関連しないすべてのコンテンツを破棄したい場合に理想的です。また、シートのユーザーが選択した領域をスタンドアロンのファイルとしてエクスポートする場合にも役立ちます。

### **手順**

次の手順は、特定の範囲を新しいワークブックにコピーして Excel ファイルを分割する方法を示しています。

1. ファイルパスを使用して `Workbook` オブジェクトをインスタンス化し、ソース Excel ファイルを開きます。
2. コピーしたい範囲を含む対象の `Worksheet` を、インデックス（たとえば、最初のシート）または `Worksheets` コレクションからの名前によって取得します。
3. コピーする範囲を特定します。これは、`A1:C10` のようなハードコードされたセル範囲、`Worksheet.Cells` コレクションを介して取得された名前付き範囲、または `Worksheet.Cells.CreateRange` を介して作成された範囲にすることができます。
4. 新しいコピー先の `Workbook` インスタンスを作成します。
5. コピー先ワークブックの最初の `Worksheet`（デフォルトのシート）にアクセスします。
6. ソース範囲を、通常はセル `A1` から開始して、コピー先ワークシートにコピーします。コピー先 `Cells` コレクションの `Cells.Copy` メソッドを使用して範囲全体をコピーすることも、ソース範囲のセルを反復処理し、その値を `PutValue` でコピー先セルに書き込むこともできます。オプションの `CopyOptions` を指定して、転送される内容を制御できます（値のみ、値とスタイル、数式など）。
7. `Workbook.Save` メソッドを使用して、コピー先ワークブックをディスク上の新しいファイルパスに保存します。

### **コード例**

```csharp
using System;
using System.IO;
using Aspose.Cells;

// データディレクトリとファイルパスを定義する
string dataDir = "data/";
string sourcePath = dataDir + "book1.xls";
string outputPath = dataDir + "outputrange.xls";

// ソースExcelファイルを開く
Workbook sourceWorkbook = new Workbook(sourcePath);

// ソースワークブックから最初のワークシートを取得する
Worksheet sourceWorksheet = sourceWorkbook.Worksheets[0];

// ソースセル範囲 A1:C10 を定義する(行0、列0から始まる10行3列)
var sourceRange = sourceWorksheet.Cells.CreateRange(0, 0, 10, 3);

// 新しい宛先ワークブックを作成する
Workbook destWorkbook = new Workbook();

// 宛先ワークブックの最初のワークシートにアクセスする
Worksheet destWorksheet = destWorkbook.Worksheets[0];

// ソース範囲と同じ寸法で A1 に宛先範囲を作成する
var destRange = destWorksheet.Cells.CreateRange(0, 0, 10, 3);

// ソース範囲を宛先範囲にコピーする
destRange.Copy(sourceRange);

// 宛先ワークブックを新しい .xls ファイルとして保存する
destWorkbook.Save(outputPath, SaveFormat.Excel97To2003);
```

予想される出力は、データディレクトリ内の単一の新しいファイルであり、ソースワークブックから抽出された指定された範囲の値（およびオプションで書式設定）のみが含まれています。コピー先ファイルはソースファイル内の他のデータとは関係がなく、最初のワークシートのセル `A1` から始まる抽出された範囲のみを含んでいます。

## **関連記事**

- [Copying Rows and Columns](/cells/ja/net/copying-rows-and-columns/)
- [Merging and Unmerging Cells](/cells/ja/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}