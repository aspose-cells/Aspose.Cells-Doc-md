---
title: Invia la forma avanti o indietro all interno del foglio di lavoro
type: docs
weight: 600
url: /it/java/send-shape-front-or-back-inside-the-worksheet/
---

## **Possibili Scenari di Utilizzo**

Quando sono presenti più forme nello stesso punto, la visibilità è determinata dalle posizioni dell'ordine Z. Aspose.Cells fornisce il metodo [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) che cambia la posizione dell'ordine Z della forma. Se vuoi inviare la forma in secondo piano, userai un numero negativo come -1, -2, -3, ecc. e se vuoi inviare la forma in primo piano, userai un numero positivo come 1, 2, 3, ecc.

## **Invia la forma avanti o indietro all'interno del foglio di lavoro**

Il seguente codice di esempio spiega l'uso del metodo [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)). Si prega di vedere il [file Excel di esempio](50528362.xlsx) utilizzato all'interno del codice e il [file Excel di output](50528361.xlsx) generato da esso. La schermata mostra l'effetto del codice sul file Excel di esempio in esecuzione.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
