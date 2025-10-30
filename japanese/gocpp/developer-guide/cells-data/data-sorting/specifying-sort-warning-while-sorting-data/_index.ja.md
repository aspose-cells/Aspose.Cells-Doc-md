---
title: GolangをC++経由で使用して並べ替え時に警告を指定する
linktitle: データをソートする際のソート警告の指定
type: docs
weight: 140
url: /ja/go-cpp/specifying-sort-warning-while-sorting-data/
description: ソート時の警告を指定する方法をAspose.Cells for C++ APIを使って学びます。
keywords: データをソートする際にソート警告を追加する、データをソートする際にソート警告を設定する、データをソートする際にソート警告を選択する。
---

## **可能な使用シナリオ**

テキストデータ{11, 111, 22}を考慮してください。このテキストデータは、テキストにおいて111が22より前に来るためにソートされます。しかし、このデータをテキストではなく数字としてソートしたい場合、それは{11, 22, 111}になります。Aspose.Cellsはこの問題に対処するために{0}プロパティを提供します。このプロパティを**true**に設定すると、テキストデータが数値データとしてソートされます。次のスクリーンショットは、テキストデータが数字のように見える場合にMicrosoft Excelで表示されるソート警告を示しています。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **サンプルコード**

次のサンプルコードは、上記で説明した[**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortasnumber/)プロパティの使用方法を説明しています。詳細については、サンプルExcelファイル（43352075.xlsx）とそれに対応する出力Excelファイル（43352076.xlsx）を確認してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSortWarningWhileSortingData.go" >}}
