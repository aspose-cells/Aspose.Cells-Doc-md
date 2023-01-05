---
title: 範囲データのみをコピー
type: docs
weight: 600
url: /ja/net/copy-range-data-only/
---
{{% alert color="primary" %}}

あるセル範囲から別のセル範囲にデータをコピーし、書式設定ではなくデータのみをコピーする必要がある場合があります。 Aspose.Cells はこの機能を提供します。

この記事では、Aspose.Cells を使用してデータの範囲をコピーするサンプル コードを提供します。

{{% /alert %}}

この例は、次の方法を示しています。

1. ワークブックを作成します。
1. 最初のワークシートのセルにデータを追加します。
1. 作成する[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. 作成する[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)指定されたフォーマット属性を持つオブジェクト。
1. スタイルの書式設定を範囲に適用します。
1. 別のセル範囲を作成します。
1. 最初の範囲のデータをこの 2 番目の範囲にコピーします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataOnly-1.cs" >}}
