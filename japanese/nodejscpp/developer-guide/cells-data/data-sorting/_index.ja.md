---
title: データソート
type: docs
weight: 130
url: /ja/nodejs-cpp/sort-data-of-excel/
description: Aspose.Cells for Node.js via C++を使用してデータを並べ替える方法を学びます。
keywords: 昇順または降順でデータをソートし、背景色に基づいてデータをソートする。
---

{{% alert color="primary" %}}

データの並べ替えはMicrosoft Excelの多くの便利な機能の一つです。これにより、ユーザーはデータを整理しやすくなります。Aspose.Cells for Node.js via C++は、Microsoft Excelと同じ方法でデータをアルファベット順または数字順に並べ替えることができます。

{{% /alert %}}

## **Microsoft Excel でのデータのソート**

Microsoft Excel でデータをソートするには:

1. **ソート**メニューから**データ**を選択します。ソートダイアログが表示されます。
1. ソートオプションを選択します。

一般的に、ソートはリスト上で実行されます。リストは、データが列に表示される連続したグループと定義されます。

## **Aspose.Cells でのデータのソート**

Aspose.Cells for Node.js via C++は、昇順または降順に並べ替えるための[**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter)クラスを提供します。このクラスには、Key1...Key3やOrder1...Order3などの重要なメンバーがあります。これらは並べ替えのキーを定義し、並べ替え順序を指定するために使用されます。

データソートを実装する前に、キーを定義してソート順を設定する必要があります。このクラスは、ワークシート内のセルデータに基づいてデータのソートを実行するために使用される [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) メソッドを提供しています。

[**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) メソッドは、以下のパラメータを受け入れます:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)、基になるワークシートのセル。
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)、セル範囲。データソーティングを適用する前にセル領域を定義します。

この例では、Microsoft Excelで作成した「Book1.xls」という名前のテンプレートファイルを使用します。以下のコードを実行した後、データが適切にソートされます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

もし*LeftToRight*でソートしたい場合は、[**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-)属性を使用します。

{{% /alert %}}

### **背景色でデータをソートする**

Excelは背景色に基づいてデータを並べ替える機能を提供しています。同じ機能がAspose.Cells for Node.js via C++のDataSorterを使用して提供されており、[**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/)のセルカラーを[**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-)内で使用して、背景色に基づいてデータを並べ替えることができます。指定された色を含むすべてのセルは、SortOrder設定と他のセルの順序に従って上または下に配置され、その他のセルの順序は変更されません。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **高度なトピック**
- [カスタムソートリストを使用した列内のデータの並べ替え](/cells/ja/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [データソート時の警告の指定](/cells/ja/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="nodejs-cpp" >}}
