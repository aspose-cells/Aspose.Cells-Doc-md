---
title: 使用数据透视表
type: docs
weight: 100
url: /zh/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

数据透视表是一种交互式表格，可对数据进行总结并以有意义的方式呈现。SQL Server报告服务无法将报表导出为Microsoft Excel格式并保留数据透视表。报告用户必须每次将数据透视表报告从报告服务导出到Microsoft Excel时手动创建数据透视表。使用Aspose.Cells for Reporting Services，您可以在报表设计时仅需设计一次数据透视表。每次运行报表时，Aspose.Cells for Reporting Services将报表导出到Microsoft Excel并刷新数据到数据透视表中。

{{% /alert %}} 

创建数据透视表报告：

1. 创建数据集作为数据透视表的数据源。
   下面，我们使用随SQL Server报告服务 2005一起提供的AdventureWorks示例数据库，并创建名为“销售”的数据集。
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

请参考[数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/)，了解如何使用Aspose.Cells.Report.Designer创建数据源和数据集。

{{% /alert %}} 

1. 根据[创建表格报告](/cells/zh/reportingservices/creating-tabular-report/)中的指示创建一个表格报告，如下所示。
   该表格将成为数据透视表的数据源。 

![todo:image_alt_text](working-with-pivottable_1.png)




1. 在Microsoft Excel中，从**插入**菜单中选择**名称**，然后选择**定义**。
1. 将名称定义为“销售”。
   名称的范围从标题的第一个单元格开始，直到表格数据行的最后一个单元格，如下所示。 

![todo:image_alt_text](working-with-pivottable_2.png)




1. 点击**确定**完成。
1. 为数据透视表创建一个新表。
1. 从**数据**菜单中选择**数据透视表和数据透视图报告**来添加一个数据透视表。
   将显示对话框。
1. 选择**Microsoft Office Excel列表或数据库**作为数据源，并选择**数据透视表**作为报表类型。
1. 点击**下一个**继续。 

![todo:image_alt_text](working-with-pivottable_3.png)




1. 在对话框中输入“sales”，即您上面定义的名称。
1. 点击**下一个**继续。 

![todo:image_alt_text](working-with-pivottable_4.png)




1. 点击**完成**。 

![todo:image_alt_text](working-with-pivottable_5.png)




1. 在Excel中设计数据透视表。 

![todo:image_alt_text](working-with-pivottable_6.png)



设计的数据透视表如下所示。 

![todo:image_alt_text](working-with-pivottable_7.png)




1. 右键单击数据透视表，然后选择**表选项**。
1. 确保已选择**打开时刷新**。 

![todo:image_alt_text](working-with-pivottable_8.png)




1. 保存报告并将其发布到报告服务器。
1. 从报告服务器导出报告。
   结果如下所示。 

![todo:image_alt_text](working-with-pivottable_9.png)
