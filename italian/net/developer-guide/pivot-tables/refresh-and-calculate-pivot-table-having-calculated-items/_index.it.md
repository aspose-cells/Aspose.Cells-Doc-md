---
title: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 40
url: /it/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells ora supporta l'aggiornamento e il calcolo della tabella pivot con elementi calcolati. Si prega di utilizzare il[**Tabella pivot.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) e[**Tabella pivot.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) come al solito per eseguire questa funzione.

{{% /alert %}}

## **Aggiorna e calcola la tabella pivot con elementi calcolati**

 Il codice di esempio seguente carica il file[file excel di origine](5115238.xlsx)che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Per prima cosa modifichiamo il valore della cella D2 in 20, quindi aggiorniamo e calcoliamo la tabella pivot utilizzando le API Aspose.Cells e salviamo la cartella di lavoro in formato PDF. I risultati nel[uscita PDF](5115229.pdf) mostra che Aspose.Cells ha aggiornato e calcolato la tabella pivot avendo calcolato correttamente gli elementi. Puoi verificarlo utilizzando Microsoft Excel inserendo manualmente il valore 20 nella cella D2 e quindi aggiornando la tabella pivot tramite il tasto di scelta rapida Alt + F5 o facendo clic sul pulsante Aggiorna tabella pivot.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
