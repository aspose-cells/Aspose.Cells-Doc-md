---
title: Preparazione per la creazione di report tabella
type: docs
weight: 10
url: /it/reportingservices/preparing-for-creating-table-report/
---
 Prima di creare un report tabulare, l'utente deve prima creare origini dati, set di dati e parametri del report (facoltativo) come descritto in[DataSource e query](/cells/it/reportingservices/data-sources-and-queries/).

Di seguito viene utilizzato il database di esempio AdventureWorks fornito con SQL Server Reporting Services 2005.

1. Crea un set di dati denominato EmpSalesDetail. Lo useremo come origine dati della tabella. Il set di dati ha tre parametri: ReportYear, ReportMonth e EmpID.
 L'SQL che definisce EmpSalesDetail è il seguente:

**SQL**

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

1. Crea un set di dati denominato SalesEmps. Lo useremo come valori validi per il parametro EmpID.
 L'SQL che definisce SalesEmps è:

**SQL**

{{< highlight "csharp" >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1.  Creare tre parametri di report: ReportYear, ReportMonth e EmpID.
 1. I valori validi per il parametro ReportYear sono:

![cose da fare:immagine_alt_testo](preparing-for-creating-table-report_1.png)




1.  valori validi per il parametro ReportMonth sono:

![cose da fare:immagine_alt_testo](preparing-for-creating-table-report_2.png)




1.  I valori validi per il parametro EmpID sono:

![cose da fare:immagine_alt_testo](preparing-for-creating-table-report_3.png)




1.  Mappare i parametri del set di dati per segnalare i parametri, come segue:

![cose da fare:immagine_alt_testo](preparing-for-creating-table-report_4.png)
