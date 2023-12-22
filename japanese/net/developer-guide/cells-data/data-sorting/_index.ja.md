---
title: データの並べ替え
type: docs
weight: 130
url: /ja/net/sort-data-of-excel/
description: Aspose.Cells for .NET API を使用してデータを並べ替える方法を学習します。
keywords: Sort data in ascending or descending order, Sort data based on the background color
---
{{% alert color="primary" %}}

データの並べ替えは、Excel の多くの便利な機能の 1 つです。これにより、ユーザーはデータを注文してスキャンしやすくなります。 Aspose.Cells を使用すると、開発者はワークシート データをアルファベット順または数値順に並べ替えることができます。これは、Microsoft Excel がデータを並べ替えるのと同じように機能します。

{{% /alert %}}

##  **Microsoft Excel でのデータの並べ替え**

Microsoft Excel でデータを並べ替えるには:

1. 選択する**データ**から**選別**メニュー。 [並べ替え]ダイアログが表示されます。
1. 並べ替えオプションを選択します。

一般に、並べ替えはリスト (データが列に表示される連続したデータのグループとして定義) に対して実行されます。

##  **Aspose.Cells でデータを並べ替える**

 Aspose.Cells は、[**データソーター**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)データを昇順または降順でソートするために使用されるクラス。このクラスには、Key1 ... Key3 や Order1 ... Order3 などのプロパティなど、いくつかの重要なメンバーがあります。これらのメンバーは、ソートされたキーを定義し、キーのソート順序を指定するために使用されます。

データの並べ替えを実装する前に、キーを定義し、並べ替え順序を設定する必要があります。クラスが提供するのは、[**選別**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)ワークシート内のセル データに基づいてデータの並べ替えを実行するために使用されるメソッド。

の[**選別**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)メソッドは次のパラメータを受け入れます。

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)、基礎となるワークシートのセル。
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)、セルの範囲。データの並べ替えを適用する前に、セル領域を定義します。

この例では、Microsoft Excel で作成したテンプレート ファイル「Book1.xls」を使用します。以下のコードを実行すると、データが適切にソートされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 *LeftToRight* を並べ替える場合は、[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright)属性。

{{% /alert %}}

###  **データを背景色で並べ替える**

Excel には、背景色に基づいてデータを並べ替える機能が用意されています。同じ機能は、DataSorter を使用して Aspose.Cells を使用して提供されます。[**ソートオンタイプ**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor は以下で使用できます。[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)背景色に基づいてデータを並べ替えます。指定された色を含むすべてのセル[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)、関数は SortOrder 設定に従って上または下に配置され、残りのセルの順序はまったく変更されません。

この機能をテストするためにダウンロードできるサンプル ファイルは次のとおりです。

[サンプルバックグラウンドファイル.xlsx](81920906.xlsx)

[出力サンプルBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

##  **アドバンストトピック**
- [カスタム並べ替えリストを使用して列内のデータを並べ替える](/cells/ja/net/sort-data-in-column-with-custom-sort-list/)
- [データのソート時のソート警告の指定](/cells/ja/net/specifying-sort-warning-while-sorting-data/)
