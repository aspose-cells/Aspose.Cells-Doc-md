---
title: スマート マーカーを使用してデータを結合する際の通知の取得
type: docs
weight: 20
url: /ja/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells API は、[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)クラスへ[スマート マーカーの操作](https://docs.aspose.com/cells/net/smart-markers/)フォーマットと数式が配置されている場所[デザイナー スプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)で処理し、[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)クラスを使用して、指定されたスマート マーカーに従ってデータを入力します。場合によっては、セル参照または処理中の特定のスマート マーカーに関する通知を取得する必要がある場合があります。これは、[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback)プロパティと[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) Aspose.Cells for .NET 8.6.2 のリリースで公開されたインターフェース。

{{% /alert %}} 

次のコードは、[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback)コールバックを処理する新しいクラスを定義するインターフェース[WorkbookDesigner.プロセス](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)方法。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



残りのプロセスには、スマート マーカーを含むデザイナー スプレッドシートの読み込みが含まれます。[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)データソースを設定して処理します。例を単純にするために、以下のスナップショットに示すように、2 つのスマート マーカーのみを含む事前定義されたデザイナー スプレッドシートを使用しました。このスナップショットでは、データ ソースが動的に作成され、指定されたスマート マーカーに従ってデータがマージされます。

|![todo:画像_代替_文章](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
