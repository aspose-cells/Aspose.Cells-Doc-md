---
title: ピボットアイテムの絶対位置を指定する
type: docs
weight: 50
url: /ja/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

ユーザーがピボットアイテムの絶対位置を指定する必要がある場合、Aspose.Cells APIはこれを実現するためのいくつかの新しいプロパティとメソッドを公開しています。

- 親ノードに関係なくすべてのPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)プロパティが追加されました。- 同じ親ノード内のPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)プロパティが追加されました。
- PivotItemを移動するための[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)メソッドが追加されました。こちらでは、移動する位置数（count）に基づいてアイテムを上または下に移動します。count値がゼロ未満の場合、アイテムは上に移動し、count値がゼロより大きい場合は、PivotItemは下に移動します。isSameParentパラメータは、移動操作を同じ親ノード内で実行するかどうかを指定します。
- *PivotItem.Move(int count)*メソッドは廃止されたため、新しく追加された[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)メソッドを使用することが推奨されています。

{{% /alert %}}

次のサンプルコードは、ピボットテーブルを作成し、その後、同じ親ノード内でのPivot Itemsの位置を指定しています。参照のために、[ソースExcel](5112632.xlsx)および[出力Excel](5112619.xlsx)ファイルをダウンロードできます。出力Excelファイルを開くと、「K11」の親での0番目の位置に「4H12」アイテムが、3番目の位置に「DIF400」が表示されます。同様に、CA32は1番目の位置にあり、AAA3は2番目の位置にあります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

注意: [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)、[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)プロパティおよび[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)メソッドを使用する前に、PivotTable.RefreshDataおよびPivotTable.CalculateDataメソッドを呼び出す必要があります。

{{% /alert %}}
