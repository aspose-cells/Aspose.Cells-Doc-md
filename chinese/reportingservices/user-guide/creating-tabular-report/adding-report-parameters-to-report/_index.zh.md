---
title: 添加报告参数到报告
type: docs
weight: 60
url: /zh/reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

Aspose.Cells的报告模板支持报告服务报告参数作为包含报告服务参数标记的单元格的数据源。请参阅[Aspose.Cells模板和智能标记](/cells/zh/reportingservices/aspose-cells-template-and-smart-markers/)来了解报告服务参数标记。报告参数通常放置在表头或页脚的文本区域中。

{{% /alert %}} 
### **添加报告参数**
要向报告添加报告参数：

1. 选择一个单元格。 

   **选择一个单元格** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. 单击Aspose.Cells.Report.Designer工具栏上的插入公式（

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. 从左侧的参数面板中选择**参数**。
   所有参数都列在右侧面板中。 
1. 选择一个参数，在本示例中，我们选择了EmpID。
1. 双击参数，以使表达式出现在表单顶部的编辑器中。
   参数有两个数据属性：标签和值（默认属性是值）。 

   **选择一个参数** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. 在示例中，参数的标签应在报告中显示，因此修改表达式为Parameters!EmpID.Label。 

   **修改参数** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. 点击**确定**。
   所选单元格包含报告参数标记。 

   **报告参数插入到单元格中** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
