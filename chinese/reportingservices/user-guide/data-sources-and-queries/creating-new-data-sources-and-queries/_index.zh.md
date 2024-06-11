---
title: 创建新的数据源和查询
type: docs
weight: 20
url: /zh/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer与MS Query集成，并使用MS Query作为创建数据源和查询的工具。要在Aspose.Cells.Report.Designer中创建新的数据源和查询，请按照以下步骤进行： 

{{% /alert %}} 

要在Aspose.Cells.Report.Designer中创建新的数据源和查询：

1. 打开 Microsoft Excel。
1. 在Aspose.Cells.Report.Designer工具栏中点击**构建数据集**： 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


所有数据源和查询都列在对话框中。 

1. 数据源节点： 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. 数据集节点： 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. 选择树的根节点。
1. 单击 **添加**。 

   **添加数据源和数据集** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. 在对话框中，将数据源命名为**SqlServer**，将数据集命名为**EmpsSalesDetail**。
1. 点击**下一步**。 

   **添加数据集和数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer启动Microsoft Query。 

1. 在选择数据源对话框中，选择**新数据源**。
1. 点击**确定**。
   您也可以选择现有的数据源。 

   **选择数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. 输入数据源名称并从数据库驱动程序的下拉列表中选择 SQL Server。
1. 单击**连接**。 

   **创建新数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. 在 SQL Server 登录对话框中，为每个项目选择适当的值。
   例如，将服务器设置为本地，选择 AdventureWorks 数据库，并选择**使用可信连接**。
1. 点击**确定**。 

   **登录到 SQL 服务器** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. 点击**确定**。 

   **请注意，我们现在已登录到 SQL 服务器** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



新数据源显示在**选择数据源**对话框中。 

1. 选择新数据源。 

   **新数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. 单击**确定**以打开 Microsoft Query。
1. 若要在 Microsoft Query 中创建查询，请参考 Microsoft Query Helper。在以下示例中，我们使用参数创建查询。 

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


该查询有三个参数：ReportYear、ReportMonth 和 EmpID。

1. 从Microsoft Query的**文件**菜单中，选择**返回到Aspose.Cells.Report.Designer**。 

   **返回到报表设计师** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



上述创建的数据源和查询在对话框中列出。 

1. 单击数据源**SqlServer**以查看其详细信息。 

   **新数据源** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. 点击查询EmpSalesDetails以查看其详细信息。 

   **点击SQL选项卡以查看查询的SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**点击列选项卡以查看查询的列** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**点击参数选项卡以查看查询的参数** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



