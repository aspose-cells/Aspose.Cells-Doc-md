---
title: Actualización de Slicer
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/python-net/updating-slicer/
description: Aprenda cómo actualizar un slicer para filtrar los datos de la tabla dinámica o tabla vinculada con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca de Excel para Python, Python actualizar Slicer sin Excel, filtrar tabla dinámica mediante slicer en Python, Slicer select_items, Slicer clear_filter.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Actualizar un slicer significa filtrar los datos de la tabla dinámica o tabla a la que está conectado el slicer. Cuando selecciona o deselecciona elementos del slicer en Microsoft Excel, la tabla dinámica o tabla vinculada se recalcula en consecuencia. Con Aspose.Cells for Python via .NET, no necesita recorrer los elementos de la caché del slicer ni actualizar el slicer manualmente — el método [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) actualiza el slicer y recalcula la tabla dinámica o tabla vinculada directamente a partir de los elementos de filtro:
- `Slicer.select_items(labels, append)` — selecciona las etiquetas especificadas y recalcula la tabla dinámica o tabla vinculada. Cuando `append` es `True`, las etiquetas seleccionadas originalmente se conservan y las etiquetas especificadas se añaden a la selección; cuando `append` es `False`, todas las selecciones originales se borran y solo permanecen seleccionadas las etiquetas especificadas.
- `Slicer.unselect_items(labels)` — deselecciona parte de los elementos seleccionados actualmente.
- `Slicer.clear_filter()` — elimina el filtro y selecciona todos los elementos.

{{% alert color="primary" %}}
A partir de Aspose.Cells for Python via .NET 26.10, la propiedad `SlicerCacheItem.selected` pasa a ser de solo lectura y su establecedor ya no se admite. Utilice los métodos `Slicer.select_items`, `Slicer.unselect_items` y `Slicer.clear_filter` en lugar de establecer `SlicerCacheItem.selected` elemento por elemento.
{{% /alert %}}

## **Cómo actualizar Slicer usando la biblioteca Excel de Aspose.Cells para Python**
El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un slicer existente conectado a una tabla dinámica. Selecciona solo los elementos "Blue" y "Pink" del slicer con `Slicer.select_items(labels, False)` — la tabla dinámica se recalcula directamente a partir de los elementos de filtro, sin una llamada manual a `Slicer.refresh()`. A continuación, guarda el libro de trabajo como el [archivo Excel de salida](67338476.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como puede ver en la captura de pantalla, la tabla dinámica muestra solo los elementos filtrados.
![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**
Reemplace la selección actual (solo permanecen seleccionadas las etiquetas especificadas) y recalcule la tabla dinámica o tabla vinculada:

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

Conserve las etiquetas seleccionadas actualmente y seleccione elementos adicionales:

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

Deseleccione parte de los elementos seleccionados:

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

Elimine el filtro (seleccione todos los elementos):

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}