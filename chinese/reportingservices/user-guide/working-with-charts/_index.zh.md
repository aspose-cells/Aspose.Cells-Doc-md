---
title: 使用图表
type: docs
weight: 110
url: /zh/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

Aspose.Cells 报表模板支持Microsoft Excel图表。每次执行报告时，图表都会填充最新数据。

{{% /alert %}} 

将图表添加到报告模板：

1. 首先，创建将作为图表数据源的数据集。
下面，我们使用 SQL Server Reporting Services 2005 附带的 AdventureWorks 示例数据库并创建一个名为 Sales 的数据集。
此 SQL 定义数据集：

**数据库**

{{< highlight "csharp" >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



请参阅[数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/)在 Aspose.Cells.Report.Designer 中了解有关如何创建数据源和数据集的更多信息。

1. 根据中的说明创建表格报告[创建表格报告](/cells/zh/reportingservices/creating-tabular-report/).我们为此示例创建的报告如下。表格是图表的数据源。

![待办事项：图像_替代_文本](working-with-charts_1.png)




1. 在 Microsoft Excel 中，单击**插入**菜单并选择**图表**.
1. 点击**下一个**. 

![待办事项：图像_替代_文本](working-with-charts_2.png)




1. 点击**系列**标签。

![待办事项：图像_替代_文本](working-with-charts_3.png)




1. 点击**添加**. 

![待办事项：图像_替代_文本](working-with-charts_4.png)




1. 在对话框中，将 Series1（季度系列）的值设置为表的第一个数据字段。
在示例中，它是“CompanySales!$C$3:$C$3”。第一个 $C$3 是“Quarter”的第一行索引，第二个 $C$3 是“Quarter”最后一行索引的占位符，将在呈现时替换为表数据的实际行索引。将类别 (X) 轴标签设置为“=CompanySales!$C$3:$C$3”。

![待办事项：图像_替代_文本](working-with-charts_5.png)




1. 点击**添加**添加另一个系列。
在示例中，我们添加了销售系列。
1. 将 Series2（销售系列）的值设置为表的第二个数据字段。
在示例中它是“CompanySales!$D$3:$D$3”。第一个 $D$3 是“Sales”的第一行索引，第二个 $D$3 是“Sales”最后一行索引的占位符，将在呈现时替换为表数据的实际行索引。
1. 点击**下一个**接着说。

![待办事项：图像_替代_文本](working-with-charts_6.png)




1. 在对话框中，设置图表标题和类别（X）轴。
1. 点击**结束**完成工作。

![待办事项：图像_替代_文本](working-with-charts_7.png)



该模板如下所示。

![待办事项：图像_替代_文本](working-with-charts_8.png)




1. 保存报表并将其发布到报表服务器。
1. 从报表服务器导出报表。
结果如下。

![待办事项：图像_替代_文本](working-with-charts_9.png)
