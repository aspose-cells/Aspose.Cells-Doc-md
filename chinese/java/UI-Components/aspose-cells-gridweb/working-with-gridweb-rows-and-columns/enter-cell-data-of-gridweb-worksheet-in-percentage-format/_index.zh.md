---
title: 在GridWeb工作表的单元格中输入百分比格式的数据
type: docs
weight: 1010
url: /zh/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **可能的使用场景**
GridWeb现在支持用户以百分比格式（如3%）输入单元格数据，并且单元格中的数据将自动格式为3.00%。但是，您必须将单元格样式设置为百分比格式，即GridTableItemStyle.NumberType为9或10。数字9将以3%的格式显示，但数字10将以3.00%的格式显示。

{{% alert color="primary" %}} 

如果未将单元格样式设置为百分比格式，则输入数据3%将显示为0.03。

{{% /alert %}} 
## **在GridWeb工作表的单元格中输入百分比格式的数据**
以下示例代码将单元格A1的GridTableItemStyle.NumberType设置为10，因此输入的3%数据将自动格式为3.00%，如屏幕截图所示。

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **示例代码**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






