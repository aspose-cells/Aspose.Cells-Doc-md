---
title: 格式化智能标记
type: docs
weight: 20
url: /zh/net/formatting-smart-markers/
---
## **复制样式属性**
有时，在使用智能标记时，您想要复制包含智能标记标签的单元格的样式。为此，您可以使用智能标记标签的 CopyStyle 属性。
### **使用智能标记从 Cells 复制样式**
此示例使用一个简单的模板 Microsoft Excel 文件，在 A2 和 B2 单元格中有两个标记。粘贴在单元格 B2 中的标记使用 CopyStyle 属性，而单元格 A2 中的标记则不使用。应用简单格式（例如，将字体颜色设置为**红色的**并将单元格填充颜色设置为**黄色的**).

执行代码时，Aspose.Cells将格式复制到B列中的所有记录，但不保留A列中的格式。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **添加自定义标签**
### **介绍**
在使用智能标记的分组数据功能时，有时您需要将自己的自定义标签添加到摘要行。您还希望将列的名称与该标签连接起来，例如“订单小计”。 Aspose.Cells 为您提供 Label 和 LabelPosition 属性，因此您可以将自定义标签放置在智能标记中，同时在分组数据中与小计行连接。
### **添加自定义标签以与智能标记中的小计行连接**
这个例子使用了[数据文件](96927971.xlsx)和一个[模板文件](96927972.xlsx)细胞中有一些标记。执行代码时，Aspose.Cells 将一些自定义标签添加到分组数据的摘要行中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
