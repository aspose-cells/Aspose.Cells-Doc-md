---
title: Porta in primo o in secondo piano le forme all interno del foglio di lavoro con Golang tramite C++
linktitle: Invia la forma avanti o indietro all interno del foglio di lavoro
type: docs
weight: 3400
url: /it/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Impara come cambiare la posizione Z order delle forme in un foglio di lavoro usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando ci sono più forme presenti nello stesso luogo, la loro visibilità è determinata dalle loro posizioni di z-ordine. Aspose.Cells offre il metodo [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/), che cambia la posizione di z-ordine della forma. Se si desidera inviare una forma in background, si utilizza un numero negativo come -1, -2, -3, ecc. Se si desidera portare una forma in primo piano, si utilizza un numero positivo come 1, 2, 3, ecc.

## **Invia la forma avanti o indietro all'interno del foglio di lavoro**

Il seguente esempio di codice dimostra l'uso del metodo [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/). Si prega di consultare il [file Excel di esempio](50528330.xlsx) utilizzato nel codice e il [file Excel di output](50528331.xlsx) generato da esso. Lo screenshot mostra l'effetto del codice sul file Excel di esempio all'esecuzione.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
