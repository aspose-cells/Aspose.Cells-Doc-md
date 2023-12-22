---
title: Ottieni l'indice Cells
type: docs
weight: 600
url: /it/net/get-cells-index/
description: Scopri come inserire una riga o una colonna con il nome di riga, colonna o celle. Converti il nome della cella nell'indice di riga e colonna in base zero.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
La visualizzazione predefinita di Excel è il riferimento allo stile A1, ciascuna colonna è definita come A, B, C.... e le celle sono denominate A1, B2, C3... e così via.
Potresti voler sapere in quale riga e colonna si trova questa cella.

{{% /alert %}}


##  **Possibili scenari di utilizzo**
 Quando hai solo bisogno di manipolare dati specifici sul foglio di lavoro tramite l'indice di riga e colonna, devi conoscere gli indici di colonna e colonna di quella cella specifica.
 Aspose.Cells offre questa funzionalità per ottenere l'indice di righe e colonne in base al nome della riga, colonna e cella.
Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Nota: l'indicizzazione è in base zero in Aspose.Cells per .Net, ma l'ID di riga è in base uno in MS Excel.

##  **Ottieni gli indici Cells utilizzando Aspose.Cells**
Questo esempio mostra come:

1. Crea una cartella di lavoro e aggiungi alcuni dati.
1. Trova la cella specifica nel primo foglio di lavoro.
1. Ottieni l'indice della riga e l'indice della colonna in base al nome della cella.
1. Ottieni l'indice della colonna in base al nome della colonna.
1. Ottieni l'indice della riga in base al nome della riga.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}