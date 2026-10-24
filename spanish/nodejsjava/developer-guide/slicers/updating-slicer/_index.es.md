---
title: Actualizar Slicer con Node.js a través de Java
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/nodejs-java/updating-slicer/
description: Este artículo muestra cómo actualizar un slicer para filtrar los datos de la tabla dinámica o tabla vinculada usando Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells Node.js via Java, Actualizar Slicer en Node.js, cómo cambiar el slicer en Node.js, cómo filtrar una tabla dinámica mediante slicer en Node.js, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Actualizar un slicer significa filtrar los datos de la tabla dinámica o tabla a la que está conectado el slicer. Cuando selecciona o deselecciona elementos del slicer en Microsoft Excel, la tabla dinámica o tabla vinculada se recalcula en consecuencia. Con Aspose.Cells for Node.js via Java, no necesita recorrer los elementos de la caché del slicer ni actualizar el slicer manualmente — el método [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs/slicer/) actualiza el slicer y recalcula la tabla dinámica o tabla vinculada directamente a partir de los elementos de filtro:
- `Slicer.selectItems(labels, append)` — selecciona las etiquetas especificadas y recalcula la tabla dinámica o tabla vinculada. Cuando `append` es `true`, las etiquetas seleccionadas originalmente se conservan y las etiquetas especificadas se añaden a la selección; cuando `append` es `false`, todas las selecciones originales se borran y solo permanecen seleccionadas las etiquetas especificadas.
- `Slicer.unselectItems(labels)` — deselecciona parte de los elementos seleccionados actualmente.
- `Slicer.clearFilter()` — elimina el filtro y selecciona todos los elementos.

{{% alert color="primary" %}}
A partir de Aspose.Cells for Node.js via Java 26.10, la propiedad `SlicerCacheItem.Selected` pasa a ser de solo lectura y su establecedor ya no se admite. Utilice los métodos `Slicer.selectItems`, `Slicer.unselectItems` y `Slicer.clearFilter` en lugar de establecer `SlicerCacheItem.Selected` elemento por elemento.
{{% /alert %}}

## **Cómo actualizar el slicer**
El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un slicer existente conectado a una tabla dinámica. Selecciona solo los elementos "Blue" y "Pink" del slicer con `Slicer.selectItems(labels, false)` — la tabla dinámica se recalcula directamente a partir de los elementos de filtro, sin una llamada manual a `Slicer.refresh()`. A continuación, guarda el libro de trabajo como el [archivo Excel de salida](67338476.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como puede ver en la captura de pantalla, la tabla dinámica muestra solo los elementos filtrados.
![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**
Reemplace la selección actual (solo permanecen seleccionadas las etiquetas especificadas) y recalcule la tabla dinámica o tabla vinculada:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Conserve las etiquetas seleccionadas actualmente y seleccione elementos adicionales:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Deseleccione parte de los elementos seleccionados:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Elimine el filtro (seleccione todos los elementos):

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-java" >}}