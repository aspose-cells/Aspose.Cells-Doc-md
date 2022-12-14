---
title: Erstellen neuer Datenquellen und Abfragen
type: docs
weight: 20
url: /de/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

 Aspose.Cells.Report.Designer lässt sich in MS Query integrieren und verwendet MS Query als Tool zum Erstellen von Datenquellen und Abfragen. Führen Sie die folgenden Schritte aus, um eine neue Datenquelle und Abfrage in Aspose.Cells.Report.Designer zu erstellen:.

{{% /alert %}} 

So erstellen Sie eine neue Datenquelle und Abfrage in Aspose.Cells.Report.Designer:

1. Öffnen Sie Microsoft Excel.
1.  Klicken**Datensatz erstellen** in der Symbolleiste Aspose.Cells.Report.Designer:

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_1.png)


Alle Datenquellen und Abfragen werden im Dialogfeld aufgelistet.

1.  Ein Datenquellenknoten:

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_2.png)

1.  Ein Datensatzknoten:

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_3.png)

1. Wählen Sie den Wurzelknoten des Baums aus.
1.  Klicken**Hinzufügen**. 

   **Hinzufügen von Datenquellen und Datensätzen** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_4.png)




1.  Rufen Sie im Dialogfenster die Datenquelle auf**SQL Server** und der Datensatz**EmpsSalesDetail**.
1.  Klicken**Nächste**. 

   **Hinzufügen von Datensätzen und Datenquellen** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_5.png)



 Aspose.Cells.Report.Designer startet die Microsoft-Abfrage.

1.  Wählen Sie im Dialogfeld „Datenquelle auswählen“ aus**Neue Datenquelle**.
1.  Klicken**OK**.
 Sie können auch eine vorhandene Datenquelle auswählen.

   **Auswählen einer Datenquelle** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_6.png)




1. Geben Sie einen Datenquellennamen ein und wählen Sie SQL Server aus der Dropdown-Liste der Datenbanktreiber aus.
1.  Klicken**Verbinden**. 

   **Erstellen einer neuen Datenquelle** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_7.png)




1. Wählen Sie im Dialogfeld SQL Server-Anmeldung den entsprechenden Wert für jedes Element aus.
 Stellen Sie beispielsweise server auf local ein, wählen Sie die AdventureWorks-Datenbank aus, und wählen Sie aus**Vertrauenswürdige Verbindung verwenden**.
1.  Klicken**OK**. 

   **Anmeldung am SQL-Server** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_8.png)




1.  Klicken**OK**. 

   **Beachten Sie, dass wir jetzt beim SQL-Server angemeldet sind** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_9.png)



Die neue Datenquelle wird in der angezeigt**Wählen Sie Datenquelle** Dialog.

1.  Wählen Sie die neue Datenquelle aus.

   **Die neue Datenquelle** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_10.png)




1.  Klicken**OK** Microsoft Abfrage öffnen.
1.  Informationen zum Erstellen einer Abfrage in Microsoft-Abfrage finden Sie im Microsoft-Abfrage-Helper. Im folgenden Beispiel erstellen wir eine Abfrage mit Parametern.

   **Erstellen einer Abfrage** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_11.png)



 Das SQL ist wie folgt:

**SQL**

{{< highlight "csharp" >}}

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


Die Abfrage hat drei Parameter: ReportYear, ReportMonth und EmpID.

1.  Von Microsoft Abfrage's**Datei** Menü, auswählen**Zurück zu Aspose.Cells.Report.Designer**. 

   **Zurück zum Berichtsdesigner** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_12.png)



 Die oben erstellte Datenquelle und Abfrage werden im Dialogfeld aufgelistet.

1.  Klicken Sie auf die Datenquelle**SQL Server** um seine detaillierten Informationen anzuzeigen.

   **Die neue Datenquelle** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_13.png)




1.  Klicken Sie auf die Abfrage EmpSalesDetails, um die detaillierten Informationen anzuzeigen.

   **Klicken Sie auf die Registerkarte „SQL“, um die SQL für die Abfrage anzuzeigen** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_14.png)



**Klicken Sie auf die Registerkarte Spalten, um die Spalten der Abfrage anzuzeigen** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_15.png)



**Klicken Sie auf die Registerkarte Parameter, um die Parameter der Abfrage anzuzeigen** 

![todo: Bild_alt_Text](creating-new-data-sources-and-queries_16.png)



