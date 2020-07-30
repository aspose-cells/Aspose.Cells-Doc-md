---
title : "Sub-reports" 
description : "" 
weight : 8026 
toc : false
type: docs
url: /reportingservices/newfeatures/sub-reports/
---

# Aspose.Cells for Reporting Services : Sub-reports


We incorporated support for Embedding a Sub-Report in a Table group row. The format is:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

### Example

**A sub-report in a table**  
![](https://docs2.aspose.com/cells/reportingservices/attachments/6094922/6193432.png)

In the example, the name of sub-report is “Sales Order Detail”. It has one parameter, *SalesOrderNumber*. The value of the parameter is *EmpSalesDetail.SalesOrderNumber.*

#### Restrictions on using Sub-Reports

*   The sub-report should be designed with the Aspose.Cells.Reporting Services Designer tool.
*   The Sub-Report can only be embedded in the table group row and the group row cannot contain other elements except the Sub-Report. Embedding a Sub-Report in the table detail rows or footer rows is not allowed.
*   Currently, nesting more than one level is not supported. The Sub-Report cannot contain embedded report.

## Attachments:

![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Sub Reports-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094922/6193432.png) (image/png)  

