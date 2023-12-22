---
title: Aggiorna e calcola la tabella pivot con gli elementi calcolati
type: docs
weight: 40
url: /it/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Questo articolo mostra come aggiornare e calcolare la tabella pivot avendo elementi calcolati con Aspose.Cells for Python via .NET.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET ora supporta l'aggiornamento e il calcolo della tabella pivot con elementi calcolati. Si prega di utilizzare il[**Tabella pivot.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) E[**Tabella pivot.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) come al solito per eseguire questa funzione.

{{% /alert %}}

##  **Aggiorna e calcola la tabella pivot con gli elementi calcolati**

 Il codice di esempio seguente carica il file[file Excel di origine](5115238.xlsx)che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Per prima cosa modifichiamo il valore della cella D2 in 20, quindi aggiorniamo e calcoliamo la tabella pivot utilizzando le API Aspose.Cells for Python via .NET e salviamo la cartella di lavoro nel formato PDF. I risultati in[uscita PDF](5115229.pdf) mostra che Aspose.Cells for Python via .NET ha aggiornato e calcolato la tabella pivot avendo calcolato gli elementi correttamente. Puoi verificarlo utilizzando Microsoft Excel inserendo manualmente il valore 20 nella cella D2 e quindi aggiornando la tabella pivot tramite il tasto di scelta rapida Alt+F5 o facendo clic sul pulsante Aggiorna tabella pivot.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
