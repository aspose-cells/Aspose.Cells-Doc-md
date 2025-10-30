---
title: Actualizar Segmentador con Node.js a través de C++
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/nodejs-cpp/updating-slicer/
description: Este artículo muestra cómo actualizar tablas dinámicas vinculadas actualizando el segmentador usando Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js a través de C++, Actualizar segmentador en Node.js, cómo cambiar el segmentador en Node.js, cómo ajustar el segmentador en Node.js, cómo seleccionar o deseleccionar los elementos del segmentador en Node.js con C++.
---

## **Escenarios de uso posibles**

Si deseas actualizar un segmentador en Microsoft Excel, selecciona o deselecciona sus elementos, y el segmentador actualizará la tabla o la tabla dinámica en consecuencia. Usa [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) para seleccionar o deseleccionar elementos del segmentador con Aspose.Cells y luego llama al método [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) para actualizar la tabla o la tabla dinámica.

## **Cómo actualizar filtro**

El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un filtro existente. Desactiva los elementos 2 y 3 del filtro y actualiza el filtro. Luego guarda el libro de trabajo como [archivo Excel de salida](67338476.xlsx). La captura de pantalla siguiente muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, al actualizar el filtro con los elementos seleccionados también se ha actualizado la tabla dinámica correspondientemente.

![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
