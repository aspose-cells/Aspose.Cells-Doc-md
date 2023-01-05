---
title: スマート マーカーを使用してデータを結合する際の通知の取得
type: docs
weight: 460
url: /ja/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells API は、[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)クラスへ[スマート マーカーの操作](/cells/ja/java/smart-markers/)フォーマットと数式が配置されている場所[デザイナー スプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)で処理し、[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)クラスを使用して、指定されたスマート マーカーに従ってデータを入力します。場合によっては、セル参照または処理中の特定のスマート マーカーに関する通知を取得する必要がある場合があります。これは、[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)プロパティと[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)Aspose.Cells for Java 8.6.2 のリリースで公開されたインターフェース。

{{% /alert %}} 
## **スマート マーカーを使用してデータをマージする際に通知を受け取る**
次のコードは、[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)コールバックを処理する新しいクラスを定義するインターフェース[WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


例を簡潔かつ簡潔にするために、次のスニペットでは、空のデザイナー スプレッドシートを作成し、スマート マーカーを挿入して、動的に作成されたデータ ソースで処理します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
