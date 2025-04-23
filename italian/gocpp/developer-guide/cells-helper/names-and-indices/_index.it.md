---
title: Nomi e Indici
type: docs
weight: 10
url: /it/go-cpp/names-and-indices/
---

## **Ottieni il Nome della Cella dagli Indici di Riga e Colonna**

È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come fare.
Aspose.Cells fornisce il metodo [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/), che permette agli sviluppatori di ottenere il nome di una cella fornendo l'indice di riga e colonna.

{{% alert color="primary" %}}

A differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}}

Il seguente esempio di codice illustra come utilizzare [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/) per accedere al nome di una cella dato un indice di riga e colonna noti. Il codice genera il seguente output.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **Ottieni Gli Indici di Riga e Colonna dal Nome della Cella**

È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.
Aspose.Cells fornisce il metodo [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/), che permette agli sviluppatori di ottenere un indice di riga e colonna partendo dal nome della cella.

{{% alert color="primary" %}}

A differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}}

 Il seguente esempio di codice illustra come utilizzare [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/) per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera il seguente output.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}
