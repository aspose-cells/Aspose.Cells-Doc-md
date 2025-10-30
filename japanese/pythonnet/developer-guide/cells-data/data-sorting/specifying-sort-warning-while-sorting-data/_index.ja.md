---
title: データをソートする際のソート警告の指定
type: docs
weight: 140
url: /ja/python-net/specifying-sort-warning-while-sorting-data/
description: Aspose.Cells for Python via .NET API を使用してデータを並べ替える際にソート警告を指定する方法を学びます。
keywords: Python Excel ライブラリ、データを並べ替える際にソート警告を追加、データを並べ替える際にソート警告を設定、データを並べ替える際にソート警告を選択
---

## **可能な使用シナリオ**

このテキストデータ{11, 111, 22}を考慮してください。このテキストデータはソートされていますが、テキストとして111は22の前に来るためです。しかし、このデータをテキストではなく数値としてソートしたい場合、それは{11, 22, 111}になります。なぜなら、数値的には111は22の後に来るからです。Aspose.Cells for Python via .NETはこの問題を解決するための{0}プロパティを提供します。このプロパティを**true**に設定すると、テキストデータは数値データとしてソートされます。次のスクリーンショットは、Microsoft Excelが数値データに見えるテキストデータをソートする際に表示される警告を示しています。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **サンプルコード**

次のサンプルコードは、上記で説明した[**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/)プロパティの使用方法を説明しています。詳細については、サンプルExcelファイル（43352075.xlsx）とそれに対応する出力Excelファイル（43352076.xlsx）を確認してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
{{< app/cells/assistant language="python-net" >}}
