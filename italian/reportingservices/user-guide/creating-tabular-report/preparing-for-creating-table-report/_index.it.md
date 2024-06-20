---
title: Preparazione per la creazione di un rapporto tabellare
type: docs
weight: 10
url: /it/reportingservices/preparing-for-creating-table-report/
---

Prima di creare un rapporto tabellare, l'utente deve prima creare origini dati, set di dati e parametri di rapporto (opzionale) come descritto in [DataSources e Queries](/cells/it/reportingservices/data-sources-and-queries/).

Di seguito, utilizziamo il database di esempio AdventureWorks che viene fornito con SQL Server Reporting Services 2005.

1. Creare un set di dati chiamato EmpSalesDetail. Lo useremo come origine dati della tabella. Il set di dati ha tre parametri: ReportYear, ReportMonth ed EmpID.
   Il SQL che definisce EmpSalesDetail è il seguente: 

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

1. Creare un set di dati chiamato SalesEmps. Lo useremo come valori validi per il parametro EmpID.
   L'SQL che definisce SalesEmps è: 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. Creare tre parametri di report: ReportYear, ReportMonth ed EmpID. 
   1. I valori validi per il parametro ReportYear sono: 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. I valori validi per il parametro ReportMonth sono: 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. Il valore valido per il parametro EmpID è: 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. Mappare i parametri del dataset ai parametri di report, come segue: 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
