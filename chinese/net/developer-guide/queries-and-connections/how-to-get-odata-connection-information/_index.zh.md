---
title: 如何获取 OData 连接信息
type: docs
weight: 60
url: /zh/net/how-to-get-odata-connection-information/
---
## **获取 OData 连接信息**

在某些情况下，开发人员可能需要从 excel 文件中提取 OData 信息。 Aspose.Cells 提供了[**工作簿.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup)返回 Excel 文件中存在的 DataMashup 信息的属性。此信息由[**数据混搭**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)班级。这[**数据混搭**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)类提供了[**PowerQuery公式**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas)返回的属性[**PowerQuery公式集合**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)收藏。来自[**PowerQuery公式集合**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction)，您可以访问[**PowerQuery公式**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula)和[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

以下代码片段演示了如何使用这些类来检索 OData 信息。

附上以下代码片段中使用的源文件供您参考。

[源文件](96928098.xlsx)

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **控制台输出**

连接名称：订单

名称：来源

值：OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

名称：订单表

值：来源{[Name="Orders",Signature="table"]}[Data]