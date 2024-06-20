---
title: ピボットアイテムの絶対位置を指定する
type: docs
weight: 40
url: /ja/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

ユーザーがピボットアイテムの絶対位置を指定する必要がある場合、Aspose.Cells API はこのユーザー要件を満たすためにいくつかの新しいプロパティとメソッドを公開しています。

- 親ノードに関係なくすべてのPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)プロパティが追加されました。- 同じ親ノード内のPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)プロパティが追加されました。
- 移動する位置のカウント値に基づいてアイテムを上下に移動するための [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) メソッドが追加されました。カウント値がゼロより小さい場合、アイテムが上に移動し、カウント値がゼロより大きい場合、PivotItem が下に移動します。同じ親ノード内で移動操作を行うかどうかを指定するブール型の isSameParent パラメータが含まれています。
- *PivotItem.move(int count)* メソッドが廃止されたため、代わりに新たに追加されたメソッド [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) を使用することが推奨されます。

なお、これらのプロパティとメソッドを使用する前に、必ず [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) および [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) メソッドを呼び出す必要があります。

{{% /alert %}}

## サンプルコード

次のサンプルコードでは、ピボットテーブルを作成し、同じ親ノード内での Pivot Items の位置を指定しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
