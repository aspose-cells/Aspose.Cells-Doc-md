---
title: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 40
url: /it/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells ora supporta l'aggiornamento e il calcolo della tabella pivot con elementi calcolati. Si prega di utilizzare [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) e [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) come di consueto per eseguire questa funzione.

{{% /alert %}}

## **Aggiornare e calcolare la tabella pivot con elementi calcolati**

Il seguente codice di esempio carica il [file Excel di origine](5115238.xlsx) che contiene una tabella pivot con tre elementi calcolati come "aggiungi", "dividi", "dividi2". Cambiamo prima il valore della cella D2 in 20 e quindi aggiorniamo e calcoliamo la tabella pivot utilizzando le API di Aspose.Cells e salviamo il workbook in formato PDF. I risultati nel [PDF di output](5115229.pdf) mostrano che Aspose.Cells ha aggiornato e calcolato correttamente la tabella pivot con elementi calcolati. È possibile verificarlo utilizzando Microsoft Excel mettendo manualmente il valore 20 nella cella D2 e poi aggiornando la tabella pivot tramite il tasto di scelta rapida Alt+F5 o facendo clic sul pulsante di aggiornamento della tabella pivot.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
