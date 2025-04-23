---
title: スライサーの更新
type: docs
weight: 50
url: /ja/net/updating-slicer/
description: この記事では、Aspose.Cells for .NET APIでスライサーを更新し、関連するピボットテーブルを更新する方法を示しています。
keywords: Aspose.Cells C#でスライサーを更新する方法、スライサーを変更するC#、C#でスライサーを調整する方法、スライサーの項目を選択または選択解除する方法。
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーを更新する場合は、その項目を選択または選択解除すると、スライサーテーブルまたはピボットテーブルが更新されます。Aspose.Cellsを使用してスライサーの項目を選択または選択解除し、その後、[**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) メソッドを呼び出してスライサーテーブルまたはピボットテーブルを更新してください。

## **スライサーの更新方法**

次のサンプルコードは、既存のスライサーを含む [サンプルExcelファイル](67338475.xlsx) を読み込みます。スライサーの2番目と3番目の項目を選択解除し、スライサーを更新します。それからワークブックを[出力Excelファイル](67338476.xlsx)として保存します。スクリーンショットには、サンプルコードがサンプルExcelファイルに与えた影響が示されています。スクリーンショットでは、選択された項目を持つスライサーを更新することでピボットテーブルも更新されていることがわかります。

![todo:image_alt_text](updating-slicer_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
