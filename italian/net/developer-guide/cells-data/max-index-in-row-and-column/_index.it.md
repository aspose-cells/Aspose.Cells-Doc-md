---
title: Ottenere l Indice Massimo della Colonna nella Riga e l Indice Massimo della Riga nella Colonna
type: docs
weight: 600
url: /it/net/get-max-index-in-row-and-column/
description: Impara come ottenere l Indice della Colonna Massima nella Riga e l Indice della Riga Massima nella Colonna attraverso l API Aspose.Cells for .NET.
keywords: Ottieni l Indice della Colonna Massima nella Riga, Ottieni l Indice della Riga Massima nella Colonna, Ottieni l Indice della Colonna Dati Massima nella Riga, Ottieni l Indice della Riga Dati Massima nella Colonna. 
---

## **Possibili Scenari di Utilizzo**
Quando devi manipolare solo alcuni dati sulle righe o colonne, devi conoscere l'intervallo di dati delle righe e delle colonne. Aspose.Cells offre questa funzionalità. Per ottenere l'indice massimo della colonna su una riga, puoi ottenere le proprietà [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) e [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/), e quindi utilizzare la proprietà [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) per ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati. Ma per ottenere l'indice massimo della riga e l'indice massimo dei dati della riga su una colonna, è necessario creare un intervallo sulla colonna, quindi attraversare l'intervallo per trovare l'ultima cella, e infine ottenere l'attributo [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) sulla cella.

Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Ottieni l'Indice della Colonna Massima nella Riga e l'Indice della Riga Massima nella Colonna usando Aspose.Cells**
Questo esempio mostra come:

1. Caricare il [file di esempio](sample.xlsx).
1. Ottenere la riga che ha bisogno di ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati.
1. Ottieni l'attributo [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) sulla cella.
1. Creare un intervallo basato sulla colonna.
1. Ottenere l'iteratore e attraversare l'intervallo.
1. Ottieni l'attributo [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) sulla cella.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
