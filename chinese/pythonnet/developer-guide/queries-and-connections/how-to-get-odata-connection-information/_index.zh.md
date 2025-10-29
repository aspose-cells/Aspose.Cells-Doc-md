---
title: 如何获取OData连接信息
type: docs
weight: 60
url: /zh/python-net/how-to-get-odata-connection-information/
---

## **获取OData连接信息**

开发者有时可能需要从Excel文件中提取OData信息。Aspose.Cells for Python via .NET 提供了[**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup)属性，该属性返回Excel文件中的DataMashup信息。这些信息由[**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup)类表示。[**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup)类提供了[**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas)属性，该属性返回[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/)集合。通过[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/)，可以访问[**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula)和[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem)。

以下代码片段演示了使用这些类来检索OData信息。

以下代码片段中使用的源文件，请参考附件。

[源文件](96928098.xlsx)

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **控制台输出**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
