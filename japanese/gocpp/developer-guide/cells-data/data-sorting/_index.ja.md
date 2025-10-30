---
title: GolangをC++経由でデータの並べ替えを行う
linktitle: データソート
type: docs
weight: 130
url: /ja/go-cpp/sort-data-of-excel/
description: Aspose.Cells for C++ APIを使用してデータの並べ替え方を学びます。
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

Aspose.Cellsは、昇順または降順でデータをソートするために使用される[**DataSorter**](https://reference.aspose.com/cells/go-cpp/datasorter/)クラスを提供しています。このクラスには、Key1などの重要なメンバーがあります。これらのメンバーはソートされたキーを定義し、Keyの並べ替えを指定するために使用されます。

データソートを実装する前に、キーを定義してソート順を設定する必要があります。このクラスは、ワークシート内のセルデータに基づいてデータのソートを実行するために使用される [**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) メソッドを提供しています。

[**Sort**](https://reference.aspose.com/cells/go-cpp/datasorter/sort_cells_int_int_int_int/) メソッドは、以下のパラメータを受け入れます:

- [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/)、基になるワークシートのセル。
- [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/)、セル範囲。データソーティングを適用する前にセル領域を定義します。

この例では、Microsoft Excelで作成した「Book1.xls」という名前のテンプレートファイルを使用します。以下のコードを実行した後、データが適切にソートされます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting.go" >}}
{{% alert color="primary" %}}

もし*LeftToRight*でソートしたい場合は、[**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortlefttoright/)属性を使用します。

{{% /alert %}}

### **背景色でデータをソートする**

Excelでは背景色に基づいてデータをソートする機能が提供されています。この機能はAspose.Cellsを使用してDataSorterで提供され、[**SortOnType**](https://reference.aspose.com/cells/go-cpp/sortontype/)によって[**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/)で背景色に基づいてデータをソートすることができます。指定された色を含むすべてのセルは、SortOrderの設定と残りのセルの順序に従って、上部または下部に配置されます。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSorting-1.go" >}}
## **高度なトピック**
- [カスタムソートリストを使用した列内のデータの並べ替え](/cells/ja/cpp/sort-data-in-column-with-custom-sort-list/)
- [データソート時の警告の指定](/cells/ja/cpp/specifying-sort-warning-while-sorting-data/)
