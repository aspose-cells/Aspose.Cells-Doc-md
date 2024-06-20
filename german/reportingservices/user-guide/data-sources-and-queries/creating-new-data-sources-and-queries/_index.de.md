---
title: Erstellen von neuen Datenquellen und Abfragen
type: docs
weight: 20
url: /de/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer integriert sich mit MS Query und verwendet MS Query als Werkzeug zur Erstellung von Datenquellen und Abfragen. Befolgen Sie die folgenden Schritte, um eine neue Datenquelle und Abfrage in Aspose.Cells.Report.Designer zu erstellen:. 

{{% /alert %}} 

Um eine neue Datenquelle und Abfrage in Aspose.Cells.Report.Designer zu erstellen:

1. Öffnen Sie Microsoft Excel.
1. Klicken Sie auf **Build DataSet** in der Aspose.Cells.Report.Designer-Symbolleiste: 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


Alle Datenquellen und Abfragen werden in der Dialogbox aufgelistet. 

1. Ein Datenquellknoten: 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. Ein Datensatzknoten: 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. Wählen Sie den Wurzelknoten des Baums.
1. Klicken Sie auf **Hinzufügen**. 

   **Hinzufügen von Datenquellen und Datensätzen** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. Benennen Sie in der Dialogbox die Datenquelle **SqlServer** und den Datensatz **EmpsSalesDetail**.
1. Klicken Sie auf **Weiter**. 

   **Hinzufügen von Datensätzen und Datenquellen** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer startet Microsoft Query. 

1. Wählen Sie im Dialogfeld Datenquelle auswählen **Neue Datenquelle** aus.
1. Klicken Sie auf **OK**.
   Sie können auch eine vorhandene Datenquelle auswählen. 

   **Auswahl einer Datenquelle** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. Geben Sie einen Datenquellennamen ein und wählen Sie SQL Server aus der Dropdown-Liste der Datenbanktreiber aus.
1. Klicken Sie auf **Verbinden**. 

   **Eine neue Datenquelle erstellen** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. Wählen Sie im SQL Server-Anmeldedialog den geeigneten Wert für jedes Element aus.
   Setzen Sie beispielsweise den Server auf lokal, wählen Sie die AdventureWorks-Datenbank aus und wählen Sie **Vertrauenswürdige Verbindung verwenden** aus.
1. Klicken Sie auf **OK**. 

   **Anmelden beim SQL-Server** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. Klicken Sie auf **OK**. 

   **Beachten Sie, dass wir nun beim SQL-Server angemeldet sind** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



Die neue Datenquelle wird im Dialogfeld **Datenquelle auswählen** angezeigt. 

1. Wählen Sie die neue Datenquelle aus. 

   **Die neue Datenquelle** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. Klicken Sie auf **OK**, um Microsoft Query zu öffnen.
1. Um eine Abfrage in Microsoft Query zu erstellen, beachten Sie den Microsoft Query Helper. Im folgenden Beispiel erstellen wir eine Abfrage mit Parametern. 

   **Erstellen einer Abfrage** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



Der SQL lautet wie folgt: 

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


Die Abfrage hat drei Parameter: ReportYear, ReportMonth und EmpID.

1. Wählen Sie im **Datei**-Menü von Microsoft Query **Zurück zum Aspose.Cells.Report.Designer** aus. 

   **Rückkehr zum Berichtsdesigner** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



Die oben erstellte Datenquelle und Abfrage werden im Dialogfeld aufgelistet. 

1. Klicken Sie auf die Datenquelle **SqlServer**, um ihre ausführlichen Informationen anzuzeigen. 

   **Die neue Datenquelle** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. Klicken Sie auf die Abfrage EmpSalesDetails, um ihre ausführlichen Informationen anzuzeigen. 

   **Klicken Sie auf die SQL-Registerkarte, um das SQL für die Abfrage anzuzeigen** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**Klicken Sie auf die Spalten-Registerkarte, um die Spalten der Abfrage anzuzeigen** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**Klicken Sie auf die Parameter-Registerkarte, um die Parameter der Abfrage anzuzeigen** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



