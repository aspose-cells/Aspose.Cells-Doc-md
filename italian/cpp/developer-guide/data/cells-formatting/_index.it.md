---
title: Cells Formattazione
type: docs
weight: 50
url: /it/cpp/cells-formatting/
---
## **Formato Cell o Intervallo di Cells**
 Se desideri formattare una cella o un intervallo di celle, Aspose.Cells fornisce il file[Stile](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)classe. Puoi eseguire tutta la formattazione della cella o dell'intervallo di celle utilizzando questa classe. Di seguito sono riportate alcune delle cose relative alla formattazione che possono essere eseguite con la classe IStyle

- Imposta il colore di riempimento della cella
- Imposta il testo a capo della cella
- Imposta i bordi delle celle come i bordi superiore, sinistro, inferiore e destro, ecc.
- Imposta il colore del carattere, la dimensione del carattere, il nome del carattere, il carattere barrato, il grassetto, il corsivo, il sottolineato, ecc.
- Imposta l'allineamento orizzontale o verticale del testo su destra, sinistra, alto, basso, centro, ecc.

 Se si desidera impostare lo stile di una singola cella, utilizzare[ICell->SetIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5) metodo e se si desidera impostare lo stile di un intervallo di celle, utilizzare[IRange->ApplicaIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)metodo.
## **Codice di esempio**
 Il seguente codice di esempio formatta la cella C4 del foglio di lavoro in vari modi e lo screenshot mostra il file[file excel di output](21266438.xlsx) generato da esso per il vostro riferimento.

![cose da fare:immagine_alt_testo](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
