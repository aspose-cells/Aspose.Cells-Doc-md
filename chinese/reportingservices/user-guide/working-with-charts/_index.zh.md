---
title: 处理图表
type: docs
weight: 110
url: /zh/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells 报表模板支持 Microsoft Excel 图表。每次执行报表时，图表都将用最新数据填充。 

{{% /alert %}} 

要向报表模板添加图表：

1. 首先，创建将成为图表数据源的数据集。
   下面，我们使用随 SQL Server Reporting Services 2005 发货的 AdventureWorks 示例数据库，并创建一个名为 Sales 的数据集。
   此 SQL 定义数据集： 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



请参阅 [数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/) 了解更多有关在 Aspose.Cells.Report.Designer 中创建数据源和数据集的信息。

1. 根据 [创建表格报表](/cells/zh/reportingservices/creating-tabular-report/) 中的说明创建表格报表。我们为该示例创建的报表如下。表是图表的数据源。 

![todo:image_alt_text](working-with-charts_1.png)




1. 在 Microsoft Excel 中，单击 **插入** 菜单，然后选择 **图表**。
1. 点击**下一步**。 

![todo:image_alt_text](working-with-charts_2.png)




1. 单击 **系列** 选项卡。 

![todo:image_alt_text](working-with-charts_3.png)




1. 单击 **添加**。 

![todo:image_alt_text](working-with-charts_4.png)




1. 在对话框中，将 Series1 (季度系列) 的值设置为表的第一个数据字段。
   在该示例中，即“CompanySales!$C$3:$C$3”。第一个 $C$3 是“季度”的第一行索引，第二个 $C$3 是“季度”的最后一行索引的占位符，在渲染时将用表格数据的实际行索引替换。将类别(X)轴标签设置为“=CompanySales!$C$3:$C$3”。 

![todo:image_alt_text](working-with-charts_5.png)




1. 单击 **添加** 以添加另一个系列。
   在示例中，我们添加了销售系列。 
1. 将Series2（销售系列）的值设置为表格的第二个数据字段。
   在示例中，它是“CompanySales!$D$3:$D$3”。 第一个$D$3是“销售”的第一行索引，第二个$D$3是“销售”的最后一行索引的占位符，并将在呈现时替换为表格数据的实际行索引。 
1. 点击**下一个**继续。 

![todo:image_alt_text](working-with-charts_6.png)




1. 在对话框中，设置图表标题和分类（X）轴。
1. 单击**完成**以完成工作。 

![todo:image_alt_text](working-with-charts_7.png)



模板如下所示。 

![todo:image_alt_text](working-with-charts_8.png)




1. 保存报告并将其发布到报告服务器。
1. 从报告服务器导出报告。
   结果如下。 

![todo:image_alt_text](working-with-charts_9.png)
