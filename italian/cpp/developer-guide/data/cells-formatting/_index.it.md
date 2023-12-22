---
title: Cells Formattazione
type: docs
weight: 50
url: /it/cpp/cells-formatting/
---
##  **Formato Cell o intervallo Cells**
 Se desideri formattare una cella o un intervallo di celle, Aspose.Cells fornisce il file[Stile](https://reference.aspose.com/cells/cpp/aspose.cells/style/)classe. Puoi eseguire tutta la formattazione della cella o dell'intervallo di celle utilizzando questa classe. Di seguito sono riportate alcune delle operazioni relative alla formattazione che possono essere eseguite con la classe IStyle

- Imposta il colore di riempimento della cella
- Imposta il testo a capo della cella
- Imposta i bordi delle celle come i bordi superiore, sinistro, inferiore e destro, ecc.
- Imposta il colore del carattere, la dimensione del carattere, il nome del carattere, barrato, grassetto, corsivo, sottolineato, ecc.
- Imposta l'allineamento orizzontale o verticale del testo su destra, sinistra, alto, basso, centro, ecc.

 Se desideri impostare lo stile di una singola cella, utilizza[Cell->ImpostaStile()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) metodo e se desideri impostare lo stile di un intervallo di celle, utilizza[Intervallo->ApplicaStile()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)metodo.
##  **Codice d'esempio**
 Il seguente codice di esempio formatta la cella C4 del foglio di lavoro in vari modi e lo screenshot mostra il file[file Excel di output](21266438.xlsx) generato da esso per riferimento.

![cose da fare:immagine_alt_testo](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
