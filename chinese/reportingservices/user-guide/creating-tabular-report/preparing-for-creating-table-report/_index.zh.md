---
title: 准备创建表格报表
type: docs
weight: 10
url: /zh/reportingservices/preparing-for-creating-table-report/
---

在创建表格报表之前，用户必须先创建数据源、数据集和报表参数（可选），如[数据源和查询](/cells/zh/reportingservices/data-sources-and-queries/)中所述。

下面，我们使用随 SQL Server Reporting Services 2005 一起提供的 AdventureWorks 示例数据库。

1. 创建名为 EmpSalesDetail 的数据集。我们将使用它作为表格的数据源。该数据集有三个参数：ReportYear、ReportMonth 和 EmpID。
   定义 EmpSalesDetail 的 SQL 如下： 

**SQL**

{{< highlight csharp >}}

 SELECT C.FirstName+' '+C.LastName 'Employee',

DATEPART(Month,SOH.OrderDate) 'OrderMonthNum',

PS.Name 'SubCat',

Sum(SOD.LineTotal) 'Sales',

SOH.SalesOrderNumber,

P.Name 'Product',

Sum(SOD.OrderQty) 'OrderQty',

SOD.UnitPrice,

PC.Name 'ProdCat'

FROM AdventureWorks.Person.Contact C,

AdventureWorks.HumanResources.Employee E,

AdventureWorks.Production.Product P,

AdventureWorks.Production.ProductCategory PC,

AdventureWorks.Production.ProductSubcategory PS,

AdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH,

AdventureWorks.Sales.SalesPerson SP

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND SOH.SalesPersonID = SP.SalesPersonID

AND SP.SalesPersonID = E.EmployeeID

AND E.ContactID = C.ContactID

AND SOD.ProductID = P.ProductID

AND P.ProductSubcategoryID = PS.ProductSubcategoryID

 AND PS.ProductCategoryID = PC.ProductCategoryID

AND ((DATEPART(Year,SOH.OrderDate)=?)

AND (DATEPART(Month,SOH.OrderDate)=?) AND (SOH.SalesPersonID=?))

GROUP BY C.FirstName+' '+C.LastName, DATEPART(Month,SOH.OrderDate),

 PS.Name,

SOH.SalesOrderNumber,

P.Name,

SOD.UnitPrice,

PC.Name



{{< /highlight >}}

1. 创建名为 SalesEmps 的数据集。我们将使用它作为 EmpID 参数的有效值。
   定义 SalesEmps 的 SQL 如下： 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. 创建三个报表参数：ReportYear、ReportMonth 和 EmpID。 
   1. 参数 ReportYear 的有效值为： 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. 参数 ReportMonth 的有效值为: 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. 参数 EmpID 的有效值为: 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. 将数据集参数映射到报表参数，如下所示: 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
