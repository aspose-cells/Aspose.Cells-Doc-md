---
title: 格式化SmartMarkers
type: docs
weight: 20
url: /zh/java/formatting-smart-markers/
---

## **复制样式属性**
有时，在使用SmartMarkers时，您希望复制包含Smart Marker标记的单元格的样式。您可以使用Smart Marker标记的CopyStyle属性来实现此目的。
### **从带有Smart Markers的单元格中复制样式**
此示例使用一个具有A2和B2单元格中两个标记的简单模板Microsoft Excel文件。粘贴到单元格B2中的标记使用CopyStyle属性，而在单元格A2中的标记则不使用。应用简单的格式（例如，将字体颜色设置为**红色**，将单元格填充颜色设置为**黄色**）。

该示例使用了带有几个标记的 [模板文件](template1.xlsx) 中的单元格。执行代码时，Aspose.Cells会将格式复制到B列所有记录，但在A列中不保留格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **添加自定义标签**
### **介绍**
在使用Smart Markers的数据分组功能时，有时需要向摘要行添加自定义标签。您还希望将列名与该标签连接起来，例如"订单小计"。Aspose.Cells为您提供了Label和LabelPosition属性，因此您可以在Smart Markers中放置自定义标签，同时与数据分组中的小计行连接。
### **在Smart Markers中添加要连接到小计行的自定义标签**
该示例使用了带有几个标记的 [模板文件](template.xlsx) 中的单元格。执行代码时，Aspose.Cells会为分组数据的摘要行添加一些自定义标签。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
