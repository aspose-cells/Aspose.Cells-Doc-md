---
title: Förberedelser för att skapa en tabellrapport
type: docs
weight: 10
url: /sv/reportingservices/preparing-for-creating-table-report/
---

Innan man skapar en tabellrapport måste användaren först skapa datakällor, dataset och rapportparametrar (valfritt) enligt beskrivningen i [Datakällor och frågor](/cells/sv/reportingservices/data-sources-and-queries/).

Nedan använder vi exempeldatabasen AdventureWorks som inkluderas med SQL Server Reporting Services 2005.

1. Skapa ett dataset med namnet EmpSalesDetail. Vi kommer att använda detta som tabellens datakälla. Datasetet har tre parametrar: Rapportår, Rapportmånad och EmpID.
   SQL som definierar EmpSalesDetail är följande: 

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

1. Skapa ett dataset med namnet SalesEmps. Vi kommer att använda det som giltiga värden för parametern EmpID.
   SQL som definierar SalesEmps är: 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. Skapa tre rapportparametrar: Rapportår, Rapportmånad och EmpID. 
   1. De giltiga värdena för parametern Rapportår är: 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. De giltiga värdena för parametern Rapportmånad är: 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. Det giltiga värdet för parametern EmpID är: 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. Kartlägg datasetparametrar till rapportparametrar, enligt följande: 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
