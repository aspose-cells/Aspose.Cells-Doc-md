---
title: カスタムソートリストを使用して列のデータをソートする
type: docs
weight: 210
url: /ja/java/sort-data-in-column-with-custom-sort-list/
---
## **考えられる使用シナリオ**

カスタム リストを使用して、列のデータを並べ替えることができます。これは、[DataSorter.AddKey(int キー、SortOrder 順、文字列 customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)） 方法。ただし、この方法は、カスタム リスト内の項目にコンマが含まれていない場合にのみ機能します。 「USA、US」、「中国、CN」などのカンマがある場合は、使用する必要があります[DataSorter.AddKey(int キー、SortOrder 順、文字列 customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)） 方法。ここで、最後のパラメーターは文字列ではなく、文字列の配列です。

## **カスタムソートリストを使用して列のデータをソートする**

次のサンプル コードでは、DataSorter.AddKey(int key, SortOrder order, String[]customList) メソッドを使用して、カスタム ソート リストでデータをソートする方法について説明します。をご覧ください[サンプル Excel ファイル](50528359.xlsx)このコードで使用され、[出力エクセルファイル](50528358.xlsx)それによって生成されます。次のスクリーンショットは、実行時のサンプル Excel ファイルに対するコードの効果を示しています。

![todo:画像_代替_文章](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
