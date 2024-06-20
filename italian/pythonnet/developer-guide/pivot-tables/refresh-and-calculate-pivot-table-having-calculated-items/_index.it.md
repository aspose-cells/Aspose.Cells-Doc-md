---
title: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 40
url: /it/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Questo articolo mostra come Aggiornare e Calcolare una Tabella Pivot con Elementi Calcolati con Aspose.Cells per Python via .NET.
keywords: Aspose.Cells per Python Excel, libreria Python di Excel, Aggiornare e Calcolare la tabella pivot con elementi calcolati
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET supporta ora l'aggiornamento e il calcolo di una tabella pivot con elementi calcolati. Si prega di utilizzare i [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) e [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) come di consueto per eseguire questa funzione.

{{% /alert %}}

## **Aggiornare e calcolare la tabella pivot con elementi calcolati**

Il seguente codice di esempio carica il [file excel di origine](5115238.xlsx) che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Cambiamo prima il valore della cella D2 a 20 e poi aggiorniamo e calcoliamo la tabella pivot utilizzando le API di Aspose.Cells per Python via .NET e salviamo il foglio di lavoro in formato PDF. I risultati nel [PDF di output](5115229.pdf) mostrano che Aspose.Cells per Python via .NET ha aggiornato e calcolato con successo la tabella pivot con elementi calcolati. Puoi verificarlo usando Microsoft Excel inserendo manualmente il valore 20 nella cella D2 e poi aggiornando la tabella pivot tramite la scorciatoia Alt+F5 o cliccando sul pulsante Aggiorna tabella pivot.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
