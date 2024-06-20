---
title: Excelなしで凍結状態をチェックする方法。
linktitle: 凍結状態
type: docs
weight: 190
url: /ja/net/how-to-check-frozen-state-of-excel-worksheet
description: この記事では、.NET APIを使用してC#ライブラリでExcelワークシートの凍結状態をプログラムで確認する方法について学びます。

---

## **紹介**

この記事では、Excelワークシートの凍結状態をプログラムで確認する方法について学びます。MS Excelでワークシートが凍結されているか分割されているかは簡単に見つけることができますが、CSharpでそれが凍結されているか分割されているかを見つける方法はありますか。Aspose.Cells for .Netを使用すると簡単に行うことができます。

## **ウィンドウペインは凍っていますか**
.NetのAspose.Cellsを使用すると、ウィンドウが凍結されているかどうか、そしてロックされている行と列がいくつあるかをチェックできます。

ウィンドウペインの状態をチェックするには[**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/)プロパティを使用してください 
また、[**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)メソッドを使用してロックされた行と列を取得できます。
1. ファイルを開くためのワークブックを作成します。
2. ワークシートが凍結しているかどうかを確認します。
3. ロックされた行および列を取得します

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
