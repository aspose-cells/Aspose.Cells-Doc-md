---
title: Porta le forme avanti o indietro in un foglio di lavoro
type: docs
weight: 3400
url: /it/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **Possibili Scenari di Utilizzo**

Quando ci sono più forme presenti nello stesso punto, la loro visibilità è decisa dalle loro posizioni nell'ordine z. Aspose.Cells fornisce il metodo [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) che cambia la posizione nell'ordine z della forma. Se vuoi inviare la forma in background, userai un numero negativo come -1, -2, -3, ecc. e se vuoi inviare la forma in primo piano, userai un numero positivo come 1, 2, 3, ecc.

## **Porta Forma avanti o indietro all'interno del foglio di lavoro**

Il seguente esempio di codice spiega l'uso del metodo [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)). Per favore, guarda il [file Excel di esempio](sampleToFrontOrBack.xlsx) usato nel codice e il [file Excel di output](50528331.xlsx) generato da esso. La schermata mostra l'effetto del codice sul file Excel di esempio durante l'esecuzione.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
