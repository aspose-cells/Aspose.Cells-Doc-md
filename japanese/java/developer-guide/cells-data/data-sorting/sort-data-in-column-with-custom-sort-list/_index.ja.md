---
title: カスタムソートリストで列内のデータをソートする
type: docs
weight: 210
url: /ja/java/sort-data-in-column-with-custom-sort-list/
---

## **可能な使用シナリオ**

カスタムリストを使用して列内のデータをソートすることができます。これは[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String))メソッドを使用して行われます。ただし、このメソッドは、カスタムリストのアイテムにカンマが含まれていない場合のみ機能します。"USA, US"、"China, CN"などのようにカンマが含まれている場合、[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String))メソッドを使用する必要があります。ここでは、最後のパラメータは文字列ではなく、文字列の配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

次のサンプルコードでは、DataSorter.AddKey(int key, SortOrder order, String[] customList) メソッドを使用してカスタムソートリストでデータをソートする方法を説明しています。このコードで使用される[sample Excel file](50528359.xlsx) と、それによって生成された[output Excel file](50528358.xlsx)をご覧ください。次のスクリーンショットは、サンプルExcelファイルに対するコードの効果を示しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
