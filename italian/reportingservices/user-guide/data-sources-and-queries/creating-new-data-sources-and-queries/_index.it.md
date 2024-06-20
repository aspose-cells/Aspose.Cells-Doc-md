---
title: Creazione di nuove origini dati e query
type: docs
weight: 20
url: /it/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer si integra con MS Query e utilizza MS Query come strumento per creare origini dati e query. Per creare una nuova origine dati e query in Aspose.Cells.Report.Designer, seguire i passaggi seguenti: 

{{% /alert %}} 

Per creare una nuova origine dati e query in Aspose.Cells.Report.Designer:

1. Aprire Microsoft Excel.
1. Fare clic su **Genera DataSet** nella barra degli strumenti di Aspose.Cells.Report.Designer: 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


Tutte le origini dati e le query sono elencate nella finestra di dialogo. 

1. Un nodo di origine dati: 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. Un nodo di set di dati: 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. Selezionare il nodo radice dell'albero.
1. Fare clic su **Aggiungi**. 

   **Aggiunta di origini dati e set di dati** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. Nella finestra di dialogo, chiamare l'origine dati **SqlServer** e il set di dati **DettaglioVenditeDipendenti**.
1. Fare clic su **Avanti**. 

   **Aggiunta di set di dati e origini dati** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer avvia Microsoft Query. 

1. Nella finestra di dialogo Scegli origine dati, seleziona **Nuova origine dati**.
1. Fai clic su **OK**.
   È anche possibile selezionare una origine dati esistente. 

   **Selezione di una origine dati** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. Immetti un nome per l'origine dati e seleziona SQL Server dall'elenco a discesa dei driver del database.
1. Fai clic su **Connetti**. 

   **Creazione di una nuova origine dati** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. Nella finestra di dialogo Accesso a SQL Server, seleziona il valore appropriato per ciascun elemento.
   Ad esempio, imposta il server su locale, seleziona il database AdventureWorks e seleziona **Usa connessione attendibile**.
1. Fai clic su **OK**. 

   **Accesso al server SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. Fai clic su **OK**. 

   **Nota che ora siamo connessi al server SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



La nuova origine dati appare nella finestra di dialogo **Scegli origine dati**. 

1. Seleziona la nuova origine dati. 

   **La nuova origine dati** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. Fai clic su **OK** per aprire Microsoft Query.
1. Per creare una query in Microsoft Query, fare riferimento all'Assistente di Microsoft Query. Nel seguente esempio, creiamo una query con parametri. 

   **Costruzione di una query** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



Il codice SQL è il seguente: 

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


La query ha tre parametri: AnnoReport, MeseReport e IDImpiegato.

1. Dal menu **File** di Microsoft Query, selezionare **Ritorna a Aspose.Cells.Report.Designer**. 

   **Tornare al designer del rapporto** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



La sorgente dati e la query create sopra sono elencate nella finestra di dialogo. 

1. Fare clic sulla sorgente dati **SqlServer** per visualizzare le informazioni dettagliate. 

   **La nuova origine dati** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. Fare clic sulla query EmpSalesDetails per visualizzare le informazioni dettagliate. 

   **Fare clic sulla scheda SQL per visualizzare l'SQL per la query** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**Fare clic sulla scheda Column per visualizzare le colonne della query** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**Fare clic sulla scheda Parameters per visualizzare i parametri della query** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



