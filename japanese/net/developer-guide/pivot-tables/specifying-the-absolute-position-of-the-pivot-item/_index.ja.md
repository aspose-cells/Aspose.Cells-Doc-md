---
title: ピボット アイテムの絶対位置の指定
type: docs
weight: 50
url: /ja/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

場合によっては、ユーザーはピボット アイテムの絶対位置を指定する必要があります。

- 追加した[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)親ノードに関係なく、すべての PivotItems の位置インデックスを指定するために使用できるプロパティ。追加した[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)同じ親ノードの下の PivotItems で位置インデックスを指定するために使用できるプロパティ。
- 追加した[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)count 値に基づいて項目を上下に移動するためのメソッド。 count は PivotItem を上下に移動する位置の数です。カウント値がゼロより小さい場合、アイテムは上に移動し、カウント値がゼロより大きい場合、PivotItem は下に移動します。ブール型の isSameParent パラメータは、移動操作を同じ親ノードで実行する必要があるかどうかを指定しますか否か。
- 廃止された*PivotItem.Move(整数カウント)*メソッドしたがって、新しく追加されたメソッドを使用することをお勧めします[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)代わりは。

{{% /alert %}}

次のサンプル コードは、ピボット テーブルを作成し、同じ親ノードでピボット アイテムの位置を指定します。ダウンロードできます[ソースエクセル](5112632.xlsx)と[エクセル出力](5112619.xlsx)参照用のファイル。出力された Excel ファイルを開くと、ピボット アイテム「4H12」が親「K11」の 0 番目の位置にあり、「DIF400」が 3 番目の位置にあることがわかります。同様に、CA32 は位置 1 にあり、AAA3 は位置 2 にあります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

使用する前に PivotTable.RefreshData および PivotTable.CalculateData メソッドを呼び出す必要があることに注意してください。[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)プロパティと[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法。

{{% /alert %}}
