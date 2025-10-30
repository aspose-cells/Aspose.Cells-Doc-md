---
title: Ottenere l indice delle celle con Golang tramite C++
linktitle: Ottenere l indice delle celle
type: docs
weight: 600
url: /it/go-cpp/get-cells-index/
description: Impara come ottenere l indice di riga o colonna tramite il nome di riga, colonna o celle. Convertire il nome della cella in indice di riga e colonna zero based usando Aspose.Cells con Golang tramite C++.
keywords: Ottieni l indice di riga e l indice di colonna per il nome della cella, Ottieni l indice di colonna per il nome della colonna, Ottieni l indice di riga per il nome della riga, Ottieni l indice per il nome della cella.
---

{{% alert color="primary" %}}
La vista predefinita di Excel è il riferimento stile A1, dove ogni colonna è definita come A, B, C..., e le celle sono chiamate A1, B2, C3... e così via.
Potresti voler sapere in quale riga e colonna si trova questa cella.

{{% /alert %}}

## **Possibili Scenari di Utilizzo**

Quando devi manipolare dati specifici nel foglio di lavoro per indice di riga e colonna, devi conoscere gli indici di riga e colonna di quella cella specifica.
Aspose.Cells offre questa funzione per ottenere gli indici di riga e colonna per nome di riga, colonna e cella.
Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi:

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

Nota: L'indicizzazione parte da zero in Aspose.Cells for C++, ma l'id di Row è one-based in MS Excel.

## **Ottieni Gli Indici delle Celle utilizzando Aspose.Cells**

Questo esempio mostra come:

1. Creare un workbook e aggiungere alcuni dati.
1. Trova la cella specifica nel primo foglio di lavoro.
1. Ottieni l'indice di riga e l'indice di colonna per nome della cella.
1. Ottieni l'indice di colonna per nome della colonna.
1. Ottieni l'indice di riga per nome della riga.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
