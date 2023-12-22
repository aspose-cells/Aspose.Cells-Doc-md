---
title: Excelを使わずに凍結状態を確認する方法。
linktitle: 凍結状態
type: docs
weight: 190
url: /ja/net/how-to-check-frozen-state-of-excel-worksheet
description: この記事では、.NET API の C# Library を使用してプログラムで Excel ワークシートのフリーズ状態を確認する方法を説明します。
---
{{% alert color="primary" %}}

この記事では、Excel ワークシートのフリーズ状態をプログラムで確認する方法を学びます。
MS Excel では、ワークシートがフリーズされているか分割されているかを簡単に確認できます。しかし、CSharpでフリーズしているか分割されているかを確認する方法はありますか。
.Net の場合は Aspose.Cells を使用するだけで済みます。
{{% /alert %}}

##  **窓ガラスは凍っていますか**
.Net の Aspose.Cells を使用すると、ウィンドウがフリーズしているかどうか、ロックされている行と列の数を確認できます。

をご利用ください。[**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/)ウィンドウペインの状態を確認するプロパティ
ロックされた行と列を取得します[**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)方法。
1. ファイルを開くためのワークブックを構築します。
2. ワークシートがフリーズしていないか確認します。
3. ロックされた行と列を取得します

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}