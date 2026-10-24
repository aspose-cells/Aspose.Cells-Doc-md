---
title: Actualización de Slicer
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/java/updating-slicer/
description: Este artículo muestra cómo actualizar un slicer para filtrar los datos de la tabla dinámica o tabla vinculada mediante la API de Aspose.Cells for Java.
keywords: Aspose.Cells Java Actualizar slicer, Java cómo cambiar el slicer, cómo filtrar una tabla dinámica mediante slicer en Java, Java Slicer selectItems, Java Slicer clearFilter, Java Slicer unselectItems.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Actualizar un slicer significa filtrar los datos de la tabla dinámica o tabla a la que está conectado el slicer. Cuando selecciona o deselecciona elementos del slicer en Microsoft Excel, la tabla dinámica o tabla vinculada se recalcula en consecuencia. Con Aspose.Cells for Java, no necesita recorrer los elementos de la caché del slicer ni actualizar el slicer manualmente — el método [Slicer.selectItems(String[], boolean)](https://reference.aspose.com/cells/java/com.aspose.cells/slicer/#selectItems-java.lang.String---boolean-) actualiza el slicer y recalcula la tabla dinámica o tabla vinculada directamente a partir de los elementos de filtro:
- `Slicer.selectItems(labels, append)` — selecciona las etiquetas especificadas y recalcula la tabla dinámica o tabla vinculada. Cuando `append` es `true`, las etiquetas seleccionadas originalmente se conservan y las etiquetas especificadas se añaden a la selección; cuando `append` es `false`, todas las selecciones originales se borran y solo permanecen seleccionadas las etiquetas especificadas.
- `Slicer.unselectItems(labels)` — deselecciona parte de los elementos seleccionados actualmente.
- `Slicer.clearFilter()` — elimina el filtro y selecciona todos los elementos.

{{% alert color="primary" %}}
A partir de Aspose.Cells for Java 26.10, la propiedad `SlicerCacheItem.Selected` pasa a ser de solo lectura y su establecedor ya no se admite. Utilice los métodos `Slicer.selectItems`, `Slicer.unselectItems` y `Slicer.clearFilter` en lugar de establecer `SlicerCacheItem.Selected` elemento por elemento.
{{% /alert %}}

## **Actualización del slicer**
El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](67338506.xlsx) que contiene un slicer existente conectado a una tabla dinámica. Selecciona solo los elementos "Blue" y "Pink" del slicer con `Slicer.selectItems(labels, false)` — la tabla dinámica se recalcula directamente a partir de los elementos de filtro, sin una llamada manual a `Slicer.refresh()`. A continuación, guarda el libro de trabajo como el [archivo de Excel de salida](67338505.xlsx). La siguiente captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo. Como puede ver en la captura de pantalla, la tabla dinámica muestra solo los elementos filtrados.
![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**
Reemplace la selección actual (solo permanecen seleccionadas las etiquetas especificadas) y recalcule la tabla dinámica o tabla vinculada:

```java
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
import com.aspose.cells.Slicer;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(new String[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Conserve las etiquetas seleccionadas actualmente y seleccione elementos adicionales:

```java
// Keep the current selection and add "Red" to it.
slicer.selectItems(new String[] { "Red" }, true);
```

Deseleccione parte de los elementos seleccionados:

```java
// Remove "Pink" from the current selection.
slicer.unselectItems(new String[] { "Pink" });
```

Elimine el filtro (seleccione todos los elementos):

```java
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="java" >}}