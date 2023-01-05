---
title: Creazione di nuove origini dati e query
type: docs
weight: 20
url: /it/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

 Aspose.Cells.Report.Designer si integra con MS Query e utilizza MS Query come strumento per la creazione di origini dati e query. Per creare una nuova origine dati e una query in Aspose.Cells.Report.Designer, attenersi alla seguente procedura:.

{{% /alert %}} 

Per creare una nuova origine dati e una query in Aspose.Cells.Report.Designer:

1. Apri Microsoft Excel.
1.  Clic**Crea set di dati** nella barra degli strumenti Aspose.Cells.Report.Designer:

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_1.png)


Tutte le origini dati e le query sono elencate nella finestra di dialogo.

1.  Un nodo di origine dati:

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_2.png)

1.  Un nodo del set di dati:

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_3.png)

1. Seleziona il nodo radice dell'albero.
1.  Clic**Aggiungere**. 

   **Aggiunta di origini dati e set di dati** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_4.png)




1.  Nella finestra di dialogo chiamare l'origine dati**Server SQL** e il set di dati**EmpsSalesDetail**.
1.  Clic**Prossimo**. 

   **Aggiunta di set di dati e origini dati** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_5.png)



 Aspose.Cells.Report.Designer avvia Microsoft Query.

1.  Nella finestra di dialogo Scegli origine dati, selezionare**Nuova origine dati**.
1.  Clic**OK**.
 Puoi anche selezionare un'origine dati esistente.

   **Scelta di un'origine dati** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_6.png)




1. Immettere un nome per l'origine dati e selezionare SQL Server dall'elenco a discesa dei driver di database.
1.  Clic**Collegare**. 

   **Creazione di una nuova origine dati** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_7.png)




1. Nella finestra di dialogo Accesso a SQL Server selezionare il valore appropriato per ogni elemento.
 Ad esempio, imposta il server su locale, seleziona il database AdventureWorks e seleziona**Usa connessione affidabile**.
1.  Clic**OK**. 

   **Accesso al server SQL** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_8.png)




1.  Clic**OK**. 

   **Si noti che ora siamo connessi al server SQL** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_9.png)



La nuova origine dati viene visualizzata nel file**Scegli Origine dati** dialogo.

1.  Seleziona la nuova origine dati.

   **La nuova origine dati** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_10.png)




1.  Clic**OK** per aprire Microsoft Query.
1.  Per creare una query in Microsoft Query, fare riferimento a Microsoft Query Helper. Nell'esempio seguente creiamo una query con parametri.

   **Costruire una query** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_11.png)



 L'SQL è il seguente:

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


La query ha tre parametri: ReportYear, ReportMonth e EmpID.

1.  Da Microsoft Query**File** menù, selezionare**Torna a Aspose.Cells.Report.Designer**. 

   **Tornando al progettista di report** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_12.png)



 L'origine dati e la query create in precedenza sono elencate nella finestra di dialogo.

1.  Fare clic sull'origine dati**Server SQL** per visualizzarne le informazioni dettagliate.

   **La nuova origine dati** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_13.png)




1.  Fare clic sulla query EmpSalesDetails per visualizzarne le informazioni dettagliate.

   **Fare clic sulla scheda SQL per visualizzare l'sql per la query** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_14.png)



**Fare clic sulla scheda Colonne per visualizzare le colonne della query** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_15.png)



**Fare clic sulla scheda Parametri per visualizzare i parametri della query** 

![cose da fare:immagine_alt_testo](creating-new-data-sources-and-queries_16.png)



