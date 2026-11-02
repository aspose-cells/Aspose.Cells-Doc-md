---
title: Golang via C++ を使用してピボットテーブル内のピボットフィールドをグループ化
linktitle: Golang via C++ を使用してピボットテーブル内のピボットフィールドをグループ化
description: Aspose.Cells for Go via C++ を使用して、ピボットテーブル内のピボットフィールドをグループ化する方法を学びます。
keywords: Aspose.Cells, Aspose.Cells for Go via C++, ピボットテーブル, ピボットフィールド, ピボットフィールドのグループ化, GroupBy, PivotField, 日付のグループ化, Go
type: docs
weight: 80
url: /ja/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
Microsoft Excel では、ピボットテーブル**内で**ピボットフィールドをグループ化できます。ピボットフィールドに関連するデータ量が多い場合、データをセクションごとにグループ化すると便利です。Aspose.Cells にも、[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) メソッドでピボットフィールドをグループ化する機能が用意されています。

## **ピボットテーブル内のピボットフィールドをグループ化**
次のサンプルコードは[サンプル Excel ファイル](64716818.xlsx) を読み込み、[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) メソッドを使用して最初のピボットフィールドをグループ化します。次に、ピボットテーブルを更新し、データを計算し、ワークブックを[出力 Excel ファイル](64716817.xlsx) として保存します。スクリーンショットには、サンプル Excel ファイルにサンプルコードを適用した結果を示しています。スクリーンショットから可以看出、最初のピボットフィールドが月および四半期ごとにグループ化されています。
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}