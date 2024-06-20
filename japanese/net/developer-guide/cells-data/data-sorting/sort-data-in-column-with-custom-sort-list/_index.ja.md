---
title: カスタムソートリストで列内のデータをソートする
type: docs
weight: 290
url: /ja/net/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for .NET APIを使用してカスタムリストを使用して列のデータをソートする方法を学んでください。
keywords: カスタムリストを使用して列のデータをソートする、カスタムリストによるデータのソート。
---

## **可能な使用シナリオ**

列のデータをカスタムリストを使用してソートできます。これは[**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)メソッドを使用することで行えます。ただし、このメソッドはカスタムリストのアイテムにカンマが含まれていない場合にのみ機能します。カンマが含まれる場合（"USA,US"、"China,CN"など）は、[**DataSorter.AddKeyメソッド（Int32、SortOrder、String[]）**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3)メソッドを使用する必要があります。ここで、最後のパラメータはStringではなくStringの配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

[**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3)メソッドを使用してカスタムソートリストでデータをソートする方法を説明したサンプルコードをご覧ください。このコードで使用された[サンプルExcelファイル](50528327.xlsx)とそれによって生成される[output Excel file](50528328.xlsx)を確認してください。次のスクリーンショットには、サンプルExcelファイルにコードが及ぼす効果が表示されています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
