---
title: Invia la forma avanti o indietro all interno del foglio di lavoro
type: docs
weight: 3400
url: /it/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **Possibili Scenari di Utilizzo**

Quando ci sono più forme presenti nella stessa posizione, la visibleità viene decisa dalla loro posizione z-order. Aspose.Cells per Python via .NET fornisce il metodo [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) che cambia la posizione z-order della forma. Se si desidera inviare la forma dietro, si userà un numero negativo come -1, -2, -3, ecc., e se si desidera portare la forma in primo piano, si userà un numero positivo come 1, 2, 3, ecc.

## **Invia la forma avanti o indietro all'interno del foglio di lavoro**

Il seguente codice di esempio spiega l'uso del metodo [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back). Si prega di consultare il [file Excel di esempio](50528330.xlsx) utilizzato nel codice e il [file Excel di output](50528331.xlsx) generato da esso. La schermata mostra l'effetto del codice sul file Excel di esempio in esecuzione.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
