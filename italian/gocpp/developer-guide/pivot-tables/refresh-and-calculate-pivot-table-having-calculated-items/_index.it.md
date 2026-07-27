---
title: Aggiorna e calcola la tabella pivot con elementi calcolati usando Golang tramite C++
linktitle: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 40
url: /it/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aggiorna e calcola la tabella pivot con elementi calcolati usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells ora supporta l'aggiornamento e il calcolo della tabella pivot con elementi calcolati. Si prega di utilizzare [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) e [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) come di consueto per eseguire questa funzione.

{{% /alert %}}

## **Aggiornare e calcolare la tabella pivot con elementi calcolati**

 Il seguente esempio di codice carica il [file Excel di origine](5115238.xlsx) che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Per prima cosa cambiamo il valore della cella D2 a 20, poi aggiorniamo e calcoliamo la tabella pivot utilizzando le API di Aspose.Cells e salviamo il workbook in formato PDF. I risultati nel [PDF di output](5115229.pdf) mostrano che Aspose.Cells ha aggiornato e calcolato con successo la tabella pivot con elementi calcolati. Puoi verificarlo manualmente inserendo il valore 20 in cella D2 e aggiornando la tabella pivot tramite il tasto rapido Alt+F5 o cliccando sul pulsante di aggiornamento della tabella pivot.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
