---
title: Ottieni l indice massimo di colonna in una riga e l indice massimo di riga in una colonna con Golang tramite C++
linktitle: Ottenere l Indice Massimo della Colonna nella Riga e l Indice Massimo della Riga nella Colonna
type: docs
weight: 600
url: /it/go-cpp/get-max-index-in-row-and-column/
description: Impara come ottenere il Max Indice di Colonna in Riga e il Max Indice di Riga in Colonna tramite l API Aspose.Cells for C++.
keywords: Ottieni l Indice della Colonna Massima nella Riga, Ottieni l Indice della Riga Massima nella Colonna, Ottieni l Indice della Colonna Dati Massima nella Riga, Ottieni l Indice della Riga Dati Massima nella Colonna.
---

## **Possibili Scenari di Utilizzo**
Quando devi manipolare solo alcuni dati sulle righe o colonne, devi conoscere l'intervallo di dati di righe e colonne. Aspose.Cells offre questa funzionalità. Per ottenere l'indice massimo di colonna su una riga, puoi ottenere le proprietà [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) e [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), e poi usare la proprietà [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) per ottenere l'indice massimo di colonna e l'indice massimo di colonna di dati. Ma per ottenere l'indice massimo di riga e l'indice massimo di dati di riga su una colonna, devi creare un intervallo sulla colonna, quindi attraversare l'intervallo per trovare l'ultima cella, e infine ottenere l'attributo [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) sulla cella.

Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Ottieni l'Indice della Colonna Massima nella Riga e l'Indice della Riga Massima nella Colonna usando Aspose.Cells**
Questo esempio mostra come:

1. Caricare il [file di esempio](sample.xlsx).
1. Ottenere la riga che ha bisogno di ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati.
1. Ottieni l'attributo [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) sulla cella.
1. Creare un intervallo basato sulla colonna.
1. Ottenere l'iteratore e attraversare l'intervallo.
1. Ottieni l'attributo [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) sulla cella.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
