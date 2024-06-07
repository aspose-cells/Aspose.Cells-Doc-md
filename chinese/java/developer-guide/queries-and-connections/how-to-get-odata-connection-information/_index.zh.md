---
title: 如何获取OData连接信息
type: docs
weight: 60
url: /zh/java/how-to-get-odata-connection-information/
---

## **获取OData连接信息**

有时，开发人员可能需要从Excel文件中提取OData信息。Aspose.Cells提供了 [DataMashup](ODataSample.xlsx) 属性，它返回Excel文件中存在的DataMashup信息。这些信息由DataMashup类表示。DataMashup类提供了返回PowerQueryFormulaCollction集合的PowerQueryFormulas属性。从PowerQueryFormulaCollction，您可以访问PowerQueryFormula和PowerQueryFormulaItem。

以下代码片段演示了使用这些类来检索OData信息的用法。

以下代码片段中使用的源文件已附上供您参考。

[源文件](ODataSample.xlsx)

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **控制台输出**

连接名称：订单

名称：源

数值：OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

名称：Orders_table

数值：Source{[名称="Orders",签名="table"]}[数据]
