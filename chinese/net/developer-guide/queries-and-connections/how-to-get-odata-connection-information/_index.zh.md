---
title: 如何获取OData连接信息
type: docs
weight: 60
url: /zh/net/how-to-get-odata-connection-information/
---

## **获取OData连接信息**

可能存在需要从Excel文件中提取OData信息的情况。 Aspose.Cells提供[**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup)属性，返回Excel文件中存在的DataMashup信息。此信息由[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)类表示。[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)类提供[**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas)属性，返回[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)集合。从[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)中，您可以访问[**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula)和[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem)。

以下代码片段演示了使用这些类来检索OData信息。

以下代码片段中使用的源文件，请参考附件。

[源文件](96928098.xlsx)

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **控制台输出**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
