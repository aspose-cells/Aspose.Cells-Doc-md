##Sub-reports
We incorporated support for Embedding a Sub-Report in a Table group row. The format is:
&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......}
### **Example**
**A sub-report in a table**
![todo:image_alt_text](sub-reports_1.png)
In the example, the name of sub-report is “Sales Order Detail”. It has one parameter, *SalesOrderNumber*. The value of the parameter is *EmpSalesDetail.SalesOrderNumber.*
#### **Restrictions on using Sub-Reports**
- The sub-report should be designed with the Aspose.Cells.Reporting Services Designer tool.
- The Sub-Report can only be embedded in the table group row and the group row cannot contain other elements except the Sub-Report. Embedding a Sub-Report in the table detail rows or footer rows is not allowed.
- Currently, nesting more than one level is not supported. The Sub-Report cannot contain embedded report.
