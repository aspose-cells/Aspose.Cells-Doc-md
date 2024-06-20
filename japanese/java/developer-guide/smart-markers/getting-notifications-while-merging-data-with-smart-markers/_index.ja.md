---
title: Smart Markers でデータをマージする際の通知の取得
type: docs
weight: 460
url: /ja/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.CellsのAPIは[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)クラスを提供しており、[スマートマーカー](/cells/ja/java/smart-markers/)を使用する際に、フォーマットや数式が[デザイナースプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)に配置され、[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)クラスによって指定されたスマートマーカーに従ってデータが入力されます。時々、セル参照や特定のスマートマーカーの処理に関する通知が必要になることがあります。これは[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)プロパティと[リリースAspose.Cells for Java 8.6.2](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)インターフェースとして公開されたISmartMarkerCallBackを使用することで実現できます。

{{% /alert %}} 
## **スマートマーカーを使用してデータをマージする際の通知の取得**
以下のコードは、[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)インターフェースの使用例を示し、新しいクラスを定義し、[WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\))メソッドのコールバックを処理します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


例をシンプルかつ明確にするために、次のスニペットでは空のデザイナースプレッドシートを作成し、スマートマーカーを挿入し、動的に作成されたデータソースで処理します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
