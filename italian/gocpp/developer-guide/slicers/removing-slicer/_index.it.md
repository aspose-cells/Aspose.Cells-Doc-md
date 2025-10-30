---
title: Rimuovere il Filtro con Golang tramite C++
linktitle: Rimozione del filtro
type: docs
weight: 30
url: /it/go-cpp/removing-slicer/
description: Impara come rimuovere slicer nei file Excel programmaticamente usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi rimuovere un slicer in Microsoft Excel, selezionalo e premi il pulsante *Elimina*. Allo stesso modo, se vuoi rimuoverlo usando l'API di Aspose.Cells programmaticamente, utilizza il metodo [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/go-cpp/slicercollection/remove/). Rimuoverà il slicer dal foglio di lavoro.

## **Rimozione dello slicer**

Il seguente codice di esempio carica il [file Excel di esempio](67338478.xlsx) che contiene un filtro esistente. Accede ai filtri e li rimuove. Infine, salva il lavoro come [file Excel di output](67338477.xlsx). La seguente schermata mostra il filtro che verrà rimosso dopo l'esecuzione del codice di esempio.

![todo:image_alt_text](removing-slicer_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingSlicer.go" >}}
