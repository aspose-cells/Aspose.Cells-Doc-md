---
title: 子报告
type: docs
weight: 90
url: /zh/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

子报告可以嵌入表项目。格式为：&=subreport{ReportName=您的报告名称；参数1名称=参数1值；参数2名称=参数2值；...}

**报告定义中的子报告** 

![todo:image_alt_text](sub-report_1.png)

在示例中，子报告名称为“销售订单详情”。它有一个参数，SalesOrderNumber。参数的值为 EmpSalesDetail.SalesOrderNumber。
### **子报告的限制**
1. 子报表应设计为 Aspose.Cells.ReportingServices 设计师。
1. 子报表只能嵌入在表组行中，组行中不能包含任何元素，除了子报表。不允许在表的详细行或页脚行中嵌入子报表。
1. 目前不支持多层嵌套。子报表不能包含内嵌报表。

{{% /alert %}} 
###### **本节包括以下主题:** 
- [创建表项](/cells/zh/reportingservices/creating-table-item/)
- [添加子报表项目](/cells/zh/reportingservices/add-sub-report-item/)
