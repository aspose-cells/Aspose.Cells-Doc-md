---
title: 子报表
type: docs
weight: 90
url: /zh/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

子报表可以嵌入在表项中。格式为：&subreport{ReportName=您的报告名称; 参数1名称=参数1值; 参数2名称=参数2值; ...}

**报告定义中的子报表** 

![todo:image_alt_text](sub-report_1.png)

在这个示例中，子报表的名称是“销售订单详细信息”。它有一个参数，SalesOrderNumber。该参数的值为 EmpSalesDetail.SalesOrderNumber。
### **子报表的限制**
1. 子报表应该使用Aspose.Cells.ReportingServices Designer进行设计。
1. 子报表只能嵌入到表组行中，组行除了子报表以外不能包含任何元素。不允许将子报表嵌入到表详细行或页脚行中。
1. 目前不支持多层嵌套。子报表不能包含嵌入的报表。

{{% /alert %}} 
###### **本部分包括以下主题:** 
- [创建表项](/cells/zh/reportingservices/creating-table-item/)
- [添加子报表项](/cells/zh/reportingservices/add-sub-report-item/)
