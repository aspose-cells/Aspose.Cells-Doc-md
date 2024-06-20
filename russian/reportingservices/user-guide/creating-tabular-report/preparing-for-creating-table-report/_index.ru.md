---
title: Подготовка к созданию отчета таблицы
type: docs
weight: 10
url: /ru/reportingservices/preparing-for-creating-table-report/
---

Перед созданием табличного отчета пользователь должен сначала создать источники данных, наборы данных и параметры отчета (при необходимости), как описано в [Источники данных и запросы](/cells/ru/reportingservices/data-sources-and-queries/).

Ниже мы используем демонстрационную базу данных AdventureWorks, которая поставляется вместе с SQL Server Reporting Services 2005.

1. Создайте набор данных с именем EmpSalesDetail. Мы будем использовать его в качестве источника данных для таблицы. У этого набора данных три параметра: ReportYear, ReportMonth и EmpID.
   SQL, который определяет EmpSalesDetail, выглядит следующим образом: 

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

1. Создайте набор данных с именем SalesEmps. Мы будем использовать его в качестве допустимых значений для параметра EmpID.
   SQL, который определяет SalesEmps, выглядит следующим образом: 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. Создайте три параметра отчета: ReportYear, ReportMonth и EmpID. 
   1. Допустимые значения для параметра ReportYear: 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. Допустимые значения для параметра ReportMonth: 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. Допустимое значение для параметра EmpID: 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. Сопоставьте параметры набора данных с параметрами отчета следующим образом: 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
