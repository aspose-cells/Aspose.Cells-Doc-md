---
title: データソート
type: docs
weight: 130
url: /ja/net/sort-data-of-excel/
description: Aspose.Cells for .NET APIを使用してデータをソートする方法を学ぶ。
keywords: 昇順または降順でデータをソートし、背景色に基づいてデータをソートする。
---

{{% alert color="primary" %}}

データソーティングはMicrosoft Excelの多くの便利な機能の1つです。ユーザーはデータを整理してスキャンしやすくするためにデータを並べ替えることができます。Aspose.Cellsを使用すると、ワークシートのデータをアルファベット順または数値順に並べ替えることができます。

{{% /alert %}}

## **Microsoft Excel でのデータのソート**

Microsoft Excel でデータをソートするには:

1. **ソート**メニューから**データ**を選択します。ソートダイアログが表示されます。
1. ソートオプションを選択します。

一般的に、ソートはリスト上で実行されます。リストは、データが列に表示される連続したグループと定義されます。

## **Aspose.Cells でのデータのソート**

Aspose.Cellsは、昇順または降順でデータをソートするために使用される[**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)クラスを提供しています。このクラスには、Key1などの重要なメンバーがあります。これらのメンバーはソートされたキーを定義し、Keyの並べ替えを指定するために使用されます。

データソートを実装する前に、キーを定義してソート順を設定する必要があります。このクラスは、ワークシート内のセルデータに基づいてデータのソートを実行するために使用される [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index) メソッドを提供しています。

[**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1) メソッドは、以下のパラメータを受け入れます:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)、基になるワークシートのセル。
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)、セル範囲。データソーティングを適用する前にセル領域を定義します。

この例では、Microsoft Excelで作成した「Book1.xls」という名前のテンプレートファイルを使用します。以下のコードを実行した後、データが適切にソートされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

もし*LeftToRight*でソートしたい場合は、[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright)属性を使用します。

{{% /alert %}}

### **背景色でデータをソートする**

Excelでは背景色に基づいてデータをソートする機能が提供されています。この機能はAspose.Cellsを使用してDataSorterで提供され、[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype)によって[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)で背景色に基づいてデータをソートすることができます。指定された色を含むすべてのセルは、SortOrderの設定と残りのセルの順序に従って、上部または下部に配置されます。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **高度なトピック**
- [カスタムソートリストを使用した列内のデータの並べ替え](/cells/ja/net/sort-data-in-column-with-custom-sort-list/)
- [データソート時の警告の指定](/cells/ja/net/specifying-sort-warning-while-sorting-data/)
