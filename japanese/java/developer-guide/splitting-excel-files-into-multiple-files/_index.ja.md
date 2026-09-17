---
title: Excelファイルを複数ファイルに分割
linktitle: Excelファイルを複数ファイルに分割
description: Aspose.Cellsはスプレッドシートファイルを扱うためのJavaライブラリであり、単一のExcelファイルを複数ファイルに分割することをサポートしています。この記事では、各ワークシートを別のワークブックにコピーする方法、および特定のセル範囲を他のワークブックにコピーする方法によって、Excelファイルを分割する方法を紹介します。
keywords: Aspose.Cells, Javaライブラリ, スプレッドシート, Excelファイルの分割, ワークシートのコピー, 範囲のコピー, 複数ワークブック, 個別ファイルとして保存
type: docs
weight: 195
url: /ja/java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、単一のExcelファイルを複数ファイルに分割することをサポートしています。これを行うには主に2つの方法があります。(1) ソースワークブックの各ワークシートを新しいワークブックにコピーしてそれぞれを別ファイルとして保存する方法、および(2) ワークシートから特定のセル範囲を新しいワークブックにコピーする方法です。データのサブセットを配布したり、受信者ごとに小さいレポートを作成したり、個別の処理のためにデータを分離したりする必要があるときには、どちらの方法も役立ちます。
{{% /alert %}}

## **Introduction**
開発者が単一のExcelファイルを複数の小さいファイルに分割する必要があるシナリオは、現実世界で数多く存在します。たとえば、ワークブックに部門ごとに1つのワークシートが含まれており、各部門責任者は自分のシートのみを受け取る必要があるとします。その他のケースとして、ワークシートから特定のテーブルまたはデータブロックを抽出し、ワークブックの他の部分を公開せずに、それを独立したファイルとしてメールで送信したい場合があります。大きな統合ワークブックを、より扱いやすく、読み込みを高速化し、他のシステムによる下流処理のために、より小さなピースに分割する必要が生じることもあります。
Aspose.Cellsはこのタスクに対して2つの柔軟なアプローチを提供します。最初のアプローチでは、ソースワークブック内のすべてのワークシートを反復処理し、その内容を新しい`Workbook`インスタンスにコピーして、それぞれを別ファイルとして保存します。2番目のアプローチでは、ワークシート内の特定のセル範囲に焦点を絞り、その範囲のみを新しいワークブックにコピーします。どちらの場合も、一般的な流れは同じです。`Workbook`クラスを使用してソースワークブックを読み込み、`Worksheet`および`Cells`オブジェクトを介して関連データにアクセスし、内容を宛先の`Workbook`に転送してから、宛先をディスクに保存します。

## **Splitting an Excel File by Copying Each Worksheet to a New Workbook**

### **Approach Overview**
このアプローチでは、ソースワークブックを1回開き、その`Worksheets`コレクション内のすべての`Worksheet`に対して新しい宛先`Workbook`が作成されます。次に、ソースワークシートの内容が宛先ワークブックの最初のワークシートにコピーされ、宛先ワークブックはソースワークシートの名前から派生した名前のファイルとして保存されます。結果は、ワークシートごとに1つの出力ファイルとなり、各出力ファイルには単一のソースシートのデータが含まれます。
この方法は、ソースワークブックの各ワークシートが論理的に独立した情報の単位(部門、地域、月、製品ラインなど)を表しており、それぞれの単位を単独で配信または処理したい場合に最適な選択です。

