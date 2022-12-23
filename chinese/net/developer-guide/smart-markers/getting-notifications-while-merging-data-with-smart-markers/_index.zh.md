---
title: 使用智能标记合并数据时获取通知
type: docs
weight: 20
url: /zh/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells API 提供[工作簿设计器](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)类[使用智能标记](https://docs.aspose.com/cells/net/smart-markers/)格式和公式放置在[设计师电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/)然后处理[工作簿设计器](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)类根据指定的智能标记填充数据。有时，可能需要获取有关单元格引用或正在处理的特定智能标记的通知。这可以通过使用[工作簿设计器.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback)财产和[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback)接口随着 Aspose.Cells for .NET 8.6.2 的发布而暴露。

{{% /alert %}} 

下面的一段代码演示了[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback)定义处理回调的新类的接口[WorkbookDesigner.进程](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)方法。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



其余过程包括加载包含智能标记的设计器电子表格[工作簿设计器](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)并通过设置数据源进行处理。为了使示例保持简单，我们使用了一个仅包含两个智能标记的预定义设计器电子表格，如下面的快照所示，其中动态创建数据源以根据指定的智能标记合并数据。

|![待办事项：图片_替代_文本](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
