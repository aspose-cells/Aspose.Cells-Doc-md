---
title: Ottenere l indice delle celle
type: docs
weight: 600
url: /it/net/get-cells-index/
description: Scopri come ottenere la riga o la colonna per nome di riga, colonna o celle. Converti il nome della cella in un indice di riga e colonna in base zero.
keywords: Ottieni l indice di riga e l indice di colonna per il nome della cella, Ottieni l indice di colonna per il nome della colonna, Ottieni l indice di riga per il nome della riga, Ottieni l indice per il nome della cella. 
---

{{% alert color="primary" %}}
La visualizzazione predefinita di Excel è il riferimento in stile A1, ogni colonna è definita come A, B, C...., e le celle sono denominate come A1, B2, C3... e così via.
Potresti voler sapere in quale riga e colonna si trova questa cella.

{{% /alert %}}


## **Possibili Scenari di Utilizzo**
Quando hai bisogno solo di manipolare un dato specifico nel foglio di lavoro per indice di riga e colonna, devi conoscere gli indici di riga e colonna di quella cella specifica. 
Aspose.Cells offre questa funzione per ottenere l'indice di riga e colonna per il nome della riga, colonna e cella. 
Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Nota: L'indicizzazione è a base zero in Aspose.Cells per .Net, ma l'id della riga è a base uno in MS Excel.

## **Ottieni Gli Indici delle Celle utilizzando Aspose.Cells**
Questo esempio mostra come:

1. Creare un workbook e aggiungere alcuni dati.
1. Trova la cella specifica nel primo foglio di lavoro.
1. Ottieni l'indice di riga e l'indice di colonna per nome della cella.
1. Ottieni l'indice di colonna per nome della colonna.
1. Ottieni l'indice di riga per nome della riga.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
