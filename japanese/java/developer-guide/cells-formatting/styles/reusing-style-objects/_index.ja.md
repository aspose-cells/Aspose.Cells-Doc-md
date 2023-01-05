---
title: スタイル オブジェクトの再利用
type: docs
weight: 60
url: /ja/java/reusing-style-objects/
---
{{% alert color="primary" %}}

スタイル オブジェクトを再利用すると、メモリが節約され、プログラムの実行速度が向上します。

{{% /alert %}}

ワークシート内の広範囲のセルに書式を適用するには:

1. スタイル オブジェクトを作成します。
1. 属性を指定します。
1. 範囲内のセルにスタイルを適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

上記と同じプロセスを以下のように行うこともできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

なぜなら[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ） と[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) メソッドはメモリ使用量が大幅に少なく効率的であり、古いほど*Cell.getStyle()*不要なメモリを大量に消費するプロパティは、のリリースで削除されました*Aspose.Cells 7.1.0*.

{{% /alert %}}
