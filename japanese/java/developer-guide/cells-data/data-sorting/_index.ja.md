---
title: データソート
type: docs
weight: 90
url: /ja/java/sort-data-of-excel/
---

{{% alert color="primary" %}}

データソートは、Microsoft Excel の多くの便利な機能の1つです。これにより、データを整理してスキャンしやすくすることができます。

Aspose.Cells では、ワークシートデータをアルファベット順または数値順にソートすることができます。データのソートは、Microsoft Excel と同様の方法で機能します。

{{% /alert %}}

## **Microsoft Excel でのデータのソート**

Microsoft Excel でデータをソートするには:

1. **ソート** メニューから **データ** を選択します。
   ソートダイアログが表示されます。
1. ソートオプションを選択します。

一般的に、ソートはリスト上で実行されます。リストは、データが列に表示される連続したグループと定義されます。

**Microsoft Excel のソートダイアログボックス**

![todo:image_alt_text](data-sorting_1.png)

## **Aspose.Cells でのデータのソート**

Aspose.Cells は、昇順または降順でデータをソートするために使用する [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) クラスを提供しています。このクラスには、[**setKey1**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#Key1) メソッドなどの重要なメンバーがあります。これらのメンバーは、ソートされたキーを定義し、キーのソート順序を指定するために使用されます。

データソートを実装する前に、キーを定義してソート順を設定する必要があります。このクラスは、ワークシート内のセルデータに基づいてデータのソートを実行するために使用される [**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) メソッドを提供しています。

[**sort**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#sort--) メソッドは、以下のパラメータを受け入れます:

- [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)、ワークシートのセル。
- [**CellArea**](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)、セル範囲。データソーティングを適用する前にセル領域を定義します。

この例では、Aspose.Cells API を使用してデータをソートする方法を示します。この例では、テンプレートファイル「Book1.xls」を使用し、最初のワークシートのデータ範囲(A1:B14)をソートします。

この例では、Microsoft Excel で作成されたテンプレートファイル「Book1.xls」を使用します。

**データが入ったテンプレートのExcelファイル完了**

![todo:image_alt_text](data-sorting_2.png)

以下のコードを実行した後、出力されたExcelファイルから適切にデータがソートされていることがわかります。

**データがソートされた後の出力Excelファイル**

![todo:image_alt_text](data-sorting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DataSorting-DataSorting.java" >}}

{{% alert color="primary" %}}

*左から右へ* のソートには、[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortLeftToRight) 属性を使用します。

{{% /alert %}}

## **背景色でデータをソートする**

Excel は、背景色に基づいてデータをソートする機能を提供しています。この機能は、Aspose.Cells を使用して [**DataSorter**](https://reference.aspose.com/cells/java/com.aspose.cells/DataSorter) を使って同じ機能が提供されます。[**addKey()**](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-) 内で [**SortOnType.CELL_COLOR**](https://reference.aspose.com/cells/java/com.aspose.cells/sortontype#CELL-COLOR) を使用して、背景色に基づいてデータをソートします。指定した色が含まれる指定されたセル内のすべてのセルは、SortOrder の設定とその他のセルの順序に従って、先頭または最後尾に配置されます。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[sampleBackGroundFile.xlsx](sampleBackGroundFile.xlsx)

[outputsampleBackGroundFile.xlsx](outputsampleBackGroundFile.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

## **高度なトピック**
- [カスタムソートリストを使用した列内のデータの並べ替え](/cells/ja/java/sort-data-in-column-with-custom-sort-list/)
- [データソート時の警告の指定](/cells/ja/java/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="java" >}}
