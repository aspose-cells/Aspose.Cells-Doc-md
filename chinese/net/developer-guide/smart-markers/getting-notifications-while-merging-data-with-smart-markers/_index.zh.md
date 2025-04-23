---
title: 在使用智能标记合并数据时获取通知
type: docs
weight: 20
url: /zh/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells APIs 提供 [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) 类来处理 [智能标记](https://docs.aspose.com/cells/net/smart-markers/)，其中格式和公式放置在 [设计者电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/) 中，然后使用 [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) 类根据指定的智能标记填充数据。有时，可能需要获取有关所处理的单元格引用或特定智能标记的通知。这可以通过 [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) 属性和 [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) 接口来实现，该接口在 Aspose.Cells for .NET 8.6.2 版本发布时公开。

{{% /alert %}} 

以下代码片段演示了[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) 接口的用法，定义了一个处理[WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) 方法的新类。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



其余的过程包括使用[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) 加载包含智能标记的设计电子表格，并通过设置数据源处理它。 为了保持示例简单，我们使用一个预定义的设计师电子表格，其中只包含两个智能标记，如下面的快照所示，数据源是动态创建的，以根据指定的智能标记合并数据。

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
