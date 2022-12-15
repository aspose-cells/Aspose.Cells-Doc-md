---
title: 使用数据透视表
type: docs
weight: 100
url: /zh/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

一个*数据透视表*是一个交互式表格，用于汇总数据并以有意义的方式呈现数据。 SQL Server Reporting Services 在维护数据透视表时无法将报表导出为 Microsft Excel 格式。报表用户每次将数据透视表报表从 Reporting Services 导出到 Microsoft Excel 时都必须手动创建数据透视表。使用 Aspose.Cells for Reporting Services，您可以在报表设计时设计一次数据透视表。每次报表运行时，Aspose.Cells for Reporting Services 将报表导出到Microsoft Excel，并将数据刷新到数据透视表中。

{{% /alert %}} 

要创建数据透视表报告：

1. 创建数据集作为数据透视表的数据源。
下面，我们使用 SQL Server Reporting Services 2005 附带的 AdventureWorks 示例数据库并创建一个名为“sales”的数据集。
数据集的SQL如下：

**数据库**

{{< highlight "csharp" >}}

 SELECT  PC.Name AS ProdCat,

	    PS.Name AS SubCat,

	    DATEPART(yy, SOH.OrderDate) AS OrderYear,

	    'Q' + DATENAME(qq, SOH.OrderDate) AS OrderQtr,

         SUM(SOD.UnitPrice * SOD.OrderQty) AS Sales

FROM    Production.ProductSubcategory PS INNER JOIN

         Sales.SalesOrderHeader SOH INNER JOIN

         Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID INNER JOIN

         Production.Product P ON SOD.ProductID = P.ProductID ON PS.ProductSubcategoryID = P.ProductSubcategoryID INNER JOIN

         Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID

WHERE   (SOH.OrderDate BETWEEN '1/1/2002' AND '12/31/2003')

GROUP BY  DATEPART(yy, SOH.OrderDate), PC.Name, PS.Name, 'Q' + DATENAME(qq, SOH.OrderDate), PS.ProductSubcategoryID



{{< /highlight >}}



{{% alert color="primary" %}} 

请参阅[数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/)了解有关如何使用 Aspose.Cells.Report.Designer 创建数据源和数据集的更多信息。

{{% /alert %}} 

1. 根据中的说明创建表格报告[创建表格报告](/cells/zh/reportingservices/creating-tabular-report/)， 如下所示。
该表将成为数据透视表的数据源。

![待办事项：图像_替代_文本](working-with-pivottable_1.png)




1. 在 Microsoft Excel 中，从**插入**菜单，选择**姓名**接着**定义**.
1. 将名称定义为“sales”。
名称范围从标题标题的第一个单元格开始，到表数据行的最后一个单元格结束，如下所示。

![待办事项：图像_替代_文本](working-with-pivottable_2.png)




1. 点击**好的**完成。
1. 为数据透视表创建一个新工作表。
1. 来自**数据**菜单，选择**数据透视表和数据透视图报表**添加数据透视表。
显示一个对话框。
1. 选择**Microsoft Office Excel 列表或数据库**作为数据源和**数据透视表**作为报告类型。
1. 点击**下一个**接着说。

![待办事项：图像_替代_文本](working-with-pivottable_3.png)




1. 在对话框中，输入您在上面定义的名称“sales”。
1. 点击**下一个**接着说。

![待办事项：图像_替代_文本](working-with-pivottable_4.png)




1. 点击**结束**. 

![待办事项：图像_替代_文本](working-with-pivottable_5.png)




1. 在 Excel 中设计数据透视表。

![待办事项：图像_替代_文本](working-with-pivottable_6.png)



设计的数据透视表如下所示。

![待办事项：图像_替代_文本](working-with-pivottable_7.png)




1. 右键单击数据透视表并选择**表格选项**.
1. 确保**打开时刷新**被选中。

![待办事项：图像_替代_文本](working-with-pivottable_8.png)




1. 保存报表并将其发布到报表服务器。
1. 从报表服务器导出报表。
结果如下所示。

![待办事项：图像_替代_文本](working-with-pivottable_9.png)
