---
title: Preparación para Crear Reporte de Tabla
type: docs
weight: 10
url: /es/reportingservices/preparing-for-creating-table-report/
---

Antes de crear un reporte tabular, el usuario primero debe crear fuentes de datos, conjuntos de datos y parámetros de reporte (opcional) como se describe en [Fuentes de Datos y Consultas](/cells/es/reportingservices/data-sources-and-queries/).

A continuación, usamos la base de datos de ejemplo AdventureWorks que se incluye con SQL Server Reporting Services 2005.

1. Cree un conjunto de datos llamado EmpSalesDetail. Usaremos esto como origen de datos de la tabla. El conjunto de datos tiene tres parámetros: ReportYear, ReportMonth y EmpID.
   El SQL que define EmpSalesDetail es el siguiente: 

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

1. Cree un conjunto de datos llamado SalesEmps. Usaremos eso como los valores válidos para el parámetro EmpID.
   El SQL que define SalesEmps es: 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. Cree tres parámetros de informe: ReportYear, ReportMonth y EmpID. 
   1. Los valores válidos para el parámetro ReportYear son: 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. Los valores válidos para el parámetro ReportMonth son: 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. El valor válido para el parámetro EmpID es: 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. Asigne los parámetros del conjunto de datos a los parámetros del informe, de la siguiente manera: 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
