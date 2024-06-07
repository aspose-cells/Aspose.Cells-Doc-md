---
title: 在使用Smart Markers合并数据时获取通知
type: docs
weight: 460
url: /zh/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API提供了[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) 类，用于[处理智能标记](/cells/zh/java/smart-markers/)，其中格式和公式被放置在[设计者电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)中，然后使用[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) 类根据指定的智能标记填充数据。有时，可能需要获取有关正在处理的单元引用或特定智能标记的通知。可以通过[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)属性和发布的Aspose.Cells for Java 8.6.2版本中的[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) 接口来实现。

{{% /alert %}} 
## **在合并智能标记数据时获取通知**
以下代码片段演示了使用[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) 接口定义一个处理[WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) 方法回调的新类。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


为了使示例简单明了，以下代码段创建了一个空的设计者电子表格，插入了一个智能标记，然后使用动态创建的数据源对其进行处理。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
