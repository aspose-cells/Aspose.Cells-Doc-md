---
title: Smart Markers でデータをマージする際の通知の取得
type: docs
weight: 20
url: /ja/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells のAPIでは、[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) クラスが提供されており、[Smart Markers](https://docs.aspose.com/cells/net/smart-markers/) を扱うための [designer spreadsheets](/cells/ja/net/what-is-a-designer-spreadsheet/) に書式や数式を配置し、その後 [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) クラスを使用して指定された Smart Markers に従ってデータを埋めることができます。時には、セル参照や特定の Smart Marker の処理について通知を受け取る必要があります。これは、[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) プロパティと、リリースAspose.Cells for .NET 8.6.2で公開された [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) インターフェースを使用して実現できます。

{{% /alert %}} 

[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) インターフェースの使用例



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



残りの処理は、[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) で Smart Markers を含むテンプレートを読み込み、データソースを設定して処理することです。この例では、簡単のために、データソースを動的に作成し、下のスナップショットに表示されているように、2つのSmart Markers を含む事前定義のデザイナースプレッドシートを使用しています。

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
