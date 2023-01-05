---
title: 将报表参数添加到报表
type: docs
weight: 60
url: /zh/reportingservices/adding-report-parameters-to-report/
---
{{% alert color="primary" %}} 

Aspose.Cells' 报表模板支持将 Reporting Services 报表参数作为包含 Reporting Services 参数标记的单元格的数据源。请参阅[Aspose.Cells 模板和智能标记](/cells/zh/reportingservices/aspose-cells-template-and-smart-markers/)了解 Reporting Services 参数标记。报表参数通常放置在表头或表尾的文本区域。

{{% /alert %}} 
### **添加报告参数**
向报告添加报告参数：

1. 选择一个单元格。

   **选择一个单元格** 

![待办事项：图片_替代_文本](adding-report-parameters-to-report_1.png)




1. 单击 Aspose.Cells.Report.Designer 工具栏上的插入公式 (

![待办事项：图片_替代_文本](adding-report-parameters-to-report_2.png)

).

1. 选择**参数**从左侧的参数面板。
所有参数都列在右侧面板中。
1. 选择一个参数，在示例中，我们选择了 EmpID。
1. 双击参数，使表达式出现在窗体顶部的编辑器中。
一个参数有两个数据属性：label 和 value（默认属性是 value）。

   **选择参数** 

![待办事项：图片_替代_文本](adding-report-parameters-to-report_3.png)




1. 在示例中，参数的标签应显示在报告中，因此将表达式修改为 Parameters!EmpID.Label。

   **修改参数** 

![待办事项：图片_替代_文本](adding-report-parameters-to-report_4.png)




1. 点击**好的**.
所选单元格包含一个报告参数标记。

   **插入到单元格中的报告参数** 

![待办事项：图片_替代_文本](adding-report-parameters-to-report_5.png)
