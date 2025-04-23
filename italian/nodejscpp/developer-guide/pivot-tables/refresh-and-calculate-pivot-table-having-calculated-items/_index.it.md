---
title: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 40
url: /it/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ ora supporta l’aggiornamento e il calcolo di tabelle pivot con elementi calcolati. Utilizza normalmente i placeholder [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) e [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) per eseguire questa funzione.

{{% /alert %}}

## **Aggiornare e calcolare la tabella pivot con elementi calcolati**

Il seguente esempio di codice carica il [file Excel di origine](5115238.xlsx) che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Innanzitutto, cambiamo il valore della cella D2 in 20, quindi aggiorniamo e calcoliamo la tabella pivot usando le API di Aspose.Cells for Node.js via C++ e salviamo il file in formato PDF. I risultati nel [PDF di output](5115229.pdf) mostrano che Aspose.Cells for Node.js via C++ ha aggiornato e calcolato con successo la tabella pivot con elementi calcolati. Puoi verificarlo utilizzando Microsoft Excel inserendo manualmente il valore 20 in D2 e aggiornando la tabella pivot tramite il tasto di scelta rapida Alt+F5 o cliccando sul pulsante Aggiorna nella tabella pivot.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

