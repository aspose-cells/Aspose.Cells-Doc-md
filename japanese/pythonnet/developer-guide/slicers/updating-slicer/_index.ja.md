---
title: スライサーの更新
type: docs
weight: 50
url: /ja/python-net/updating-slicer/
description: Aspose.Cells for Python via .NETでスライサーを更新する方法を学ぶ。
keywords: PythonライブラリAspose.Cells for Python Excelを使用したExcelのスライサーの更新、Aspose.Cells for Pythonを使ってExcelなしでスライサーを更新する。
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーを更新する場合、そのアイテムを選択または選択解除すると、スライサーテーブルまたはピボットテーブルが更新されます。Aspose.Cells for Python via .NETを使用してスライサーアイテムを選択または選択解除し、その後[**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#)メソッドを呼び出してスライサーテーブルまたはピボットテーブルを更新してください。

## **Aspose.Cells for Python Excel Libraryを使用したスライサーの更新方法**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](67338475.xlsx) を読み込みます。スライサーの2番目と3番目の項目を選択解除し、スライサーを更新します。それからワークブックを[出力Excelファイル](67338476.xlsx)として保存します。スクリーンショットには、サンプルコードがサンプルExcelファイルに与えた影響が示されています。スクリーンショットでは、選択された項目を持つスライサーを更新することでピボットテーブルも更新されていることがわかります。

![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
