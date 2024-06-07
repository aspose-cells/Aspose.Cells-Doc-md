---
title: 使用数据透视表
type: docs
weight: 100
url: /zh/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

*数据透视表*是一个交互式表格，它可以对数据进行汇总并以有意义的方式呈现。SQL Server Reporting Services无法将报表导出为Microsoft Excel格式的同时保留数据透视表。报表用户每次将从Reporting Services导出数据透视表报表到Microsoft Excel时都必须手动创建数据透视表。使用Aspose.Cells for Reporting Services，您可以在报表设计时设计一个数据透视表。每次运行报表时，Aspose.Cells for Reporting Services都会将报表导出到Microsoft Excel，并刷新数据到数据透视表中。

{{% /alert %}} 

创建数据透视表报表：

1.创建一个数据集作为数据透视表的数据源。
   下面，我们使用随SQL Server Reporting Services 2005一起提供的AdventureWorks示例数据库，并创建一个名为“销售”的数据集。
   数据集的SQL如下： 

**SQL**

{{< highlight csharp >}}

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

请参阅[数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/)以了解如何使用Aspose.Cells.Report.Designer创建数据源和数据集的更多信息。

{{% /alert %}} 

1.根据[创建表格报表](/cells/zh/reportingservices/creating-tabular-report/)中的说明创建一个表格报表，如下所示。
   该表格将作为数据透视表的数据源。 

![todo:image_alt_text](working-with-pivottable_1.png)




1.在Microsoft Excel中，从**插入**菜单中选择**名称**，然后选择**定义**。
1.定义一个名为“销售”的名称。
   名称的范围从标题的第一个单元格开始，直到表格数据行的最后一个单元格，如下所示。 

![todo:image_alt_text](working-with-pivottable_2.png)




1. 点击**确定** 完成。
1.为数据透视表创建一个新工作表。
从**数据**菜单中选择**数据透视表和数据透视图报告**以添加一个数据透视表。
   会显示一个对话框。
1.将**Microsoft Office Excel列表或数据库**作为数据源，并选择**数据透视表**作为报告类型。
1. 单击 **下一步** 继续。 

![todo:image_alt_text](working-with-pivottable_3.png)




在对话框中，输入上面定义的“销售”名称。
1. 单击 **下一步** 继续。 

![todo:image_alt_text](working-with-pivottable_4.png)




1. 单击 **完成**。 

![todo:image_alt_text](working-with-pivottable_5.png)




1.在Excel中设计数据透视表。 

![todo:image_alt_text](working-with-pivottable_6.png)



所设计的数据透视表如下所示。 

![todo:image_alt_text](working-with-pivottable_7.png)




1. 右键单击数据透视表，然后选择**表选项**。
1.确保选择**打开时刷新**。 

![todo:image_alt_text](working-with-pivottable_8.png)




1. 保存报表并将其发布到报表服务器。
1. 从报表服务器导出报表。
   结果如下。 

![todo:image_alt_text](working-with-pivottable_9.png)
