---
title: Inserisci i dati della cella della scheda di lavoro di GridWeb nel formato percentuale
type: docs
weight: 80
url: /it/net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: Questo articolo introduce l inserimento dei dati della cella con il formato percentuale in GridWeb.
---


## **Possibili Scenari di Utilizzo**
GridWeb ora supporta gli utenti nell'inserire i dati della cella nel formato percentuale come 3% e i dati nella cella saranno automaticamente formattati come 3.00%. Tuttavia, sarà necessario impostare lo stile della cella nel formato percentuale, che può essere GridTableItemStyle.NumberType a 9 o 10. Il numero 9 formattarà 3% come 3%, ma il numero 10 formattarà 3% come 3.00%

{{% alert color="primary" %}} 

Se non hai impostato lo stile della cella nel formato percentuale, quindi i dati di input 3% verranno visualizzati come 0.03.

{{% /alert %}} 
## **Inserisci i dati della cella della scheda di lavoro di GridWeb nel formato percentuale**
Il seguente codice di esempio imposta la cella A1 GridTableItemStyle.NumberType come 10, pertanto i dati di input 3% verranno automaticamente formattati come 3.00% come mostrato nello screenshot.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Codice di Esempio**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
