---
title: 创建新的数据源和查询
type: docs
weight: 20
url: /zh/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer 与 MS Query 集成并使用 MS Query 作为创建数据源和查询的工具。要在 Aspose.Cells.Report.Designer 中创建新的数据源和查询，请按照以下步骤操作：

{{% /alert %}} 

在 Aspose.Cells.Report.Designer 中创建新的数据源和查询：

1. 打开 Microsoft Excel。
1. 点击**构建数据集**在 Aspose.Cells.Report.Designer 工具栏中：

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_1.png)


所有数据源和查询都列在对话框中。

1. 一个数据源节点：

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_2.png)

1. 一个数据集节点：

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_3.png)

1. 选择树的根节点。
1. 点击**添加**. 

   **添加数据源和数据集** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_4.png)




1. 在对话框中，调用数据源**SQL服务器**和数据集**Emps销售明细**.
1. 点击**下一个**. 

   **添加数据集和数据源** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer 启动 Microsoft 查询。

1. 在“选择数据源”对话框中，选择**新数据源**.
1. 点击**好的**.
您还可以选择现有数据源。

   **选择数据源** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_6.png)




1. 输入数据源名称并从数据库驱动程序下拉列表中选择 SQL Server。
1. 点击**连接**. 

   **创建一个新的数据源** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_7.png)




1. 在 SQL Server 登录对话框中，为每个项目选择适当的值。
例如，将服务器设置为本地，选择 AdventureWorks 数据库并选择**使用可信连接**.
1. 点击**好的**. 

   **登录到 SQL 服务器** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_8.png)




1. 点击**好的**. 

   **请注意，我们现在已登录到 SQL 服务器** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_9.png)



新数据源出现在**选择数据源**对话。

1. 选择新的数据源。

   **新的数据源** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_10.png)




1. 点击**好的**打开Microsoft查询。
1. 在Microsoft Query中创建查询，参考Microsoft Query Helper。在以下示例中，我们创建了一个带有参数的查询。

   **构建查询** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_11.png)



SQL如下：

**数据库**

{{< highlight "csharp" >}}

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


该查询具有三个参数：ReportYear、ReportMonth 和 EmpID。

1. 来自 Microsoft 查询的**文件**菜单，选择**返回Aspose.Cells.Report.Designer**. 

   **返回报表设计器** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_12.png)



上面创建的数据源和查询列在对话框中。

1. 单击数据源**SQL服务器**查看其详细信息。

   **新的数据源** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_13.png)




1. 单击查询 EmpSalesDetails 以查看其详细信息。

   **单击 SQL Tab 查看查询的 sql** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_14.png)



**单击列选项卡以查看查询的列** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_15.png)



**点击Parameters Tab查看查询的参数** 

![待办事项：图片_替代_文本](creating-new-data-sources-and-queries_16.png)



