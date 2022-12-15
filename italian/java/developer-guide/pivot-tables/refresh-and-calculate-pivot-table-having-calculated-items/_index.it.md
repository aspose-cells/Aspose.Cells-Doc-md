---
title: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 130
url: /it/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells ora supporta l'aggiornamento e il calcolo della tabella pivot con elementi calcolati. Si prega di utilizzare[**Tabella pivot.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) e[**Tabella pivot.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) come al solito per eseguire questa funzione.

{{% /alert %}}

## **Aggiorna e calcola la tabella pivot con elementi calcolati**

 Il codice di esempio seguente carica il file[file excel di origine](5473428.xlsx)che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Per prima cosa modifichiamo il valore della cella D2 in 20, quindi aggiorniamo e calcoliamo la tabella pivot utilizzando le API Aspose.Cells e salviamo la cartella di lavoro in formato PDF. I risultati nel[uscita PDF](5473431.pdf) mostra che Aspose.Cells ha aggiornato e calcolato la tabella pivot avendo calcolato correttamente gli elementi. Puoi verificarlo utilizzando Microsoft Excel inserendo manualmente il valore 20 nella cella D2 e quindi aggiornando la tabella pivot tramite il tasto di scelta rapida Alt+F5 o facendo clic sul pulsante Aggiorna tabella pivot.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
