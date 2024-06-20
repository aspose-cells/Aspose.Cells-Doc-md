---
title: Lavorare con la tabella pivot
type: docs
weight: 100
url: /it/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

Una *tabella pivot* è una tabella interattiva che riassume i dati e li presenta in modo significativo. Microsoft SQL Server Reporting Services non può esportare un report nel formato Microsoft Excel mantenendo una tabella pivot. Gli utenti del report devono creare manualmente tabelle pivot ogni volta che esportano un report con tabella pivot da Reporting Services a Microsoft Excel. Con Aspose.Cells for Reporting Services, è possibile progettare una tabella pivot una volta durante la progettazione del report. Ogni volta che viene eseguito il report, Aspose.Cells for Reporting Services esporta il report in Microsoft Excel e aggiorna i dati nella tabella pivot.

{{% /alert %}} 

Per creare un report con tabella pivot:

1. Creare un set di dati come origine dati per la tabella pivot.
   Di seguito, utilizziamo il database di esempio AdventureWorks fornito con SQL Server Reporting Services 2005 e creiamo un set di dati denominato “vendite”.
   Il codice SQL per il set di dati è il seguente: 

**SQL**

{{< highlight csharp >}}

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

Consultare [Origini dati e query](/cells/it/reportingservices/data-sources-and-queries/) per saperne di più su come creare un'origine dati e un set di dati con Aspose.Cells.Report.Designer.

{{% /alert %}} 

1. Creare un report a tabella secondo le istruzioni in [Creazione di un report tabulare](/cells/it/reportingservices/creating-tabular-report/), come mostrato di seguito.
   La tabella sarà l'origine dati per la tabella pivot. 

![todo:image_alt_text](working-with-pivottable_1.png)




1. In Microsoft Excel, dal menu **Inserisci**, selezionare **Nome** e quindi **Definisci**.
1. Definisci un nome come “vendite”.
   L'intervallo del nome inizia con la prima cella del titolo dell'intestazione e termina con l'ultima cella della riga dei dati della tabella come mostrato di seguito. 

![todo:image_alt_text](working-with-pivottable_2.png)




1. Fai clic su **OK** per terminare.
1. Crea un nuovo foglio per la tabella pivot.
1. Dal menu **Dati**, seleziona **Tabella Pivot e Grafico Pivot** per aggiungere una tabella pivot.
   Viene visualizzata una finestra di dialogo.
1. Seleziona **Elenco o database di Microsoft Office Excel** come origine dati e **tabella pivot** come tipo di rapporto.
1. Fare clic su **Avanti** per continuare. 

![todo:image_alt_text](working-with-pivottable_3.png)




1. Nella finestra di dialogo, inserisci “vendite”, il nome che hai definito in precedenza.
1. Fare clic su **Avanti** per continuare. 

![todo:image_alt_text](working-with-pivottable_4.png)




1. Fare clic su **Fine**. 

![todo:image_alt_text](working-with-pivottable_5.png)




1. Progetta la tabella pivot in Excel. 

![todo:image_alt_text](working-with-pivottable_6.png)



La tabella pivot progettata è mostrata di seguito. 

![todo:image_alt_text](working-with-pivottable_7.png)




1. Fare clic con il tasto destro sulla tabella pivot e selezionare **Opzioni Tabella**.
1. Assicurati che sia selezionata l'opzione **Aggiorna all'apertura**. 

![todo:image_alt_text](working-with-pivottable_8.png)




1. Salva il rapporto e pubblicalo sul Server dei Rapporti.
1. Esporta il rapporto dal Server dei Rapporti.
   Il risultato è mostrato di seguito. 

![todo:image_alt_text](working-with-pivottable_9.png)
