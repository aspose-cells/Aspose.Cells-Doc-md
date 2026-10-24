---
title: Actualización de Slicer
linktitle: Actualización de Slicer
type: docs
weight: 60
url: /es/python-java/updating-slicer/
description: Este artículo muestra cómo actualizar un slicer para filtrar los datos de la tabla dinámica o tabla vinculada mediante la API de Aspose.Cells for Python via Java.
keywords: Aspose.Cells for Python via Java Actualizar slicer, Python Java actualizar Slicer, cómo filtrar una tabla dinámica mediante slicer en Python, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Actualización del slicer**
Actualizar un slicer significa filtrar los datos de la tabla dinámica o tabla a la que está conectado el slicer. Aspose.Cells for Python via Java actualiza el slicer y recalcula la tabla dinámica o tabla vinculada directamente a partir de los elementos de filtro:
- `Slicer.selectItems(labels, append)` — selecciona las etiquetas especificadas y recalcula la tabla dinámica o tabla vinculada. Cuando `append` es `True`, las etiquetas seleccionadas originalmente se conservan y las etiquetas especificadas se añaden a la selección; cuando `append` es `False`, todas las selecciones originales se borran y solo permanecen seleccionadas las etiquetas especificadas.
- `Slicer.unselectItems(labels)` — deselecciona parte de los elementos seleccionados actualmente.
- `Slicer.clearFilter()` — elimina el filtro y selecciona todos los elementos.

{{% alert color="primary" %}}
A partir de Aspose.Cells for Python via Java 26.10, la propiedad `SlicerCacheItem.Selected` pasa a ser de solo lectura y su establecedor ya no se admite. Utilice los métodos `Slicer.selectItems`, `Slicer.unselectItems` y `Slicer.clearFilter` en lugar de establecer `SlicerCacheItem.Selected` elemento por elemento.
El siguiente fragmento de código carga el [archivo de Excel de ejemplo](106365050.xlsx) que contiene un slicer conectado a una tabla dinámica. Selecciona solo los elementos "Blue" y "Pink" del slicer con `Slicer.selectItems(labels, False)` — la tabla dinámica se recalcula directamente a partir de los elementos de filtro, sin una llamada manual a `Slicer.refresh()`. Luego guarda el libro de trabajo como el [archivo de Excel de salida](106365051.xlsx). La siguiente captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo. Como puede ver en la captura de pantalla, la tabla dinámica muestra solo los elementos filtrados.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Código de muestra**
Reemplace la selección actual (solo permanecen seleccionadas las etiquetas especificadas) y recalcule la tabla dinámica o tabla vinculada:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

Conserve las etiquetas seleccionadas actualmente y seleccione elementos adicionales:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Deseleccione parte de los elementos seleccionados:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Elimine el filtro (seleccione todos los elementos):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}