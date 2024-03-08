---
title: Asse della data
description: Scopri come gestire l'asse delle date in Aspose.Cells for Java. La nostra guida ti aiuterà a capire come lavorare con vari formati di data, scale temporali e frequenze di etichette di spunta.
keywords: Aspose.Cells for Java, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /it/java/date-axis/
---
##  **Possibili scenari di utilizzo**
Quando crei un grafico dai dati del foglio di lavoro che utilizza le date e le date vengono tracciate lungo l'asse orizzontale (categoria) nel grafico, Aspose.cells modifica automaticamente l'asse delle categorie in un asse delle date (scala temporale).
Un asse delle date visualizza le date in ordine cronologico a intervalli o unità di base specifici, ad esempio il numero di giorni, mesi o anni, anche se le date nel foglio di lavoro non sono in ordine sequenziale o nelle stesse unità di base.
Per impostazione predefinita, Aspose.cells determina le unità di base per l'asse delle date in base alla differenza più piccola tra due date qualsiasi nei dati del foglio di lavoro. Ad esempio, se disponi di dati sui prezzi delle azioni in cui la differenza più piccola tra le date è sette giorni, Excel imposta l'unità di base su giorni, ma puoi modificare l'unità di base su mesi o anni se desideri visualizzare la performance delle azioni nel corso un periodo di tempo più lungo.
##  **Gestisci l'asse della data come Microsoft Excel**
 Consulta il seguente codice di esempio che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro.
 Quindi aggiungiamo un grafico e impostiamo il tipo di file[**Asse**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
 A[**Scala temporale**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) e quindi impostare le unità di base su Giorni.

![cose da fare:immagine_alt_testo](excel.png)

 Il seguente codice di esempio genera il file[file Excel di output](DateAxis.xlsx).

##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
