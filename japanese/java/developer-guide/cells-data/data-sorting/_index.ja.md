---
title: データの並べ替え
type: docs
weight: 90
url: /ja/java/sort-data-of-excel/
---
{{% alert color="primary" %}}

データの並べ替えは、Microsoft Excel の多くの便利な機能の 1 つです。これにより、ユーザーはデータを並べ替えてスキャンしやすくすることができます。

Aspose.Cells では、ワークシート データをアルファベット順または数値順に並べ替えることができます。 Microsoft Excel でデータを並べ替えるのと同じように機能します。

{{% /alert %}}

## **Microsoft Excel でのデータの並べ替え**

Microsoft Excel でデータを並べ替えるには:

1. 選択する**データ**から**選別**メニュー。
[並べ替え] ダイアログが表示されます。
1. 並べ替えオプションを選択します。

通常、並べ替えはリストに対して実行されます。これは、データが列に表示される連続したデータのグループとして定義されます。

**Microsoft Excel の [並べ替え] ダイアログ ボックス**

![todo:画像_代替_文章](data-sorting_1.png)

## **Aspose.Cells でデータを並べ替える**

Aspose.Cells は[**データソーター**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)昇順または降順でデータをソートするために使用されるクラス。クラスにはいくつかの重要なメンバーがあります。たとえば、次のようなメソッドです。[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) ... [**setKey2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key2)と[**setOrder1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order1) ... [**setOrder2**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Order2).これらのメンバーは、並べ替えられたキーを定義し、キーの並べ替え順序を指定するために使用されます。

データの並べ替えを実装する前に、キーを定義し、並べ替え順序を設定する必要があります。クラスは、[**選別**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()ワークシートのセル データに基づいてデータの並べ替えを実行するために使用されるメソッド。

の[**選別**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort()) メソッドは、次のパラメーターを受け入れます。

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)、ワークシートのセル。
- [**セルエリア**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)、セルの範囲。データの並べ替えを適用する前にセル領域を定義します。

この例では、Aspose.Cells API を使用してデータを並べ替える方法を示します。この例では、テンプレート ファイル "Book1.xls" を使用し、最初のワークシートのデータ範囲 (A1:B14) のデータを並べ替えます。

この例では、Microsoft Excel で作成されたテンプレート ファイル「Book1.xls」を使用します。

**データを含むテンプレート Excel ファイル**

![todo:画像_代替_文章](data-sorting_2.png)

以下のコードを実行すると、出力 Excel ファイルからわかるように、データが適切に並べ替えられます。

**データを並べ替えてExcelファイルを出力**

![todo:画像_代替_文章](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

分類する*左から右へ*、 使用[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight)属性。

{{% /alert %}}

## **背景色によるデータの並べ替え**

Excel には、背景色に基づいてデータを並べ替える機能があります。同じ機能は、Aspose.Cells を使用して提供されます。[**データソーター**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter)どこ[**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL_COLOR)で使用できます[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int) ) を使用して、背景色に基づいてデータを並べ替えます。指定された色を含むすべてのセル[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int))、関数は SortOrder 設定に従って上または下に配置され、残りのセルの順序はまったく変更されません。

以下は、この機能をテストするためにダウンロードできるサンプル ファイルです。

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **先行トピック**
- [カスタムソートリストを使用して列のデータをソートする](/cells/ja/java/sort-data-in-column-with-custom-sort-list/)
- [データの並べ替え時の並べ替え警告の指定](/cells/ja/java/specifying-sort-warning-while-sorting-data/)

