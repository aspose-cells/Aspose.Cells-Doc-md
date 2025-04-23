---
title: Ottenere l indice delle celle
type: docs
weight: 600
url: /it/nodejs-cpp/get-cells-index/
description: Scopri come ottenere la riga o la colonna per nome di riga, colonna o celle. Converti il nome della cella in un indice di riga e colonna in base zero.
keywords: Ottieni l indice di riga e l indice di colonna per il nome della cella, Ottieni l indice di colonna per il nome della colonna, Ottieni l indice di riga per il nome della riga, Ottieni l indice per il nome della cella. 
---

{{% alert color="primary" %}}
La visualizzazione predefinita di Excel è il riferimento in stile A1, ogni colonna è definita come A, B, C...., e le celle sono denominate come A1, B2, C3... e così via.
Potresti voler sapere in quale riga e colonna si trova questa cella.

{{% /alert %}}


## **Possibili Scenari di Utilizzo**
Quando hai bisogno solo di manipolare un dato specifico nel foglio di lavoro per indice di riga e colonna, devi conoscere gli indici di riga e colonna di quella cella specifica. 
Aspose.Cells for Node.js via C++ offre questa funzione per ottenere l'indice di riga e colonna in base al nome di riga, colonna e cella. 
Aspose.Cells for Node.js via C++ fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Nota: L'indicizzazione è basata su zero in Aspose.Cells for Node.js via C++, ma l'ID di Riga è uno-based in MS Excel.

## **Ottieni gli Indici delle Celle usando Aspose.Cells for Node.js via C++**
Questo esempio mostra come:

1. Creare un workbook e aggiungere alcuni dati.
1. Trova la cella specifica nel primo foglio di lavoro.
1. Ottieni l'indice di riga e l'indice di colonna per nome della cella.
1. Ottieni l'indice di colonna per nome della colonna.
1. Ottieni l'indice di riga per nome della riga.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
