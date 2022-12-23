---
title: 以百分比格式输入 Cell GridWeb 工作表数据
type: docs
weight: 80
url: /zh/net/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **可能的使用场景**
GridWeb 现在支持用户以百分比格式输入单元格数据，如 3%，单元格中的数据将自动格式化为 3.00%。但是，您必须将单元格样式设置为百分比格式，即 GridTableItemStyle.NumberType 9 或 10。数字 9 会将 3% 的格式设置为 3%，而数字 10 会将 3% 的格式设置为 3.00%。

{{% alert color="primary" %}} 

如果你没有设置单元格样式为百分比格式，那么输入数据3%会显示为0.03。

{{% /alert %}} 
## **以百分比格式输入 Cell GridWeb 工作表数据**
以下示例代码将单元格 A1 GridTableItemStyle.NumberType 设置为 10，因此输入数据 3% 会自动格式化为 3.00%，如屏幕截图所示。

![待办事项：图片_替代_文本](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **示例代码**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
