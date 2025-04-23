---
title: カスタムソートリストで列内のデータをソートする
type: docs
weight: 290
url: /ja/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: カスタムリストを使った列のデータソート方法について学びます。Aspose.Cells for Node.js via C++ APIを使用します。
keywords: カスタムリストを使用して列のデータをソートする、カスタムリストによるデータのソート。
---

## **可能な使用シナリオ**

カスタムリストを使って列データをソートできます。これは[**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-)メソッドを使用します。ただし、この方法はカスタムリスト内のアイテムにカンマが含まれていない場合のみ有効です。"USA,US"や"中国,CN"のようにカンマが含まれる場合は、[**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-)を使用してください。最後のパラメータは文字列の配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

以下のサンプルコードは、[カスタムソートリストを使用したデータソート](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-)の方法を示しています。サンプルExcelファイルと、このコードで生成された出力Excelファイルも併せてご覧ください。コード実行時のExcelファイルへの効果もスクリーンショットで紹介しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

