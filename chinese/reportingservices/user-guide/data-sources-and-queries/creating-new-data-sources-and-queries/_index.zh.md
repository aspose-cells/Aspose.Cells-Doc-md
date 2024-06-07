---
title: 创建新的数据源和查询
type: docs
weight: 20
url: /zh/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer 与 MS Query 集成，并使用 MS Query 作为创建数据源和查询的工具。要在 Aspose.Cells.Report.Designer 中创建新的数据源和查询，请按照以下步骤操作： 

{{% /alert %}} 

在 Aspose.Cells.Report.Designer 中创建新的数据源和查询：

1. 打开Microsoft Excel。
1. 在 Aspose.Cells.Report.Designer 工具栏上单击 **构建数据集**。 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


所有数据源和查询都列在对话框中。 

1. 数据源节点： 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. 数据集节点： 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. 选择树的根节点。
1. 点击**添加**。 

   **添加数据源和数据集** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. 在对话框中，将数据源命名为**SqlServer**，数据集命名为**EmpsSalesDetail**。
1. 单击 **下一步**。 

   **添加数据集和数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer 启动 Microsoft Query。 

1. 在“选择数据源”对话框中，选择**新数据源**。
1. 单击**确定**。
   您也可以选择现有数据源。 

   **选择数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. 输入数据源名称，从数据库驱动程序下拉列表中选择 SQL Server。
1. 点击**连接**。 

   **创建新数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. 在 SQL Server 登录对话框中，为每个项目选择适当的值。
   例如，将服务器设置为本地，选择 AdventureWorks 数据库，并选择**使用受信任连接**。
1. 单击**确定**。 

   **登录到 SQL Server** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. 单击**确定**。 

   **请注意我们现在已登录到 SQL Server** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



新数据源显示在“选择数据源”对话框中。 

1. 选择新数据源。 

   **新数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. 点击**确定**以打开 Microsoft Query。
1. 要在 Microsoft Query 中创建查询，请参考 Microsoft Query 助手。在下面的示例中，我们使用参数创建查询。 

   **构建查询** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



SQL 如下： 

**SQL**

{{< highlight csharp >}}

 SELECT C.FirstName + ' ' + C.LastName AS Employee,

DATEPART(Month, SOH.OrderDate) AS OrderMonthNum,

PS.Name AS SubCat,

SUM(SOD.LineTotal) AS Sales,

SOH.SalesOrderNumber,

P.Name AS Product,

SUM(SOD.OrderQty) AS OrderQty,

SOD.UnitPrice,

PC.Name AS ProdCat

FROM  Sales.SalesOrderHeader SOH ,

Sales.SalesOrderDetail SOD ,

Sales.SalesPerson SP,

HumanResources.Employee E,

Person.Contact C,

Production.Product P,

Production.ProductSubcategory PS ,

Production.ProductCategory PC

where SOH.SalesOrderID = SOD.SalesOrderID

and SOH.SalesPersonID = SP.SalesPersonID

and SP.SalesPersonID = E.EmployeeID

and E.ContactID = C.ContactID

and SOD.ProductID = P.ProductID

and P.ProductSubcategoryID = PS.ProductSubcategoryID

and PS.ProductCategoryID = PC.ProductCategoryID

and  (DATEPART(Year, SOH.OrderDate) =  ?)

AND (DATEPART(Month, SOH.OrderDate) =  ?)

AND (SOH.SalesPersonID =?)

GROUP BY    C.FirstName + ' ' + C.LastName,

DATEPART(Month, SOH.OrderDate), SOH.SalesOrderNumber,

P.Name, PS.Name, SOD.UnitPrice, PC.Name



{{< /highlight >}}


查询有三个参数：ReportYear、ReportMonth 和 EmpID。

1. 从 Microsoft Query 的 **文件** 菜单中，选择 **返回到 Aspose.Cells.Report.Designer**。 

   **返回到报表设计器** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



上述创建的数据源和查询在对话框中列出。 

1. 点击数据源 **SqlServer** 查看其详细信息。 

   **新数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. 点击查询 EmpSalesDetails 查看其详细信息。 

   **单击 SQL 选项卡查看查询的 SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**单击列选项卡查看查询的列** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**单击参数选项卡查看查询的参数** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



