---
title: Asse della data
type: docs
weight: 200
url: /it/net/date-axis/
---
## **Possibili scenari di utilizzo**
Quando crei un grafico dai dati del foglio di lavoro che utilizza le date e le date vengono tracciate lungo l'asse orizzontale (categoria) nel grafico, Aspose.cells modifica automaticamente l'asse delle categorie in un asse della data (scala temporale).
Un asse della data visualizza le date in ordine cronologico a intervalli o unità di base specifici, ad esempio il numero di giorni, mesi o anni, anche se le date nel foglio di lavoro non sono in ordine sequenziale o nelle stesse unità di base.
Per impostazione predefinita, Aspose.cells determina le unità di base per l'asse della data in base alla minima differenza tra due date qualsiasi nei dati del foglio di lavoro. Ad esempio, se si dispone di dati per i prezzi delle azioni in cui la differenza minima tra le date è di sette giorni, Excel imposta l'unità di base su giorni, ma è possibile modificare l'unità di base su mesi o anni se si desidera vedere la performance del titolo nel corso un periodo di tempo più lungo.
## **Gestisci l'asse della data come Microsoft Excel**
 Si prega di vedere il seguente codice di esempio che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro.
 Quindi aggiungiamo un grafico e impostiamo il tipo di file[**Asse**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 a[**Scala temporale**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) e quindi imposta le unità di base su Giorni.

![cose da fare:immagine_alt_testo](excel.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
