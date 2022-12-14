---
title: Preparación para crear un informe de tabla
type: docs
weight: 10
url: /es/reportingservices/preparing-for-creating-table-report/
---
 Antes de crear un informe tabular, el usuario primero debe crear fuentes de datos, conjuntos de datos y parámetros de informe (opcional) como se describe en[Fuentes de datos y consultas](/cells/es/reportingservices/data-sources-and-queries/).

A continuación, usamos la base de datos de muestra AdventureWorks que se incluye con SQL Server Reporting Services 2005.

1. Cree un conjunto de datos denominado EmpSalesDetail. Usaremos esto como la fuente de datos de la tabla. El conjunto de datos tiene tres parámetros: ReportYear, ReportMonth y EmpID.
 El SQL que define EmpSalesDetail es el siguiente:

**sql**

{{< highlight "csharp" >}}

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

1. Cree un conjunto de datos denominado SalesEmps. Usaremos eso como los valores válidos para el parámetro EmpID.
 El SQL que define SalesEmps es:

**sql**

{{< highlight "csharp" >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1.  Cree tres parámetros de informe: ReportYear, ReportMonth y EmpID.
 1. Los valores válidos para el parámetro ReportYear son:

![todo:imagen_alternativa_texto](preparing-for-creating-table-report_1.png)




1. Los valores válidos para el parámetro ReportMonth son:

![todo:imagen_alternativa_texto](preparing-for-creating-table-report_2.png)




1.  Los valores válidos para el parámetro EmpID son:

![todo:imagen_alternativa_texto](preparing-for-creating-table-report_3.png)




1.  Asigne los parámetros del conjunto de datos a los parámetros del informe, de la siguiente manera:

![todo:imagen_alternativa_texto](preparing-for-creating-table-report_4.png)
