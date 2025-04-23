---
title: 行または列の固定解除
linktitle: ペインの固定解除
type: docs
weight: 190
url: /ja/net/unfreeze-rows-or-columns-of-excel-worksheet
description: この記事では、C# ライブラリと .NET API を使用して、Excel ワークシートの行、列、またはペインをプログラムで固定解除する方法について学びます。
keywords: ペインの固定解除、行の固定解除、列の固定解除、ウィンドウの固定解除
---

## **紹介**

この記事では、Excelファイルの行や列、またはウィンドウを非固定にする方法について学びます。Excelファイルのワークシートが凍結されている場合、ワークシートを非固定にするか凍結された行や列を調整したいことがあります。


## **Excelで**

1. 表示タブ > 固定ウィンドウ > 固定ウィンドウの解除 をクリックします。

**![Excel でのペインの固定解除](Unfreeze-Panes.png)**




## **Aspose.Cells for .Net による行、列、またはペインの固定解除**
Aspose.Cells for .Net でペインを簡単に固定解除できます。[**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes) メソッドを使用してペインの固定解除を行ってください。

1. 凍結したファイルを開くためにワークブックを作成します。
2. Worksheet.UnFreezePanes() メソッドを使用してペインを固定解除します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

添付 [サンプルソースの Excel ファイル](Frozen.xlsx) です。
{{< app/cells/assistant language="csharp" >}}
