---
title: Nomi e Indici
type: docs
weight: 10
url: /it/cpp/names-and-indices/
---
## **Ottieni il nome Cell dagli indici di riga e colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come.
Aspose.Cells fornisce il metodo ICellsHelper.CellIndexToName_i che consente agli sviluppatori di ottenere il nome di una cella se forniscono l'indice di riga e colonna.

{{% alert color="primary" %}} 

differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare ICellsHelper.CellIndexToName_i per accedere al nome di una cella in base a un indice di riga e colonna noto. Il codice genera il seguente output.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Ottieni gli indici di riga e colonna dal nome Cell**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.
Aspose.Cells fornisce il metodo ICellsHelper.CellNameToIndex_i che consente agli sviluppatori di ottenere un indice di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

differenza di Microsoft Excel, dove gli indici di riga e colonna iniziano da 1, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il codice di esempio seguente illustra come utilizzare CellsHelper.CellNameToIndex per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera il seguente output.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