### **Steps**
次の手順は、各ワークシートを新しいワークブックにコピーしてExcelファイルを分割する方法を説明します。
1. `Workbook`オブジェクトをインスタンス化し、ファイルパスをコンストラクタに渡すことで、ソースExcelファイルを開きます。
2. `for`または`foreach`ループを使用して`Workbook.Worksheets`コレクションを反復処理し、ソースファイル内のすべての`Worksheet`が処理されるようにします。
3. ループ内で、現在のワークシートに対して新しい宛先`Workbook`インスタンス(空のワークブック)を作成します。
5. ソースワークシートの内容を宛先ワークシートにコピーします。これは、ソースワークシートの`Cells`コレクションのセルを反復処理し、それらの値を宛先ワークシートの対応するセルに書き込むことで実行できます。または、`Cells.copy`メソッドを使用して、範囲全体を一度に転送することもできます。
6. ソースワークシートの名前を組み込んだ出力ファイルパス(たとえば、`dataDir + worksheet.getName() + ".xls"`)を構築して、生成される各ファイルに一意の名前が付くようにします。
7. 宛先`Workbook.save`メソッドを呼び出して、ファイルをディスクに書き込みます。
8. すべてのワークシートが処理されるまで、次のワークシートについて手順3〜7を繰り返します。

### **Code Example**

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

期待される出力は、データディレクトリ内の一連の新しいファイル(ソースワークブックのワークシートごとに1ファイル)です。各ファイルは対応するソースシートに基づいて名前が付けられ、その単一シートのデータ(およびオプションで書式設定)が含まれています。

## **Splitting an Excel File by Copying a Range to a New Workbook**

### **Approach Overview**
分割する必要があるデータがワークシート全体ではなく、ワークシートの特定の矩形領域(たとえば`A1:D10`や特定のテーブルを表す名前付き範囲)に対応する場合もあります。このような場合、ワークシート全体をコピーするのは無駄であり、より正確なアプローチが必要です。ソース範囲を特定し、その範囲のみを新しいワークブックにコピーして、新しいファイルを保存します。
このアプローチは、より大きなワークシートから単一のテーブル、レポートブロック、またはデータ領域を抽出し、無関係なコンテンツをすべて破棄する場合に最適です。また、シートのユーザーが選択した領域を独立したファイルとしてエクスポートする場合にも役立ちます。

### **Steps**
次の手順は、特定の範囲を新しいワークブックにコピーしてExcelファイルを分割する方法を説明します。
1. ファイルパスを持つ`Workbook`オブジェクトをインスタンス化して、ソースExcelファイルを開きます。
2. コピーしたい範囲を含むターゲットの`Worksheet`を、インデックス(たとえば最初のシート)または`Worksheets`コレクションから名前で取得します。
3. コピーする範囲を特定します。これは、`A1:C10`のようなハードコードされたセル範囲、または`Worksheet.Cells`コレクションを通じて取得した名前付き範囲、あるいは`Worksheet.Cells.createRange`を介して作成された範囲です。
4. 新しい宛先`Workbook`インスタンスを作成します。
5. 宛先ワークブックの最初の`Worksheet`(デフォルトシート)にアクセスします。
6. ソース範囲を宛先ワークシートにコピーします。通常はセル`A1`から開始します。宛先の`Cells`コレクションの`Cells.copy`メソッドを使用して範囲全体をコピーできます。または、ソース範囲のセルを反復処理し、`putValue`を使用してそれらの値を宛先セルに書き込むこともできます。オプションの`CopyOptions`を渡し、何が転送されるか(値のみ、値とスタイル、数式など)を制御できます。
7. `Workbook.save`メソッドを使用して、宛先ワークブックをディスク上の新しいファイルパスに保存します。

### **Code Example**
期待される出力は、データディレクトリ内の単一の新しいファイルで、ソースワークブックから抽出された指定された範囲の値(およびオプションで書式設定)のみが含まれています。宛先ファイルはソースファイル内の他のデータとの関連を持たず、最初のワークシートのセル`A1`から始まる抽出された範囲のみを含みます。

## Related Articles
- [Aspose.Cells for Javaでピボットテーブルにフィルターフィールドを追加](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Javaでピボットテーブルにスタイルを適用](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルでページフィールドのレイアウトを変更](/cells/ja/java/change-page-field-layout/)
- [Aspose.Cells for Javaでスパークラインを画像とHTMLに変換](/cells/ja/java/convert-sparkline-to-image-and-html/)
- [ExcelをOFD形式に変換](/cells/ja/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}