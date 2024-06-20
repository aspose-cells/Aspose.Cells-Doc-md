---
title: Skapar nya datakällor och frågor
type: docs
weight: 20
url: /sv/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer integreras med MS Query och använder MS Query som ett verktyg för att skapa datakällor och frågor. För att skapa en ny datakälla och fråga i Aspose.Cells.Report.Designer, följ stegen nedan:. 

{{% /alert %}} 

För att skapa en ny datakälla och fråga i Aspose.Cells.Report.Designer:

1. Öppna Microsoft Excel.
1. Klicka på **Bygg dataset** i verktygsfältet Aspose.Cells.Report.Designer: 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


Alla datakällor och frågor listas i dialogrutan. 

1. En datakällnod: 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. En datamängdnod: 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. Välj trädrotsnoden.
1. Klicka på **Lägg till**. 

   **Lägga till datakällor och datamängder** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. I dialogrutan, kalla datakällan **SqlServer** och datamängden **EmpsSalesDetail**.
1. Klicka på **Nästa**. 

   **Lägga till datamängder och datakällor** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer startar Microsoft Query. 

1. I dialogrutan Välj datakälla, välj **Ny datakälla**.
1. Klicka på **OK**.
   Du kan också välja en befintlig datakälla. 

   **Välja en datakälla** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. Ange ett namn för datakällan och välj SQL Server från rullgardinsmenyn för databasdrivrutiner.
1. Klicka på **Anslut**. 

   **Skapa en ny datakälla** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. I SQL Server Login-dialogrutan, välj rätt värde för varje objekt.
   Till exempel, ange server till lokal, välj AdventureWorks-databasen och välj **Använd pålitlig anslutning**.
1. Klicka på **OK**. 

   **Logga in på SQL-servern** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. Klicka på **OK**. 

   **Observera att vi nu är inloggad på SQL-servern** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



Den nya datakällan visas i dialogrutan **Välj datakälla**. 

1. Välj den nya datakällan. 

   **Den nya datakällan** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. Klicka på **OK** för att öppna Microsoft Query.
1. För att skapa en fråga i Microsoft Query, hänvisa till Microsoft Query Helper. I följande exempel skapar vi en fråga med parametrar. 

   **Bygga en fråga** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



SQL:en är följande: 

**SQL**

{{< highlight csharp >}}

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


Frågan har tre parametrar: Rapportår, Rapportmånad och EmpID.

1. Från Microsoft Query's **Arkiv**-meny väljer du **Återgå till Aspose.Cells.Report.Designer**. 

   **Återgå till rapportdesignern** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



Datakällan och frågan som skapats ovan listas i dialogrutan. 

1. Klicka på datakällan **SqlServer** för att visa dess detaljer. 

   **Den nya datakällan** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. Klicka på frågan EmpSalesDetails för att se dess detaljerad information. 

   **Klicka på SQL-fliken för att se sql för frågan** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**Klicka på kolumnfliken för att se kolumnerna i frågan** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**Klicka på parametrar-fliken för att se parametrarna i frågan** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



