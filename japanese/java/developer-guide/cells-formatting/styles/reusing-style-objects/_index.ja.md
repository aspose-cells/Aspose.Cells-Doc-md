---
title: スタイルオブジェクトの再利用
type: docs
weight: 60
url: /ja/java/reusing-style-objects/
---

{{% alert color="primary" %}}

スタイルオブジェクトを再利用することでメモリを節約し、プログラムを高速に実行することができます。

{{% /alert %}}

ワークシート内の大きな範囲のセルにフォーマットを適用するには:

1. スタイルオブジェクトを作成します。
1. 属性を指定します。
1. 範囲のセルにスタイルを適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

上記で説明したプロセスと同様に実行できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--)と[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-)メソッドは、メモリをはるかに少なく効率的に使用するため、以前の*Cell.getStyle()*プロパティ（不必要なメモリを大量に消費していた）は*Aspose.Cells 7.1.0*のリリース時に削除されました。

{{% /alert %}}
