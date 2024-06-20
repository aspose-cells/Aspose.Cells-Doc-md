---
title: Préparation pour la création d un rapport tabulaire
type: docs
weight: 10
url: /fr/reportingservices/preparing-for-creating-table-report/
---

Avant de créer un rapport tabulaire, l'utilisateur doit d'abord créer des sources de données, des jeux de données et des paramètres de rapport (en option) comme décrit dans [Sources de données et requêtes](/cells/fr/reportingservices/data-sources-and-queries/).

Ci-dessous, nous utilisons la base de données d'exemple AdventureWorks fournie avec SQL Server Reporting Services 2005.

1. Créez un jeu de données nommé EmpSalesDetail. Nous l'utiliserons comme source de données du tableau. Le jeu de données comporte trois paramètres : ReportYear, ReportMonth et EmpID.
   Le SQL qui définit EmpSalesDetail est le suivant : 

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

1. Créez un jeu de données nommé SalesEmps. Nous l'utiliserons comme valeurs valides pour le paramètre EmpID.
   Le SQL qui définit SalesEmps est : 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. Créez trois paramètres de rapport : ReportYear, ReportMonth et EmpID. 
   1. Les valeurs valides pour le paramètre ReportYear sont : 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. La valeur valable pour le paramètre ReportMonth est : 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. La valeur valable pour le paramètre EmpID est : 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. Associez les paramètres du jeu de données aux paramètres du rapport, comme suit : 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
