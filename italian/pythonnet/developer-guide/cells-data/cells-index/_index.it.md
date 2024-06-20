---
title: Ottenere l indice delle celle
type: docs
weight: 600
url: /it/python-net/get-cells-index/
description: Scopri come ottenere la riga o la colonna per nome della riga attraverso l API Aspose.Cells per Python via .NET, colonna o celle. Converti il nome della cella in un indice di riga e colonna a base zero attraverso l API Aspose.Cells per Python via .NET.
keywords: Excel Python, Ottieni l indice di riga e l indice di colonna per nome della cella usando Python, Ottieni l indice di colonna per nome della colonna usando Python, Ottieni l indice di riga per nome della riga usando Python, Ottieni l indice per nome della cella usando Python. 
---

{{% alert color="primary" %}}
La visualizzazione predefinita di Excel è il riferimento in stile A1, ogni colonna è definita come A, B, C...., e le celle sono denominate come A1, B2, C3... e così via.
Potresti voler sapere in quale riga e colonna si trova questa cella.

{{% /alert %}}


## **Possibili Scenari di Utilizzo**
Quando hai bisogno solo di manipolare un dato specifico nel foglio di lavoro per indice di riga e colonna, devi conoscere gli indici di riga e colonna di quella cella specifica. 
Aspose.Cells per Python via .NET offre questa funzionalità per ottenere l'indice di riga e colonna per nome della riga, colonna e cella. 
Aspose.Cells per Python via .NET fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Nota: L'indicizzazione è a base zero in Aspose.Cells per Python via .NET, ma l'id della riga è basato su uno in MS Excel.

## **Ottieni Indici delle Celle utilizzando la Libreria Excel Aspose.Cells per Python**
Questo esempio mostra come:

1. Creare un workbook e aggiungere alcuni dati.
1. Trova la cella specifica nel primo foglio di lavoro.
1. Ottieni l'indice di riga e l'indice di colonna per nome della cella.
1. Ottieni l'indice di colonna per nome della colonna.
1. Ottieni l'indice di riga per nome della riga.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
