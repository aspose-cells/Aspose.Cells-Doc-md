---
title: データソート
type: docs
weight: 130
url: /ja/python-net/sort-data-of-excel/
description: Aspose.Cells for for Python via .NET APIを使用してデータをソートする方法を学ぶ。
keywords: Python Excelライブラリ、Pythonで昇順または降順でデータをソートする方法、背景色に基づいてデータをソートするPython。
---

{{% alert color="primary" %}}

データのソートはMicrosoft Excelの多くの便利な機能の1つです。これにより、データをスキャンしやすくするためにデータを順番に並べることができます。Aspose.Cells for for Python via .NETは、ワークシートのデータをアルファベット順または数字順に並べ替えることができます。これはMicrosoft Excelがデータをソートする方法と同じです。

{{% /alert %}}

## **Microsoft Excel でのデータのソート**

Microsoft Excel でデータをソートするには:

1. **ソート**メニューから**データ**を選択します。ソートダイアログが表示されます。
1. ソートオプションを選択します。

一般的に、ソートはリスト上で実行されます。リストは、データが列に表示される連続したグループと定義されます。

## **Aspose.Cells for for Python via .NETを使用したデータのソート**

Aspose.Cells for for Python via .NETはデータを昇順または降順にソートするための[**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter)クラスを提供しています。このクラスには、Key1...Key3やOrder1...Order3などの重要なメンバーがあります。これらのメンバーはソートされたキーを定義し、キーソートの順序を指定するのに使用されます。

データソートを実装する前に、キーを定義してソート順を設定する必要があります。このクラスは、ワークシート内のセルデータに基づいてデータのソートを実行するために使用される [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) メソッドを提供しています。

[**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) メソッドは、以下のパラメータを受け入れます:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)、基になるワークシートのセル。
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)、セル範囲。データソーティングを適用する前にセル領域を定義します。

この例では、Microsoft Excelで作成した「Book1.xls」という名前のテンプレートファイルを使用します。以下のコードを実行した後、データが適切にソートされます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

もし*LeftToRight*でソートしたい場合は、[**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/)属性を使用します。

{{% /alert %}}

### **Aspose.Cells for for Python via .NET Excel Libraryを使用した背景色を利用したデータのソート**

Excelは背景色に基づいてデータをソートする機能を提供しています。同じ機能はAspose.Cells for for Python via .NETを使用して、DataSorterで提供されています。[**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/)によって、[**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any)で背景色に基づいてデータをソートすることができます。[**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any)内で指定された色を含むすべてのセルは、SortOrderの設定に従ってトップまたはボトムに配置され、残りのセルの順序は全く変更されません。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **高度なトピック**
- [カスタムソートリストを使用した列内のデータの並べ替え](/cells/ja/python-net/sort-data-in-column-with-custom-sort-list/)
- [データソート時の警告の指定](/cells/ja/python-net/specifying-sort-warning-while-sorting-data/)
