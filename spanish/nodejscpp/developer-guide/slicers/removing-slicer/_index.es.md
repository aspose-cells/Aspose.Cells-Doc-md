---
title: Eliminar segmentador con Node.js a través de C++
linktitle: Eliminar filtro
type: docs
weight: 30
url: /es/nodejs-cpp/removing-slicer/
---

## **Escenarios de uso posibles**

Si deseas eliminar un segmentador en Excel, simplemente selecciónalo y presiona el botón *Eliminar*. De manera similar, si quieres eliminarlo usando la API de Aspose.Cells programáticamente, usa el método [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-). Esto eliminará el segmentador de la hoja de trabajo.

## **Eliminar rebanador**

El siguiente código de ejemplo carga el [archivo Excel de muestra](67338478.xlsx) que contiene un segmentador existente. Accede a los segmentadores y luego lo elimina. Finalmente, guarda el libro como [archivo Excel de salida](67338477.xlsx). La siguiente captura de pantalla muestra el segmentador que será eliminado después de la ejecución del código de ejemplo.

![todo:image_alt_text](removing-slicer_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
