---
title: カスタムソートリストで列内のデータをソートする
type: docs
weight: 210
url: /ja/java/sort-data-in-column-with-custom-sort-list/
---

## **可能な使用シナリオ**

カスタムリストを使用して列のデータを並べ替えることができます。これは、[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-)メソッドを使用して行います。ただし、この方法は、カスタムリストのアイテムにカンマが含まれていない場合にのみ機能します。"USA, US"や"China, CN"のようにカンマが含まれている場合は、[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-)メソッドを使用してください。最後のパラメータはStringではなく、文字列配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

次のサンプルコードでは、DataSorter.AddKey(int key, SortOrder order, String[] customList) メソッドを使用してカスタムソートリストでデータをソートする方法を説明しています。このコードで使用される[sample Excel file](50528359.xlsx) と、それによって生成された[output Excel file](50528358.xlsx)をご覧ください。次のスクリーンショットは、サンプルExcelファイルに対するコードの効果を示しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
