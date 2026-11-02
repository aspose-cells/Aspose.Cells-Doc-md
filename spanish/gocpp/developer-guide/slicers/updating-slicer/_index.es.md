---
title: Actualizar Slicer con Golang vía C++
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Este artículo muestra cómo actualizar un slicer para filtrar los datos de la tabla dinámica o tabla vinculada mediante la API de Aspose.Cells for Go via C++.
keywords: Aspose.Cells Go via C++ Actualizar slicer, Go cómo cambiar el slicer, cómo filtrar una tabla dinámica mediante slicer en Go, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Escenarios de uso posibles**
Actualizar un slicer significa filtrar los datos de la tabla dinámica o tabla a la que está conectado el slicer. Cuando selecciona o deselecciona elementos del slicer en Microsoft Excel, la tabla dinámica o tabla vinculada se recalcula en consecuencia. Con Aspose.Cells for Go via C++, no necesita recorrer los elementos de la caché del slicer ni actualizar el slicer manualmente — el método [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) actualiza el slicer y recalcula la tabla dinámica o tabla vinculada directamente a partir de los elementos de filtro:
- `Slicer.SelectItems(labels, append)` — selecciona las etiquetas especificadas y recalcula la tabla dinámica o tabla vinculada. Cuando `append` es `true`, las etiquetas seleccionadas originalmente se conservan y las etiquetas especificadas se añaden a la selección; cuando `append` es `false`, todas las selecciones originales se borran y solo permanecen seleccionadas las etiquetas especificadas.
- `Slicer.UnselectItems(labels)` — deselecciona parte de los elementos seleccionados actualmente.
- `Slicer.ClearFilter()` — elimina el filtro y selecciona todos los elementos.

{{% alert color="primary" %}}
A partir de Aspose.Cells for Go via C++ 26.10, la propiedad `SlicerCacheItem.Selected` pasa a ser de solo lectura y su establecedor ya no se admite. Utilice los métodos `Slicer.SelectItems`, `Slicer.UnselectItems` y `Slicer.ClearFilter` en lugar de establecer `SlicerCacheItem.Selected` elemento por elemento.
{{% /alert %}}

## **Cómo actualizar el slicer**
El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un slicer existente conectado a una tabla dinámica. Selecciona solo los elementos "Blue" y "Pink" del slicer con `Slicer.SelectItems(labels, false)` — la tabla dinámica se recalcula directamente a partir de los elementos de filtro, sin una llamada manual a `Slicer.Refresh()`. A continuación, guarda el libro de trabajo como el [archivo Excel de salida](67338476.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como puede ver en la captura de pantalla, la tabla dinámica muestra solo los elementos filtrados.
![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**
Reemplace la selección actual (solo permanecen seleccionadas las etiquetas especificadas) y recalcule la tabla dinámica o tabla vinculada:

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

Conserve las etiquetas seleccionadas actualmente y seleccione elementos adicionales:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Deseleccione parte de los elementos seleccionados:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Elimine el filtro (seleccione todos los elementos):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}