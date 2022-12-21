---
title: ピボットアイテムの絶対位置を指定する
type: docs
weight: 40
url: /ja/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

場合によっては、ユーザーはピボット項目の絶対位置を指定する必要があります。Aspose.Cells API は、このユーザー要件を達成するためのいくつかの新しいプロパティとメソッドを公開しました。

- 追加した[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)親ノードに関係なく、すべての PivotItems の位置インデックスを指定するために使用できるプロパティ。追加した[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)同じ親ノードの下の PivotItems で位置インデックスを指定するために使用できるプロパティ。
- 追加した[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)メソッドを使用して、カウント値に基づいて項目を上下に移動します。カウントは、PivotItem を上下に移動する位置の数です。カウント値が 0 より小さい場合、アイテムは上に移動し、カウント値が 0 より大きい場合、PivotItem は下に移動します。ブール型の isSameParent パラメーターは、移動操作を同じ親ノードで実行する必要があるかどうかを指定します。いいえ。
- 廃止された*PivotItem.move(整数カウント)*メソッド、したがって、新しく追加されたメソッドを使用することをお勧めします[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)） 代わりは。

に電話する必要があることに注意してください。[**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ） と[**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ）メソッドを使用する前に[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)プロパティと[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)） 方法。

{{% /alert %}}

## サンプルコード

次のサンプル コードは、ピボット テーブルを作成し、同じ親ノードでピボット アイテムの位置を指定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
