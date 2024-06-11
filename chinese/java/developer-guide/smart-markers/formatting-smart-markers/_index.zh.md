---
title: 格式化 Smart Markers
type: docs
weight: 20
url: /zh/java/formatting-smart-markers/
---

## **复制样式属性**
有时，使用 Smart Markers 时，您希望复制包含 Smart Marker 标记的单元格的样式。您可以使用 Smart Markers 标记的 CopyStyle 属性来实现此目的。
### **从包含 Smart Markers 的单元格复制样式**
此示例使用一个简单的模板 Microsoft Excel 文件，其中包含两个 A2 和 B2 单元格中的标记。粘贴在 B2 单元格中的标记使用 CopyStyle 属性，而 A2 单元格中的标记则不使用。应用简单的格式（例如，将字体颜色设置为 **红色**，单元格填充颜色设置为 **黄色**）。

此示例使用 [模板文件](template1.xlsx)，其中在单元格中有几个标记。当执行代码时，Aspose.Cells 将格式复制到 B 列中的所有记录，但不保留 A 列中的格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **添加自定义标签**
### **介绍**
在使用 Smart Markers 的分组数据功能时，有时您需要向汇总行添加自定义标签。您还希望将列的名称与该标签连接起来，例如 "订单的小计"。Aspose.Cells 为您提供了 Label 和 LabelPosition 属性，因此您可以将自定义标签放置在 Smart Markers 中，并在分组数据中将其与小计行连接起来。
### **将自定义标签添加到智能标记中以与小计行连接**
此示例使用一个包含少量标记的[模板文件](template.xlsx)。执行代码时，Aspose.Cells会为分组数据的汇总行添加一些自定义标签。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
