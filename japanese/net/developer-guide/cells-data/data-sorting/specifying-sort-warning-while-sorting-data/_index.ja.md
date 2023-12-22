---
title: データのソート時のソート警告の指定
type: docs
weight: 140
url: /ja/net/specifying-sort-warning-while-sorting-data/
description: Aspose.Cells for .NET API を使用してデータを並べ替えるときに並べ替え警告を指定する方法を学習します。
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **考えられる使用シナリオ**

このテキスト データ、つまり {11, 111, 22} を考慮してください。このテキスト データは、テキストの観点からは 111 が 22 の前に来るため、並べ替えられます。ただし、このデータをテキストとしてではなく数値として並べ替えたい場合は、数値的には 111 が 22 の後に来るため、{11, 22, 111} になります。 Aspose.Cellsが提供します[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)この問題に対処するためのプロパティ。このプロパティを設定してください**真実**テキストデータは数値データとしてソートされます。次のスクリーンショットは、数値データのように見えるテキスト データを並べ替えるときに Microsoft Excel によって表示される並べ替え警告を示しています。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

##  **サンプルコード**

次のサンプル コードは、[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)先ほど説明したプロパティ。チェックしてください[サンプル Excel ファイル](43352075.xlsx)そして[Excelファイルを出力](43352076.xlsx)さらに助けが必要です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
