---
title: Ottenere l Indice Massimo della Colonna nella Riga e l Indice Massimo della Riga nella Colonna
type: docs
weight: 600
url: /it/nodejs-cpp/get-max-index-in-row-and-column/
description: Scopri come ottenere il massimo indice di colonna in riga e il massimo indice di riga in colonna attraverso l API Aspose.Cells for Node.js via C++.
keywords: Ottenere il massimo indice di colonna in riga con Node.js via C++, ottenere il massimo indice di riga in colonna con Node.js via C++, ottenere il massimo indice di colonna dati in riga con Node.js via C++, ottenere il massimo indice di riga dati in colonna con Node.js via C++.
---

## **Possibili Scenari di Utilizzo**
Quando hai bisogno di manipolare solo alcuni dati sulle righe o colonne, devi conoscere l'intervallo di dati di righe e colonne. Aspose.Cells for Node.js via C++ offre questa funzionalità. Per ottenere il massimo indice di colonna di una riga, puoi usare i metodi [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) e [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--), e poi usare il metodo [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) per ottenere il massimo indice di colonna e il massimo indice di colonna dati. Ma, per ottenere il massimo indice di riga e il massimo indice di dati di riga in una colonna, devi creare un intervallo sulla colonna, attraversarlo per trovare l'ultima cella, e infine chiamare il metodo [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) sulla cella.

Aspose.Cells for Node.js via C++ fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Ottenere il massimo indice di colonna in riga e il massimo indice di riga in colonna**
Questo esempio mostra come:

1. Caricare il [file di esempio](sample.xlsx).
1. Ottenere la riga che ha bisogno di ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati.
1. Chiama il metodo [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) sulla cella.
1. Creare un intervallo basato sulla colonna.
1. Ottenere l'iteratore e attraversare l'intervallo.
1. Chiama il metodo [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) sulla cella.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
