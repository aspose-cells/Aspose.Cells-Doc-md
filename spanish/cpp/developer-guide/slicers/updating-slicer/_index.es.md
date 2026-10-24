---
title: Actualización del Slicer con C++
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/cpp/updating-slicer/
description: Este artículo muestra cómo actualizar un slicer para filtrar los datos de la tabla dinámica o tabla vinculada mediante la API de Aspose.Cells for C++.
keywords: Aspose.Cells C++ Actualizar slicer, C++ cómo cambiar el slicer, cómo filtrar una tabla dinámica mediante slicer en C++, C++ Slicer SelectItems, C++ Slicer ClearFilter, C++ Slicer UnselectItems.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Actualizar un slicer significa filtrar los datos de la tabla dinámica o tabla a la que está conectado el slicer. Cuando selecciona o deselecciona elementos del slicer en Microsoft Excel, la tabla dinámica o tabla vinculada se recalcula en consecuencia. Con Aspose.Cells for C++, no necesita recorrer los elementos de la caché del slicer ni actualizar el slicer manualmente — el método [**Slicer.SelectItems(Vector&lt;U16String&gt;, bool)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/selectitems/) actualiza el slicer y recalcula la tabla dinámica o tabla vinculada directamente a partir de los elementos de filtro:
- `Slicer.SelectItems(labels, append)` — selecciona las etiquetas especificadas y recalcula la tabla dinámica o tabla vinculada. Cuando `append` es `true`, las etiquetas seleccionadas originalmente se conservan y las etiquetas especificadas se añaden a la selección; cuando `append` es `false`, todas las selecciones originales se borran y solo permanecen seleccionadas las etiquetas especificadas.
- `Slicer.UnselectItems(labels)` — deselecciona parte de los elementos seleccionados actualmente.
- `Slicer.ClearFilter()` — elimina el filtro y selecciona todos los elementos.

{{% alert color="primary" %}}
A partir de Aspose.Cells for C++ 26.10, la propiedad `SlicerCacheItem.Selected` pasa a ser de solo lectura y su establecedor ya no se admite. Utilice los métodos `Slicer.SelectItems`, `Slicer.UnselectItems` y `Slicer.ClearFilter` en lugar de establecer `SlicerCacheItem.Selected` elemento por elemento.
{{% /alert %}}

## **Cómo actualizar el slicer**
El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un slicer existente conectado a una tabla dinámica. Selecciona solo los elementos "Blue" y "Pink" del slicer con `Slicer.SelectItems(labels, false)` — la tabla dinámica se recalcula directamente a partir de los elementos de filtro, sin una llamada manual a `Slicer.Refresh()`. A continuación, guarda el libro de trabajo como el [archivo Excel de salida](67338476.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como puede ver en la captura de pantalla, la tabla dinámica muestra solo los elementos filtrados.
![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**
Reemplace la selección actual (solo permanecen seleccionadas las etiquetas especificadas) y recalcule la tabla dinámica o tabla vinculada:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);
    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);
    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    Vector<U16String> labels{ u"Blue", u"Pink" };
    slicer.SelectItems(labels, false);
    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);
    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Conserve las etiquetas seleccionadas actualmente y seleccione elementos adicionales:

```cpp
// Keep the current selection and add "Red" to it.
Vector<U16String> moreLabels{ u"Red" };
slicer.SelectItems(moreLabels, true);
```

Deseleccione parte de los elementos seleccionados:

```cpp
// Remove "Pink" from the current selection.
Vector<U16String> toRemove{ u"Pink" };
slicer.UnselectItems(toRemove);
```

Elimine el filtro (seleccione todos los elementos):

```cpp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="cpp" >}}