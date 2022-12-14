---
title: 使用智能标记合并数据时获取通知
type: docs
weight: 460
url: /zh/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells API 提供[工作簿设计器](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)类[使用智能标记](/cells/zh/java/smart-markers/)格式和公式放置在[设计师电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)然后处理[工作簿设计器](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)类根据指定的智能标记填充数据。有时，可能需要获取有关单元格引用或正在处理的特定智能标记的通知。这可以通过使用[工作簿设计器.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)财产和[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)接口随着 Aspose.Cells for Java 8.6.2 的发布而暴露。

{{% /alert %}} 
## **使用智能标记合并数据时获取通知**
下面的一段代码演示了[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)定义处理回调的新类的接口[工作簿设计器.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


为了使示例简单明了，以下代码片段创建了一个空的设计器电子表格，插入了一个智能标记并使用动态创建的数据源对其进行处理。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
