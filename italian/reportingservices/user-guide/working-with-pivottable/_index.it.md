---
title: Lavorare con la tabella pivot
type: docs
weight: 100
url: /it/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 UN*tabella pivot* è una tabella interattiva che riassume i dati e li presenta in modo significativo. SQL Server Reporting Services non può esportare un report nel formato Excel di Microsft mantenendo una tabella pivot. Gli utenti dei report devono creare manualmente tabelle pivot ogni volta che esportano un report tabella pivot da Reporting Services a Microsoft Excel. Con Aspose.Cells for Reporting Services, puoi progettare una tabella pivot una sola volta al momento della progettazione del report. Ogni volta che viene eseguito il report, Aspose.Cells for Reporting Services esporta il report in Microsoft Excel e aggiorna i dati nella tabella pivot.

{{% /alert %}} 

Per creare un rapporto tabella pivot:

1. Crea un set di dati come origine dati per la tabella pivot.
 Di seguito viene utilizzato il database di esempio AdventureWorks fornito con SQL Server Reporting Services 2005 e viene creato un set di dati denominato "sales".
L'SQL per il set di dati è il seguente:

**SQL**

{{< highlight "csharp" >}}

 SELECT  PC.Name AS ProdCat,

	    PS.Name AS SubCat,

	    DATEPART(yy, SOH.OrderDate) AS OrderYear,

	    'Q' + DATENAME(qq, SOH.OrderDate) AS OrderQtr,

         SUM(SOD.UnitPrice * SOD.OrderQty) AS Sales

FROM    Production.ProductSubcategory PS INNER JOIN

         Sales.SalesOrderHeader SOH INNER JOIN

         Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID INNER JOIN

         Production.Product P ON SOD.ProductID = P.ProductID ON PS.ProductSubcategoryID = P.ProductSubcategoryID INNER JOIN

         Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID

WHERE   (SOH.OrderDate BETWEEN '1/1/2002' AND '12/31/2003')

GROUP BY  DATEPART(yy, SOH.OrderDate), PC.Name, PS.Name, 'Q' + DATENAME(qq, SOH.OrderDate), PS.ProductSubcategoryID



{{< /highlight >}}



{{% alert color="primary" %}} 

 Per favore riferisci a[Origini dati e query](/cells/it/reportingservices/data-sources-and-queries/) per ulteriori informazioni su come creare un'origine dati e un set di dati con Aspose.Cells.Report.Designer.

{{% /alert %}} 

1.  Creare un report tabellare secondo le istruzioni in[Creazione di report tabulari](/cells/it/reportingservices/creating-tabular-report/), come mostrato di seguito.
 La tabella sarà l'origine dati per la tabella pivot.

![cose da fare:immagine_alt_testo](working-with-pivottable_1.png)




1.  In Microsoft Excel, dal file**Inserire** menù, selezionare**Nome** poi**Definire**.
1. Definire un nome come "vendite".
 L'intervallo del nome inizia con la prima cella del titolo dell'intestazione e termina con l'ultima cella della riga di dati della tabella, come mostrato di seguito.

![cose da fare:immagine_alt_testo](working-with-pivottable_2.png)




1.  Clic**OK** finire.
1. Crea un nuovo foglio per la tabella pivot.
1.  Dal**Dati** menù, selezionare**Rapporto tabella pivot e grafico pivot** per aggiungere una tabella pivot.
 Viene visualizzata una finestra di dialogo.
1.  Selezionare**Elenco o database di Microsoft Office Excel** come fonte di dati e**tabella pivot** come tipo di rapporto.
1.  Clic**Prossimo** continuare.

![cose da fare:immagine_alt_testo](working-with-pivottable_3.png)




1. Nella finestra di dialogo, inserisci "vendite", il nome che hai definito sopra.
1.  Clic**Prossimo** continuare.

![cose da fare:immagine_alt_testo](working-with-pivottable_4.png)




1.  Clic**Fine**. 

![cose da fare:immagine_alt_testo](working-with-pivottable_5.png)




1.  Progetta la tabella pivot in Excel.

![cose da fare:immagine_alt_testo](working-with-pivottable_6.png)



 La tabella pivot progettata è mostrata di seguito.

![cose da fare:immagine_alt_testo](working-with-pivottable_7.png)




1.  Fai clic con il pulsante destro del mouse sulla tabella pivot e seleziona**Opzioni tabella**.
1.  Assicurati che**Aggiorna all'apertura** è selezionato.

![cose da fare:immagine_alt_testo](working-with-pivottable_8.png)




1. Salvare il report e pubblicarlo nel server di report.
1. Esportare il report dal server di report.
 Il risultato è mostrato di seguito.

![cose da fare:immagine_alt_testo](working-with-pivottable_9.png)
