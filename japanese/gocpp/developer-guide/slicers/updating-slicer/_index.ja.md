---
title: C++経由のGolangによるスライサーの更新
linktitle: スライサーの更新
type: docs
weight: 50
url: /ja/go-cpp/updating-slicer/
description: この記事は、Aspose.Cells for C++ APIを使用してスライサーを更新し、リンクされたピボットテーブルを更新する方法を示しています。
keywords: Aspose.Cells C++ でスライサーを更新する方法、スライサーの変更方法、C++でスライサーを調整する方法、スライサーアイテムの選択・解除方法。
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーを更新したい場合、アイテムを選択または解除すると、それに応じてスライサーテーブルまたはピボットテーブルが更新されます。[**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/)を使ってAspose.Cellsでスライサーアイテムを選択または解除し、その後[**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/)メソッドを呼び出してスライサーテーブルやピボットテーブルを更新してください。

## **スライサーの更新方法**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](67338475.xlsx) を読み込みます。スライサーの2番目と3番目の項目を選択解除し、スライサーを更新します。それからワークブックを[出力Excelファイル](67338476.xlsx)として保存します。スクリーンショットには、サンプルコードがサンプルExcelファイルに与えた影響が示されています。スクリーンショットでは、選択された項目を持つスライサーを更新することでピボットテーブルも更新されていることがわかります。

![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
