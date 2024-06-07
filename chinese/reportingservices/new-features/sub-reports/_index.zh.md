---
title: 子报表
type: docs
weight: 20
url: /zh/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

我们增加了对将子报表嵌入到表组行中的支持。格式为：

&=subreport{ReportName=您的报表名称; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **例子**
**表中的子报表** 

![todo:image_alt_text](sub-reports_1.png)

例如，子报表的名称是“销售订单详细信息”。它有一个参数，*SalesOrderNumber*。参数的值为*EmpSalesDetail.SalesOrderNumber*。
#### **使用子报表的限制**
- 子报表应使用Aspose.Cells.Reporting Services Designer工具设计。
- 子报表只能嵌入在表组行中，组行不能包含子报表以外的其他元素。不允许将子报表嵌入表详细行或页脚行。
- 当前不支持嵌套超过一层。子报表不能包含嵌入式报表。
