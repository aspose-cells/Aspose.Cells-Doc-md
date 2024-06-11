---
title: 如何获取OData连接信息
type: docs
weight: 60
url: /zh/java/how-to-get-odata-connection-information/
---

## **获取OData连接信息**

在某些情况下，开发人员可能需要从 Excel 文件中提取 OData 信息。Aspose.Cells 提供了返回 Excel 文件中存在的 DataMashup 信息的 [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) 属性。这些信息由 DataMashup 类表示。DataMashup 类提供了 PowerQueryFormulas 属性，该属性返回 PowerQueryFormulaCollction 集合。通过 PowerQueryFormulaCollction，您可以访问 PowerQueryFormula 和 PowerQueryFormulaItem。

以下代码片段演示了使用这些类来检索OData信息。

以下代码片段中使用的源文件，请参考附件。

[源文件](ODataSample.xlsx)

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **控制台输出**

连接名称：Orders

名称：Source

值：OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

名称：Orders_table

数值：Source{[Name="订单",Signature="表"]}[数据]
