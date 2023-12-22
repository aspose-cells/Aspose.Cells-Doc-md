---
title: 以百分比格式输入 GridWeb 工作表的 Cell 数据
type: docs
weight: 1010
url: /zh/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **可能的使用场景**
GridWeb 现在支持用户以百分比格式（如 3%）输入单元格数据，单元格中的数据将自动格式化为 3.00%。但是，您必须将单元格样式设置为百分比格式，即 GridTableItemStyle.NumberType a 9 或 10。数字 9 会将 3% 格式化为 3%，但数字 10 会将 3% 格式化为 3.00%。

{{% alert color="primary" %}} 

如果您尚未将单元格样式设置为百分比格式，则输入数据 3% 将显示为 0.03。

{{% /alert %}} 
##  **以百分比格式输入 GridWeb 工作表的 Cell 数据**
以下示例代码将单元格 A1 GridTableItemStyle.NumberType 设置为 10，因此输入数据 3% 自动格式化为 3.00%，如屏幕截图所示。

![待办事项：图像_替代_文本](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **示例代码**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






