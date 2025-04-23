---
title: データをソートする際のソート警告の指定
type: docs
weight: 140
url: /ja/net/specifying-sort-warning-while-sorting-data/
description: Aspose.Cells for .NET APIを使用してデータをソートする際にソート警告を指定する方法を学んでください。
keywords: データをソートする際にソート警告を追加する、データをソートする際にソート警告を設定する、データをソートする際にソート警告を選択する。
---

## **可能な使用シナリオ**

テキストデータ{11, 111, 22}を考慮してください。このテキストデータは、テキストにおいて111が22より前に来るためにソートされます。しかし、このデータをテキストではなく数字としてソートしたい場合、それは{11, 22, 111}になります。Aspose.Cellsはこの問題に対処するために{0}プロパティを提供します。このプロパティを**true**に設定すると、テキストデータが数値データとしてソートされます。次のスクリーンショットは、テキストデータが数字のように見える場合にMicrosoft Excelで表示されるソート警告を示しています。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **サンプルコード**

次のサンプルコードは、上記で説明した[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)プロパティの使用方法を説明しています。詳細については、サンプルExcelファイル（43352075.xlsx）とそれに対応する出力Excelファイル（43352076.xlsx）を確認してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
{{< app/cells/assistant language="csharp" >}}
