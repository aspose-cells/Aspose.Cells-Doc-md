---
title: 子报告
type: docs
weight: 20
url: /zh/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

我们合并了对在表组行中嵌入子报告的支持。格式为：

&=subreport{ReportName=你的报表名称;参数 1 名称 = 参数 1 值； parameter2 名称 = parameter2 值；……} 

{{% /alert %}} 
### **例子**
**表格中的子报表** 

![待办事项：图像_替代_文本](sub-reports_1.png)

在示例中，子报表的名称为“销售订单明细”。它有一个参数，*销售订单号*.参数的值为*EmpSalesDetail.SalesOrderNumber。*
#### **使用子报告的限制**
- 应使用 Aspose.Cells.Reporting Services Designer 工具设计子报表。
- 子报表只能嵌入到表组行中，组行不能包含子报表以外的其他元素。不允许在表格详细信息行或页脚行中嵌入子报告。
- 目前不支持嵌套多于一层。子报表不能包含嵌入式报表。
