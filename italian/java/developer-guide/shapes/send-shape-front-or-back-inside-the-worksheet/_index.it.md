---
title: Invia la forma davanti o dietro all'interno del foglio di lavoro
type: docs
weight: 600
url: /it/java/send-shape-front-or-back-inside-the-worksheet/
---
## **Possibili scenari di utilizzo**

Quando sono presenti più forme nella stessa posizione, il modo in cui saranno visibili viene deciso dalle loro posizioni in ordine z. Aspose.Cells fornisce[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) metodo che modifica la posizione dell'ordine z della forma. Se vuoi mandare la forma in secondo piano userai un numero negativo come -1, -2, -3, ecc. e se vuoi mandare la forma in primo piano, userai un numero positivo come 1, 2, 3, eccetera.

## **Invia la forma davanti o dietro all'interno del foglio di lavoro**

Il seguente codice di esempio spiega l'utilizzo di[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) metodo. Si prega di consultare il[esempio di file Excel](50528362.xlsx)utilizzato all'interno del codice e il[file Excel di output](50528361.xlsx)generato da esso. Lo screenshot mostra l'effetto del codice sul file Excel di esempio durante l'esecuzione.

![cose da fare:immagine_alt_testo](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
