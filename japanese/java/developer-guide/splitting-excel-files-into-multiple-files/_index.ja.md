---
title: Excelファイルを複数のファイルに分割する
linktitle: Excelファイルを複数のファイルに分割する
description: Aspose.Cellsはスプレッドシートファイルを操作するためのJavaライブラリで、単一のExcelファイルを複数のファイルに分割することをサポートしています。この記事では、各ワークシートを別のワークブックにコピーする方法と、特定のセル範囲を他のワークブックにコピーすることによってExcelファイルを分割する方法について紹介します。
keywords: Aspose.Cells, Java library, spreadsheet, split Excel file, copy worksheet, copy range, multiple workbooks, save as separate files
type: docs
weight: 195
url: /ja/java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cellsは、単一のExcelファイルを複数のファイルに分割することをサポートしています。これを行うには主に2つの方法があります。(1) ソースワークブックの各ワークシートを新しいワークブックにコピーし、それぞれを別々のファイルとして保存する方法、および(2) ワークシートから特定のセル範囲を新しいワークブックにコピーする方法です。どちらのアプローチも、データのサブセットを配布したり、受信者ごとに小さなレポートを作成したり、個別の処理のためにデータを分離したりする必要がある場合に役立ちます。

{{% /alert %}}

## **はじめに**

開発者が単一のExcelファイルを複数の小さなファイルに分割する必要のあるシナリオは多数あります。例えば、ワークブックには部署ごとに1つのワークシートが含まれており、各部署の責任者は自分のシートのみを受け取る必要があります。場合によっては、ワークシートから特定のテーブルまたはデータブロックを抽出し、ワークブックの残りの部分を公開せずに、電子メールでスタンドアロンファイルとして送信したいこともあります。大きな統合ワークブックも、取り扱いを容易にしたり、読み込みを高速化したり、他のシステムでの後続処理を可能にしたりするために、小さなピースに分割する必要が生じる場合もあります。

Aspose.Cellsは、このタスクに対して2つの柔軟なアプローチを提供します。最初のアプローチは、ソースワークブック内のすべてのワークシートを反復処理し、そのコンテンツをまったく新しい`Workbook`インスタンスにコピーして、それぞれを別々のファイルとして保存します。2番目のアプローチは、ワークシート内の特定のセル範囲に焦点を当て、その範囲のみを新しいワークブックにコピーします。どちらの場合も、一般的な流れは同じです。`Workbook`クラスを使用してソースワークブックを読み込み、`Worksheet`オブジェクトと`Cells`オブジェクトを介して関連データにアクセスし、コンテンツを宛先の`Workbook`に転送してから、宛先をディスクに保存します。

## **各ワークシートを新しいワークブックにコピーしてExcelファイルを分割する**

### **アプローチの概要**

このアプローチでは、ソースワークブックを1回開き、`Worksheets`コレクション内のすべての`Worksheet`に対して、新しい宛先`Workbook`を作成します。次に、ソースワークシートのコンテンツを宛先ワークブックの最初のワークシートにコピーし、ソースワークシートの名前に由来する名前を持つファイルとして宛先ワークブックを保存します。結果は、ワークシートごとに1つの出力ファイルであり、各出力ファイルには単一のソースシートのデータが含まれています。

この方法は、ソースワークブック内の各ワークシートが（部署、地域、月、製品ラインなどの）論理的に独立した情報単位を表しており、各単位を個別に配信または処理したい場合に適切な選択です。

### **手順**

以下の手順では、各ワークシートを新しいワークブックにコピーしてExcelファイルを分割する方法について説明します。

1. `Workbook`オブジェクトをインスタンス化し、ファイルパスをコンストラクタに渡して、ソースExcelファイルを開きます。
2. `for`ループまたは`foreach`ループを使用して`Workbook.Worksheets`コレクションを反復処理し、ソースファイル内のすべての`Worksheet`が処理されるようにします。
3. ループ内で、現在のワークシートに対して新しい宛先`Workbook`インスタンス（空のワークブック）を作成します。
4. 宛先ワークブックに新しい`Worksheet`を追加し（またはデフォルトの最初のワークシートを使用し）、意味のある名前を割り当てます。理想的には、ソースワークシートの`Name`プロパティと同じ名前にします。
5. ソースワークシートのコンテンツを宛先ワークシートにコピーします。これは、ソースワークシートの`Cells`コレクションのセルを反復処理し、その値を宛先ワークシートの対応するセルに書き込むか、`Cells.copy`メソッドを使用して範囲全体を一度に転送することによって行うことができます。
6. ソースワークシートの名前を組み込んだ出力ファイルパス（例えば、`dataDir + worksheet.getName() + ".xls"`）を構築し、生成された各ファイルに一意の名前が付けられるようにします。
7. 宛先`Workbook.save`メソッドを呼び出して、ファイルをディスクに書き込みます。
8. すべてのワークシートが処理されるまで、次のワークシートについて手順3〜7を繰り返します。

