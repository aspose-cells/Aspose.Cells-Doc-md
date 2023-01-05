---
title: 如何获取 OData 连接信息
type: docs
weight: 60
url: /zh/java/how-to-get-odata-connection-information/
---
## **获取 OData 连接信息**

在某些情况下，开发人员可能需要从 excel 文件中提取 OData 信息。 Aspose.Cells 提供了[**工作簿.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)返回 Excel 文件中存在的 DataMashup 信息的属性。此信息由 DataMashup 类表示。 DataMashup 类提供返回 PowerQueryFormulaCollction 集合的 PowerQueryFormulas 属性。从 PowerQueryFormulaCollction，您可以访问 PowerQueryFormula 和 PowerQueryFormulaItem。

以下代码片段演示了如何使用这些类来检索 OData 信息。

附上以下代码片段中使用的源文件供您参考。

[源文件](ODataSample.xlsx)

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **控制台输出**

连接名称：订单

名称：来源

值：OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

名称：订单表

值：来源{[Name="Orders",Signature="table"]}[Data]