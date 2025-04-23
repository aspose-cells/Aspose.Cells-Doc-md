---  
title: Formatear Segmentador con Node.js a través de C++  
linktitle: Formato de filtro  
type: docs  
weight: 20  
url: /es/nodejs-cpp/formatting-slicer/  
---  

## **Escenarios de uso posibles**  

Puedes formatear el segmentador en Microsoft Excel configurando su número de columnas o su estilo, etc. Aspose.Cells for Node.js via C++ también permite hacer esto usando las propiedades [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) y [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--).  

## ** Formatear rebanador**  

Consulte el siguiente código, carga el [archivo Excel de muestra](67338473.xlsx) que contiene un filtro. Accede al filtro, ajusta su número de columnas, tipo de estilo y lo guarda como [archivo Excel de salida](67338474.xlsx). La captura de pantalla muestra cómo se ve el filtro después de la ejecución del código de ejemplo.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

