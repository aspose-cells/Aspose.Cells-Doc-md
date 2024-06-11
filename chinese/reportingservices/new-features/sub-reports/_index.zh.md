---
title: 子报表
type: docs
weight: 20
url: /zh/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

我们增加了对在表组行中嵌入子报表的支持。格式为：

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **示例**
**表中的子报表** 

![todo:image_alt_text](sub-reports_1.png)

在示例中，子报表的名称是“销售订单详细信息”。它有一个参数，*SalesOrderNumber*。参数的值为*EmpSalesDetail.SalesOrderNumber*。
#### **使用子报表的限制**
- 子报表应使用 Aspose.Cells.Reporting Services Designer 工具设计。
- 子报表只能嵌入在表格组行中，组行不能包含除子报表之外的其他元素。不允许将子报表嵌入在表格细节行或页脚行中。
- 目前不支持超过一级的嵌套。子报表不能包含嵌入报表。
