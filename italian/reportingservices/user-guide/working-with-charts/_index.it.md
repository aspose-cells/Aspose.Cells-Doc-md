---
title: Lavorare con i grafici
type: docs
weight: 110
url: /it/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

 Aspose.Cells Il modello di rapporto supporta i grafici Microsoft Excel. Ogni volta che si esegue un report, il grafico viene popolato con i dati più recenti.

{{% /alert %}} 

Per aggiungere un grafico al modello di rapporto:

1. Innanzitutto, crea il set di dati che sarà l'origine dati per il grafico.
 Di seguito viene utilizzato il database di esempio AdventureWorks fornito con SQL Server Reporting Services 2005 e viene creato un set di dati denominato Sales.
 Questo SQL definisce il set di dati:

**SQL**

{{< highlight "csharp" >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



 Per favore riferisci a[Origini dati e query](/cells/it/reportingservices/data-sources-and-queries/) per ulteriori informazioni su come creare un'origine dati e un set di dati in Aspose.Cells.Report.Designer.

1. Creare un rapporto tabulare secondo le istruzioni in[Creazione di report tabulari](/cells/it/reportingservices/creating-tabular-report/) . Il report che abbiamo creato per questo esempio è riportato di seguito. La tabella è l'origine dati del grafico.

![cose da fare:immagine_alt_testo](working-with-charts_1.png)




1.  In Microsoft Excel, fare clic su**Inserire** menu e selezionare**Grafico**.
1.  Clic**Prossimo**. 

![cose da fare:immagine_alt_testo](working-with-charts_2.png)




1.  Clicca il**Serie** scheda.

![cose da fare:immagine_alt_testo](working-with-charts_3.png)




1.  Clic**Aggiungere**. 

![cose da fare:immagine_alt_testo](working-with-charts_4.png)




1. Nella finestra di dialogo impostare il valore di Series1 (Quarter series) sul primo campo dati della tabella.
 Nell'esempio, è "CompanySales!$C$3:$C$3". Il primo $C$3 è l'indice della prima riga di "Trimestre" e il secondo $C$3 è un segnaposto per l'indice dell'ultima riga di "Trimestre" e verrà sostituito con l'indice di riga reale dei dati della tabella al momento del rendering. Impostare le etichette dell'asse delle categorie (X) su "=CompanySales!$C$3:$C$3".

![cose da fare:immagine_alt_testo](working-with-charts_5.png)




1.  Clic**Aggiungere** per aggiungere un'altra serie.
 Nell'esempio abbiamo aggiunto la serie di vendite.
1. Impostare il valore di Series2 (Sales series) nel secondo campo dati della tabella.
Nell'esempio è "CompanySales!$D$3:$D$3". Il primo $D$3 è l'indice della prima riga di "Sales" e il secondo $D$3 è un segnaposto per l'ultimo indice della riga di "Sales" e verrà sostituito con l'indice di riga reale dei dati della tabella al momento del rendering.
1.  Clic**Prossimo** continuare.

![cose da fare:immagine_alt_testo](working-with-charts_6.png)




1. Nella finestra di dialogo, impostare il titolo del grafico e l'asse delle categorie (X).
1.  Clic**Fine** per completare l'opera.

![cose da fare:immagine_alt_testo](working-with-charts_7.png)



 Il modello è simile al seguente.

![cose da fare:immagine_alt_testo](working-with-charts_8.png)




1. Salvare il report e pubblicarlo nel server di report.
1. Esportare il report dal server di report.
 Il risultato è il seguente.

![cose da fare:immagine_alt_testo](working-with-charts_9.png)
