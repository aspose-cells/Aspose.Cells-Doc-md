---
title: GolangをC++経由で使用し、カスタム並べ替えリストで列のデータを並べ替える
linktitle: カスタムソートリストで列内のデータをソートする
type: docs
weight: 290
url: /ja/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for C++ APIを使用して、カスタムリストを用いた列のデータ並べ替え方法を学びます。
keywords: カスタムリストを使用して列のデータをソートする、カスタムリストによるデータのソート。
---

## **可能な使用シナリオ**

カスタムリストを使用して列のデータを並べ替えることができます。これは [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) メソッドを使用して行います。ただし、この方法は、カスタムリストのアイテムにカンマ（,）が含まれていない場合にのみ機能します。もし "USA,US" や "中国,CN" のようにカンマが含まれている場合は、[**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) メソッドを使用する必要があります。ここで、最後のパラメータは文字列ではなく文字列の配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

以下のサンプルコードは、[**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) メソッドを使用したカスタムソートリストによるデータの並べ替え方法を示しています。コードで使用されている [サンプルExcelファイル](50528327.xlsx) と、それによって生成された [出力Excelファイル](50528328.xlsx) を参照してください。以下のスクリーンショットは、コード実行時のサンプルExcelファイルに対する効果を示しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
