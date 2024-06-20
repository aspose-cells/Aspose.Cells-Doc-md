---
title: Formattazione delle celle
type: docs
weight: 50
url: /it/cpp/cells-formatting/
---

## **Formatta la cella o l'intervallo di celle**
Se desideri formattare la cella o l'intervallo di celle, Aspose.Cells fornisce la classe [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Puoi completare tutta la formattazione della cella o dell'intervallo di celle utilizzando questa classe. Alcune delle cose relative alla formattazione che possono essere realizzate con la classe IStyle sono le seguenti

- Imposta il colore di riempimento della cella
- Imposta il testo a capo della cella
- Imposta i bordi delle celle come i bordi superiore, sinistro, inferiore e destro, ecc.
- Imposta il colore del font, la dimensione del font, il nome del font, la cancelletto, grassetto, corsivo, sottolineato, ecc.
- Imposta l'allineamento del testo orizzontale o verticale a destra, sinistra, in alto, in basso, al centro, ecc.

Se si desidera impostare lo stile di una singola cella, utilizzare il metodo [Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) e se si desidera impostare lo stile di un intervallo di celle, utilizzare il metodo [Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).
## **Codice di Esempio**
Il seguente codice di esempio formatta la cella C4 del foglio di lavoro in vari modi e la schermata mostra il [file Excel di output](21266438.xlsx) generato per il riferimento.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
