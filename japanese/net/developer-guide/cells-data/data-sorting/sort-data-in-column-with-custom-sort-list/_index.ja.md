---
title: カスタムソートリストを使用して列のデータをソートする
type: docs
weight: 290
url: /ja/net/sort-data-in-column-with-custom-sort-list/
---
## **考えられる使用シナリオ**

カスタム リストを使用して、列のデータを並べ替えることができます。これは、[**DataSorter.AddKey(int キー、SortOrder 順、文字列 customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)方法。ただし、この方法は、カスタム リスト内の項目にコンマが含まれていない場合にのみ機能します。 「USA,US」、「China,CN」などのカンマがある場合は、[**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) メソッド。ここで、最後のパラメーターは文字列ではなく、文字列の配列です。

## **カスタムソートリストを使用して列のデータをソートする**

次のサンプル コードは、[**DataSorter.AddKey メソッド (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) カスタムソートリストでデータをソートするメソッド。このコードで使用している【サンプルExcelファイル】(50528327.xlsx)と、それによって生成された【出力Excelファイル】(50528328.xlsx)をご覧ください。次のスクリーンショットは、実行時のサンプル Excel ファイルに対するコードの効果を示しています。

![todo:画像_代替_文章](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
