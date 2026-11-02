---
title: Aggiornamento dello slicer con Golang tramite C++
linktitle: Aggiornamento dello slicer
type: docs
weight: 50
url: /it/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Questo articolo mostra come aggiornare uno slicer per filtrare i dati della Tabella Pivot o della tabella collegata utilizzando l'API Aspose.Cells for Go via C++.
keywords: Aspose.Cells Go via C++ Aggiorna slicer, Go come cambiare lo slicer, come filtrare una Tabella Pivot tramite slicer in Go, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Possibili Scenari di Utilizzo**
Aggiornare uno slicer significa filtrare i dati della Tabella Pivot o della tabella a cui lo slicer è collegato. Quando si selezionano o si deselezionano gli elementi dello slicer in Microsoft Excel, la Tabella Pivot o la tabella collegata viene ricalcolata di conseguenza. Con Aspose.Cells for Go via C++, non è necessario iterare gli elementi della cache dello slicer e aggiornare manualmente lo slicer — il metodo [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) aggiorna lo slicer e ricalcola la Tabella Pivot o la tabella collegata direttamente dagli elementi del filtro:
- `Slicer.SelectItems(labels, append)` — seleziona le etichette specificate e ricalcola la Tabella Pivot o la tabella collegata. Quando `append` è `true`, le etichette originariamente selezionate vengono mantenute e le etichette specificate vengono aggiunte alla selezione; quando `append` è `false`, tutte le selezioni originali vengono cancellate e solo le etichette specificate restano selezionate.
- `Slicer.UnselectItems(labels)` — deseleziona parte degli elementi attualmente selezionati.
- `Slicer.ClearFilter()` — rimuove il filtro e seleziona tutti gli elementi.

{{% alert color="primary" %}}
A partire da Aspose.Cells for Go via C++ 26.10, la proprietà `SlicerCacheItem.Selected` diventa di sola lettura e il relativo setter non è più supportato. Utilizzare i metodi `Slicer.SelectItems`, `Slicer.UnselectItems` e `Slicer.ClearFilter` anziché impostare `SlicerCacheItem.Selected` elemento per elemento.
{{% /alert %}}

## **Come aggiornare lo slicer**
Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene uno slicer esistente collegato a una Tabella Pivot. Seleziona solo gli elementi "Blue" e "Pink" dello slicer con `Slicer.SelectItems(labels, false)` — la Tabella Pivot viene ricalcolata direttamente dagli elementi del filtro, senza una chiamata manuale a `Slicer.Refresh()`. Salva quindi la cartella di lavoro come [file Excel di output](67338476.xlsx). La schermata seguente mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, la Tabella Pivot mostra solo gli elementi filtrati.
![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**
Sostituire la selezione corrente (restano selezionate solo le etichette specificate) e ricalcolare la Tabella Pivot o la tabella collegata:

```go
package main

import (
    "fmt"

    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")

    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)

    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)

    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)

    // Save the modified workbook.
    wb.Save_String("out.xlsx")

    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

Mantenere le etichette attualmente selezionate e selezionare ulteriori elementi:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Deselezionare parte degli elementi selezionati:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Rimuovere il filtro (selezionare tutti gli elementi):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}