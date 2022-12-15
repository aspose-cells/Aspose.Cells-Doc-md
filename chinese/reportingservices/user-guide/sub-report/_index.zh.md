---
title: 子报告
type: docs
weight: 90
url: /zh/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

子报表可以嵌入到表项中。格式为： &=subreport{ReportName=你的报表名称;参数 1 名称 = 参数 1 值；参数 2 名称 = 参数 2 值； ...}

**报表定义中的子报表** 

![待办事项：图像_替代_文本](sub-report_1.png)

在示例中，子报表的名称为“销售订单明细”。它有一个参数，SalesOrderNumber。该参数的值为 EmpSalesDetail.SalesOrderNumber。
### **子报告的限制**
1. 子报表应该用Aspose.Cells.ReportingServices Designer来设计。
1. 子报表只能嵌入到表组行中，组行不能包含子报表以外的任何元素。不允许在表格详细信息行或页脚行中嵌入子报告。
1. 目前不支持嵌套多于一层。子报表不能包含嵌入式报表。

{{% /alert %}} 
###### **本节包括以下主题：**
- [创建表项](/cells/zh/reportingservices/creating-table-item/)
- [添加子报告项](/cells/zh/reportingservices/add-sub-report-item/)
