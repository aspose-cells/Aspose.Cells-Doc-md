---
title: 以百分比格式输入GridWeb工作表单元格数据
type: docs
weight: 1010
url: /zh/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **可能的使用场景**
GridWeb现在支持用户以百分比格式输入单元格数据，如3%，单元格中的数据将自动格式化为3.00%。但是，您必须将单元格样式设置为百分比格式，即GridTableItemStyle.NumberType为9或10。数字9将3%格式化为3%，但数字10将3%格式化为3.00%。

{{% alert color="primary" %}} 

如果未将单元格样式设置为百分比格式，则输入数据3%将显示为0.03。

{{% /alert %}} 
## **以百分比格式输入GridWeb工作表的单元格数据**
以下示例代码将单元格A1 GridTableItemStyle.NumberType设为10，因此输入的数据3%将自动格式化为3.00%，如屏幕截图所示。

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **示例代码**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






