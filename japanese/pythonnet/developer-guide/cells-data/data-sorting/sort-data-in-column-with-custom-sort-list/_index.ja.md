---
title: カスタムソートリストで列内のデータをソートする
type: docs
weight: 290
url: /ja/python-net/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for Python via .NET API を使用してカスタムリストを使用して列内のデータを並べ替える方法を学びます。
keywords: Python Excel ライブラリ、Python カスタムソートリストを使用して列内のデータを並べ替える、Python カスタムリストによるデータの並べ替え
---

## **可能な使用シナリオ**

カスタムリストを使用して列内のデータを並べ替えるには、[**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) メソッドを使用できます。 ただし、このメソッドは、カスタムリスト内の項目にカンマが含まれていない場合にのみ機能します。 "USA,US"、「China,CN」など、カンマが含まれる場合は、 [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) メソッドを使用する必要があります。 ここで、最後のパラメータは文字列ではなく、文字列の配列です。

## **カスタムソートリストを使用した列内のデータの並べ替え**

以下のサンプルコードは、カスタムソートリストを使用してデータを並べ替える方法を説明しています。 このコードで使用される [サンプル Excel ファイル](50528327.xlsx) と、それによって生成される [出力 Excel ファイル](50528328.xlsx) を参照してください。 以下のスクリーンショットは、サンプル Excel ファイルにコードが与える効果を示しています。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
{{< app/cells/assistant language="python-net" >}}
