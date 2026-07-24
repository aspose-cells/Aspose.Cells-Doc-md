---
title: GolangとC++を使用してピボットアイテムの絶対位置を指定
linktitle: ピボットアイテムの絶対位置を指定する
type: docs
weight: 50
url: /ja/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Aspose.Cellsを使用してC++でピボットアイテムの絶対位置を指定する方法を学びます。
---

{{% alert color="primary" %}}

時々、ユーザーはピボットアイテムの絶対位置を指定する必要があります。Aspose.Cells APIはこの要件を達成するための新しいプロパティとメソッドを公開しています。

- 親ノードに関係なくすべてのPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/)プロパティが追加されました。- 同じ親ノード内のPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)プロパティが追加されました。
- [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/)メソッドを追加し、ピボットアイテムを上または下に移動させることができます。ここで、`count`は移動させる位置の数です。`count`の値が負の場合は上に移動し、正の場合は下に移動します。`isSameParent`は、移動操作が同じ親ノードで行われるかどうかを示すブール型のパラメータです。
- `PivotItem.Move(int count)`メソッドは廃止されました。したがって、新たに追加された[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/)メソッドの使用を推奨します。

{{% /alert %}}

以下のサンプルコードは、ピボットテーブルを作成し、同じ親ノード内のピボットアイテムの位置を指定します。[ソースExcel](5112632.xlsx)と[出力Excel](5112619.xlsx)をダウンロードして参考にしてください。出力Excelを開くと、「4H12」が親「K11」の0番目の位置にあり、「DIF400」は3番目の位置にあります。同様に、CA32は位置1、AAA3は位置2にあります。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

ご注意：`PivotTable.RefreshData`と`PivotTable.CalculateData`メソッドを呼び出す必要があることに注意してください。[**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/)、[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)プロパティおよび[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/)メソッドを使用する前に。

{{% /alert %}}
