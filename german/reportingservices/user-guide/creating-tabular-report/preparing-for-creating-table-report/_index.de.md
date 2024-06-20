---
title: Vorbereitung für die Erstellung eines tabellarischen Berichts
type: docs
weight: 10
url: /de/reportingservices/preparing-for-creating-table-report/
---

Bevor ein tabellarischer Bericht erstellt wird, muss der Benutzer zuerst Datenquellen, Datensätze und Berichtsparameter (optional) erstellen, wie in [Datenquellen und Abfragen](/cells/de/reportingservices/data-sources-and-queries/) beschrieben.

Im Folgenden verwenden wir die AdventureWorks-Beispieldatenbank, die mit SQL Server Reporting Services 2005 ausgeliefert wird.

1. Erstellen Sie einen Datensatz mit dem Namen EmpSalesDetail. Wir werden dies als Datenquelle der Tabelle verwenden. Der Datensatz hat drei Parameter: ReportYear, ReportMonth und EmpID.
   Der SQL, der EmpSalesDetail definiert, lautet: 

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

1. Erstellen Sie einen Datensatz mit dem Namen SalesEmps. Wir verwenden dies als gültige Werte für den Parameter EmpID.
   Der SQL, der SalesEmps definiert, lautet: 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. Erstellen Sie drei Berichtsparameter: ReportYear, ReportMonth und EmpID. 
   1. Die gültigen Werte für den Parameter ReportYear sind: 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. Die gültigen Werte für den Parameter ReportMonth sind: 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. Der gültige Wert für den Parameter EmpID ist: 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. Ordnen Sie die Datensatzparameter den Berichtsparametern wie folgt zu: 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
