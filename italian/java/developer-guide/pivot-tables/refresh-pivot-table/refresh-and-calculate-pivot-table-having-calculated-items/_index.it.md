---
title: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 130
url: /it/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells ora supporta l'aggiornamento e il calcolo della tabella pivot con elementi calcolati. Si prega di utilizzare [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) e [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) come al solito per eseguire questa funzione.

{{% /alert %}}

## **Aggiornare e calcolare la tabella pivot con elementi calcolati**

Il seguente codice di esempio carica il [file excel di origine](5473428.xlsx) che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Prima cambiamo il valore della cella D2 a 20 e poi aggiorniamo e calcoliamo la tabella pivot utilizzando le API Aspose.Cells e salviamo il workbook in formato PDF. I risultati nel [PDF di output](5473431.pdf) mostrano che Aspose.Cells ha aggiornato e calcolato con successo la tabella pivot con elementi calcolati. Puoi verificarlo utilizzando Microsoft Excel inserendo manualmente il valore 20 nella cella D2 e quindi aggiornando la tabella pivot tramite il tasto di scelta rapida Alt+F5 o cliccando sul pulsante Aggiorna tabella pivot.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
{{< app/cells/assistant language="java" >}}
