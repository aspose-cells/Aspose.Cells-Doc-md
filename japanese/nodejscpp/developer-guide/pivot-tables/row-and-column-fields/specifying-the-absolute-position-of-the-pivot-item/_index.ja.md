---
title: ピボットアイテムの絶対位置を指定する
type: docs
weight: 50
url: /ja/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

時には、ユーザーがピボットアイテムの絶対位置を指定する必要があり、Aspose.Cells for Node.js via C++ APIはこれを実現するための新しいプロパティとメソッドをいくつか公開しています。

- 親ノードに関係なくすべてのPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-)プロパティが追加されました。- 同じ親ノード内のPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-)プロパティが追加されました。
- PivotItemを移動するための[**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-)メソッドが追加されました。こちらでは、移動する位置数（count）に基づいてアイテムを上または下に移動します。count値がゼロ未満の場合、アイテムは上に移動し、count値がゼロより大きい場合は、PivotItemは下に移動します。isSameParentパラメータは、移動操作を同じ親ノード内で実行するかどうかを指定します。
- *PivotItem.move(int count)*メソッドは廃止されたため、新たに追加された[**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-)メソッドを代わりに使用することを推奨します。

{{% /alert %}}

次のサンプルコードは、ピボットテーブルを作成し、その後、同じ親ノード内でのPivot Itemsの位置を指定しています。参照のために、[ソースExcel](5112632.xlsx)および[出力Excel](5112619.xlsx)ファイルをダウンロードできます。出力Excelファイルを開くと、「K11」の親での0番目の位置に「4H12」アイテムが、3番目の位置に「DIF400」が表示されます。同様に、CA32は1番目の位置にあり、AAA3は2番目の位置にあります。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

注意: [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-)、[**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-)プロパティおよび[**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-)メソッドを使用する前に、PivotTable.RefreshDataおよびPivotTable.CalculateDataメソッドを呼び出す必要があります。

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
