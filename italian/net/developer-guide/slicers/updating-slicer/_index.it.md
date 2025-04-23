---
title: Aggiornamento Slicer
type: docs
weight: 50
url: /it/net/updating-slicer/
description: Questo articolo mostra come aggiornare le tabelle pivot collegate aggiornando il riquadro di selezione tramite l API Aspose.Cells for .NET.
keywords: Aspose.Cells C# Aggiorna riquadro di selezione, C# come cambiare il riquadro di selezione, come regolare il riquadro di selezione in C#, come selezionare o deselezionare gli elementi del riquadro di selezione.
---

## **Possibili Scenari di Utilizzo**

Se vuoi aggiornare il riquadro di selezione in Microsoft Excel, seleziona o deseleziona i suoi elementi, quindi aggiornerà la tabella del riquadro di selezione o la tabella pivot di conseguenza. Utilizza [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems) per selezionare o deselezionare gli elementi del riquadro di selezione con Aspose.Cells e chiamare il metodo [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) per aggiornare la tabella del riquadro di selezione o la tabella pivot.

## **Come aggiornare il riquadro di selezione**

Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene un filtro esistente. Deseleziona il 2° e 3° elemento del filtro e aggiorna il filtro. Quindi salva il lavoro come [file Excel di output](67338476.xlsx). La seguente schermata mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, l'aggiornamento del filtro con gli elementi selezionati ha anche aggiornato la tabella pivot di conseguenza.

![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
