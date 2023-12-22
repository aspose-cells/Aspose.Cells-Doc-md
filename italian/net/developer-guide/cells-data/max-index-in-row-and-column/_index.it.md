---
title: Ottieni l'indice massimo delle colonne nella riga e l'indice massimo delle righe nella colonna
type: docs
weight: 600
url: /it/net/get-max-index-in-row-and-column/
description: Scopri come ottenere l'indice massimo delle colonne nella riga e l'indice massimo delle righe nella colonna tramite Aspose.Cells for .NET API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **Possibili scenari di utilizzo**
Quando devi solo manipolare alcuni dati sulle righe o sulle colonne, devi conoscere l'intervallo di dati di righe e colonne. Aspose.Cells offre questa funzionalità. Per ottenere l'indice massimo di colonna su una riga, è possibile ottenere il file[Riga.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) E[Riga.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) proprietà, quindi utilizzare il file[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) per ottenere l'indice massimo della colonna e l'indice massimo della colonna dati. Ma per ottenere l'indice massimo delle righe e l'indice massimo dei dati delle righe su una colonna, è necessario creare un intervallo sulla colonna, quindi attraversare l'intervallo per trovare l'ultima cella e infine ottenere il valore[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attributo sulla cella.

Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Riga.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Riga.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Ottieni l'indice massimo delle colonne nella riga e l'indice massimo delle righe nella colonna utilizzando Aspose.Cells**
Questo esempio mostra come:

1.  Carica il[file di esempio](sample.xlsx).
1. Ottieni la riga che deve ottenere l'indice massimo della colonna e l'indice massimo della colonna dati.
1.  Ottenere[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) attributo sulla cella.
1. Crea un intervallo basato sulla colonna.
1. Ottieni l'iteratore e l'intervallo di attraversamento.
1.  Ottenere[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attributo sulla cella.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}