---
title: カスタム並べ替えリストを使用して列内のデータを並べ替える
type: docs
weight: 290
url: /ja/net/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for .NET API を使用して、カスタム リストを使用して列内のデータを並べ替える方法を学習します。
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **考えられる使用シナリオ**

カスタム リストを使用して、列内のデータを並べ替えることができます。これは次を使用して実行できます[**DataSorter.AddKey(int キー、SortOrder 順序、String CustomList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)方法。ただし、この方法は、カスタム リスト内の項目の中にカンマが含まれていない場合にのみ機能します。 「USA,US」、「China,CN」などのカンマがある場合は、[**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) メソッド。ここで、最後のパラメータは文字列ではなく文字列の配列です。

##  **カスタム並べ替えリストを使用して列内のデータを並べ替える**

次のサンプル コードは、[**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey の使用方法を説明しています) /methods/3) カスタム並べ替えリストを使用してデータを並べ替えるメソッド。をご覧ください。[サンプル Excel ファイル](50528327.xlsx)このコードで使用されており、[Excelファイルを出力](50528328.xlsx)それによって生み出されたもの。次のスクリーンショットは、実行時のサンプル Excel ファイルのコードの影響を示しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
