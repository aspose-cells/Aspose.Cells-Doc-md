---
title: 在使用Smart Markers合并数据时获取通知
type: docs
weight: 20
url: /zh/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells APIs provide the [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) class to [work with Smart Markers](https://docs.aspose.com/cells/net/smart-markers/) where the formatting & formulas are placed in the [designer spreadsheets](/cells/zh/net/what-is-a-designer-spreadsheet/) and then processed with [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) class to fill up the data according to specified Smart Markers. Sometimes, it may be required to get the notifications about the cell reference or the particular Smart Marker being processed. This can be achieved using the [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) property and [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interface exposed with the release of Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

以下代码片段演示了如何使用[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback)接口来定义一个负责[WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)方法的回调的新类。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



剩余的流程包括加载包含智能标记的设计师电子表格，使用[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)加载它并设置数据源进行处理。为了保持示例简单，我们使用一个预定义的设计师电子表格，只包含两个智能标记，如下面的快照所示，其中数据源是动态创建的，以根据指定的智能标记合并数据。

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