### **コード例**

```java
import com.aspose.cells.*;

String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}
```

期待される出力は、データディレクトリ内の新しいファイルのセットであり、ソースワークブックのワークシートごとに1つのファイルがあります。各ファイルは対応するソースシートにちなんで命名されており、そのファイルにはその単一シートのデータ（およびオプションで書式設定）が含まれています。

## **範囲を新しいワークブックにコピーしてExcelファイルを分割する**

### **アプローチの概要**

時々、分割する必要のあるデータはワークシート全体ではなく、`A1:D10`や特定のテーブルを表す名前付き範囲など、ワークシートの特定の長方形領域に対応します。このような場合、ワークシート全体をコピーするのは無駄であり、より正確なアプローチが必要です。ソース範囲を特定し、その範囲のみを新しいワークブックにコピーして、新しいファイルとして保存します。

このアプローチは、より大きなワークシートから無関係なコンテンツをすべて破棄しながら、単一のテーブル、レポートブロック、またはデータ領域を抽出したい場合に最適です。シートのユーザーが選択した領域をスタンドアロンファイルとしてエクスポートするためにも役立ちます。

### **手順**

以下の手順では、特定の範囲を新しいワークブックにコピーしてExcelファイルを分割する方法について説明します。

1. ファイルパスを持つ`Workbook`オブジェクトをインスタンス化して、ソースExcelファイルを開きます。
2. コピーする範囲を含むターゲットの`Worksheet`を取得します。インデックス（例えば最初のシート）または`Worksheets`コレクションから名前で取得します。
3. コピーする範囲を特定します。これは、`A1:C10`のようなハードコードされたセル範囲、`Worksheet.Cells`コレクションを介して取得された名前付き範囲、または`Worksheet.Cells.createRange`を介して作成された範囲のいずれかです。
4. 新しい宛先`Workbook`インスタンスを作成します。
5. 宛先ワークブックの最初の`Worksheet`（デフォルトのシート）にアクセスします。
6. ソース範囲を宛先ワークシートにコピーします。通常はセル`A1`から開始します。宛先`Cells`コレクションの`Cells.copy`メソッドを使用して範囲全体をコピーするか、ソース範囲のセルを反復処理してその値を`putValue`で宛先セルに書き込むことができます。オプションの`CopyOptions`を指定して、転送される内容（値のみ、値とスタイル、数式など）を制御できます。
7. `Workbook.save`メソッドを使用して、宛先ワークブックをディスク上の新しいファイルパスに保存します。

### **コード例**

```java
import com.aspose.cells.*;

// データディレクトリとファイルパスを定義する
String dataDir = "data/";
String sourcePath = dataDir + "book1.xls";
String outputPath = dataDir + "outputrange.xls";

// ソースExcelファイルを開く
Workbook sourceWorkbook = new Workbook(sourcePath);

// ソースワークブックから最初のワークシートを取得する
Worksheet sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// ソースセル範囲A1:C10を定義する（行0、列0から始まる10行3列）
Range sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// 新しい宛先ワークブックを作成する
Workbook destWorkbook = new Workbook();

// 宛先ワークブックの最初のワークシートにアクセスする
Worksheet destWorksheet = destWorkbook.getWorksheets().get(0);

// ソース範囲と同じサイズでA1に宛先範囲を作成する
Range destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// ソース範囲を宛先範囲にコピーする
destRange.copy(sourceRange);

// 宛先ワークブックを新しい.xlsファイルとして保存する
destWorkbook.save(outputPath, SaveFormat.EXCEL_97_TO_2003);
```

期待される出力は、ソースワークブックから抽出された指定された範囲の値（およびオプションで書式設定）のみを含む、データディレクトリ内の単一の新しいファイルです。宛先ファイルはソースファイル内の他のデータと何の関係もありません。最初のワークシートのセル`A1`から始まる、抽出された範囲のみが含まれています。

## **関連記事**

- [行と列のコピー](/ja/cells/java/copying-rows-and-columns/)
- [セルの結合と結合解除](/ja/cells/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}