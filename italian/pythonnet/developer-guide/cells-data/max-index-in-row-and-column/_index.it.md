---
title: Ottenere l Indice Massimo della Colonna nella Riga e l Indice Massimo della Riga nella Colonna
type: docs
weight: 600
url: /it/python-net/get-max-index-in-row-and-column/
description: Scopri come ottenere l Indice Massimo della Colonna nella Riga e l Indice Massimo della Riga nella Colonna tramite Aspose.Cells per Python via .NET API.
keywords: Libreria Excel di Python, Ottieni l Indice Massimo della Colonna nella Riga con Python, Ottieni l Indice Massimo della Riga nella Colonna con Python, Ottieni l Indice Massimo della Colonna dei Dati nella Riga con Python, Ottieni l Indice Massimo della Riga dei Dati nella Colonna con Python. 
---

## **Possibili Scenari di Utilizzo**
Quando è necessario manipolare solo alcuni dati sulle righe o colonne, è necessario conoscere l'intervallo di dati delle righe e delle colonne. Aspose.Cells per Python via .NET offre questa funzionalità. Per ottenere l'indice massimo della colonna su una riga, è possibile ottenere le proprietà [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) e [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/), e quindi utilizzare la proprietà [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) per ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati. Ma per ottenere l'indice massimo della riga e l'indice massimo della riga dei dati su una colonna, è necessario creare un intervallo sulla colonna, quindi attraversare l'intervallo per trovare l'ultima cella e infine ottenere l'attributo [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) sulla cella.

Aspose.Cells per Python via .NET fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Ottieni l'Indice Massimo della Colonna nella Riga e l'Indice Massimo della Riga nella Colonna utilizzando la libreria Excel Aspose.Cells for Python**
Questo esempio mostra come:

1. Caricare il [file di esempio](sample.xlsx).
1. Ottenere la riga che ha bisogno di ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati.
1. Ottenere l'attributo [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) sulla cella.
1. Creare un intervallo basato sulla colonna.
1. Ottenere l'iteratore e attraversare l'intervallo.
1. Ottieni l'attributo [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) sulla cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
{{< app/cells/assistant language="python-net" >}}
