---
title: Lavorare con i Grafici
type: docs
weight: 110
url: /it/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Il modello di report di Aspose.Cells supporta i grafici di Microsoft Excel. Ogni volta che si esegue un report, il grafico viene popolato con i dati più recenti. 

{{% /alert %}} 

Per aggiungere un grafico al modello di report:

1. Prima, crea il set di dati che sarà la sorgente dati per il grafico.
   Di seguito, utilizziamo il database di esempio AdventureWorks fornito con SQL Server Reporting Services 2005 e creiamo un set di dati chiamato Vendite.
   Questo SQL definisce il set di dati: 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



Si prega di fare riferimento a [Data Sources and Queries](/cells/it/reportingservices/data-sources-and-queries/) per saperne di più su come creare un'origine dati e un set di dati in Aspose.Cells.Report.Designer.

1. Crea un report tabulare seguendo le istruzioni in [Creating Tabular Report](/cells/it/reportingservices/creating-tabular-report/). Il report che abbiamo creato per questo esempio è qui sotto. La tabella è la fonte dati del grafico. 

![todo:image_alt_text](working-with-charts_1.png)




1. In Microsoft Excel, fai clic sul menu **Inserisci** e seleziona **Grafico**.
1. Fare clic su **Avanti**. 

![todo:image_alt_text](working-with-charts_2.png)




1. Fai clic sulla scheda **Serie**. 

![todo:image_alt_text](working-with-charts_3.png)




1. Fare clic su **Aggiungi**. 

![todo:image_alt_text](working-with-charts_4.png)




1. Nella finestra di dialogo, imposta il valore di Serie1 (serie Trimestre) al primo campo dati della tabella.
   Nel campione, si tratta di “VenditeAziendali!$C$3:$C$3”. Il primo $C$3 è l'indice della prima riga del “Trimestre” e il secondo $C$3 è un segnaposto per l'indice dell'ultima riga del “Trimestre” e verrà sostituito con l'effettivo indice di riga dei dati della tabella al momento del rendering. Imposta le etichette dell'asse delle categorie(X) su “=VenditeAziendali!$C$3:$C$3”. 

![todo:image_alt_text](working-with-charts_5.png)




1. Fai clic su **Aggiungi** per aggiungere un'altra serie.
   Nell'esempio, abbiamo aggiunto la serie delle vendite. 
1. Imposta il valore di Serie2 (serie Vendite) al secondo campo dati della tabella.
   Nell'esempio è “VenditeAziendali!$D$3:$D$3”. Il primo $D$3 è l'indice della prima riga delle “Vendite” e il secondo $D$3 è un segnaposto per l'indice dell'ultima riga delle “Vendite” e verrà sostituito con l'effettivo indice di riga dei dati della tabella al momento del rendering. 
1. Fare clic su **Avanti** per continuare. 

![todo:image_alt_text](working-with-charts_6.png)




1. Nella finestra di dialogo, imposta il titolo del grafico e l'asse delle categorie(X).
1. Fai clic su **Fine** per completare il lavoro. 

![todo:image_alt_text](working-with-charts_7.png)



Il modello assomiglia a quanto segue. 

![todo:image_alt_text](working-with-charts_8.png)




1. Salva il rapporto e pubblicalo sul Server dei Rapporti.
1. Esporta il rapporto dal Server dei Rapporti.
   Il risultato è come segue. 

![todo:image_alt_text](working-with-charts_9.png)
