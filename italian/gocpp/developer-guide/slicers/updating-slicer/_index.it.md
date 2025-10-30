---
title: Aggiornare il Filtro con Golang tramite C++
linktitle: Aggiornamento Slicer
type: docs
weight: 50
url: /it/go-cpp/updating-slicer/
description: Questo articolo mostra come aggiornare tabelle pivot collegate aggiornando lo slicer usando l API Aspose.Cells for C++.
keywords: Aspose.Cells C++ Aggiorna slicer, C++ come cambiare lo slicer, come regolare lo slicer in C++, come selezionare o deselezionare gli elementi dello slicer.
---

## **Possibili Scenari di Utilizzo**

Se vuoi aggiornare uno slicer in Microsoft Excel, seleziona o deseleziona gli elementi, quindi aggiornerà automaticamente la tabella dello slicer o la tabella pivot. Usa [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/) per selezionare o deselezionare gli elementi dello slicer con Aspose.Cells e poi chiama il metodo [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) per aggiornare la tabella dello slicer o la tabella pivot.

## **Come aggiornare il riquadro di selezione**

Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene un filtro esistente. Deseleziona il 2° e 3° elemento del filtro e aggiorna il filtro. Quindi salva il lavoro come [file Excel di output](67338476.xlsx). La seguente schermata mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, l'aggiornamento del filtro con gli elementi selezionati ha anche aggiornato la tabella pivot di conseguenza.

![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
